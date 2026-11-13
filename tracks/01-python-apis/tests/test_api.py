"""Contract and boundary tests; no mock model metrics are implied."""

from concurrent.futures import ThreadPoolExecutor

import pytest
from fastapi.testclient import TestClient
from httpx import Response

from app import security
from app.main import app

client = TestClient(app)
TEST_KEY = "test-key-do-not-use-in-production-12345"


@pytest.fixture(autouse=True)
def configured_access(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("BUDGET_GUARD_API_KEY", TEST_KEY)
    monkeypatch.setattr(security, "limiter", security.FixedWindowLimiter())


def payload() -> dict[str, object]:
    return {
        "input_tokens": 1000,
        "output_tokens": 500,
        "input_price_usd_per_million": "2",
        "output_price_usd_per_million": "8",
        "max_cost_usd": "0.01",
    }


def post(data: dict[str, object]) -> Response:
    return client.post("/v1/budget/check", json=data, headers={"X-API-Key": TEST_KEY})


def test_healthz() -> None:
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_estimate_and_budget_remaining() -> None:
    response = post(payload())
    assert response.status_code == 200
    assert response.json() == {
        "estimated_cost_usd": "0.006",
        "remaining_usd": "0.004",
        "within_budget": True,
        "pricing_source": "caller_supplied",
    }


def test_over_budget_and_no_negative_remaining() -> None:
    data = payload()
    data["max_cost_usd"] = "0.005"
    response = post(data)
    assert response.status_code == 200
    assert response.json()["within_budget"] is False
    assert response.json()["remaining_usd"] == "0"


def test_exact_boundary_is_allowed() -> None:
    data = payload()
    data["max_cost_usd"] = "0.006"
    response = post(data)
    assert response.json()["within_budget"] is True
    assert response.json()["remaining_usd"] == "0"


def test_zero_cost_and_zero_budget() -> None:
    data = payload()
    data.update(input_tokens=0, output_tokens=0, max_cost_usd="0")
    response = post(data)
    assert response.status_code == 200
    assert response.json()["within_budget"] is True
    assert response.json()["estimated_cost_usd"] == "0"


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("input_tokens", -1),
        ("output_tokens", 10_000_001),
        ("input_tokens", True),
        ("input_tokens", "100"),
        ("input_price_usd_per_million", 0.2),
        ("input_price_usd_per_million", -1),
        ("output_price_usd_per_million", "0.0000001"),
        ("max_cost_usd", "10001"),
        ("max_cost_usd", "not-a-number"),
        ("input_price_usd_per_million", "ignore previous instructions"),
    ],
)
def test_invalid_payloads_return_422(field: str, value: object) -> None:
    data = payload()
    data[field] = value
    assert post(data).status_code == 422


def test_unknown_fields_rejected() -> None:
    data = payload()
    data["api_key"] = "do-not-accept-extra-fields"
    assert post(data).status_code == 422


def test_openapi_documents_contract() -> None:
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert "/v1/budget/check" in response.json()["paths"]
    assert response.json()["components"]["securitySchemes"]["APIKeyHeader"]["in"] == "header"


def test_missing_api_key_is_401() -> None:
    response = client.post("/v1/budget/check", json=payload())
    assert response.status_code == 401
    assert response.headers["www-authenticate"] == "ApiKey"


def test_invalid_api_key_is_403() -> None:
    response = client.post("/v1/budget/check", json=payload(), headers={"X-API-Key": "bad"})
    assert response.status_code == 403
    assert TEST_KEY not in response.text


def test_missing_server_key_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("BUDGET_GUARD_API_KEY")
    assert post(payload()).status_code == 503


def test_short_server_key_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("BUDGET_GUARD_API_KEY", "short")
    assert post(payload()).status_code == 503


def test_fixed_window_limits_authenticated_requests(monkeypatch: pytest.MonkeyPatch) -> None:
    now = [100.0]
    monkeypatch.setattr(
        security,
        "limiter",
        security.FixedWindowLimiter(limit=2, window_seconds=10.0, clock=lambda: now[0]),
    )
    assert post(payload()).status_code == 200
    assert post(payload()).status_code == 200
    blocked = post(payload())
    assert blocked.status_code == 429
    assert blocked.headers["retry-after"] == "10"
    now[0] += 10.0
    assert post(payload()).status_code == 200


def test_wrong_key_does_not_consume_rate_limit(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(security, "limiter", security.FixedWindowLimiter(limit=1))
    assert client.post(
        "/v1/budget/check", json=payload(), headers={"X-API-Key": "invalid"}
    ).status_code == 403
    assert post(payload()).status_code == 200
    assert post(payload()).status_code == 429


def test_content_length_limit() -> None:
    response = client.post(
        "/v1/budget/check", content=b"x" * 2049, headers={"X-API-Key": TEST_KEY}
    )
    assert response.status_code == 413


def test_chunked_body_limit() -> None:
    response = client.post(
        "/v1/budget/check",
        content=iter([b"x" * 1200, b"y" * 1200]),
        headers={"X-API-Key": TEST_KEY, "Transfer-Encoding": "chunked"},
    )
    assert response.status_code == 413


def test_maximum_body_size_is_parsed_not_rejected() -> None:
    response = client.post(
        "/v1/budget/check", content=b" " * 2048, headers={"X-API-Key": TEST_KEY}
    )
    assert response.status_code == 422


def test_rate_limiter_thread_safe() -> None:
    limiter = security.FixedWindowLimiter(limit=25, window_seconds=60)
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(lambda _: limiter.retry_after(), range(100)))
    assert results.count(None) == 25
    assert results.count(60) == 75




def test_rate_limiter_rejects_invalid_settings() -> None:
    for limit, window in [(0, 60.0), (1, 0.0), (-1, 10.0)]:
        with pytest.raises(ValueError, match="positive"):
            security.FixedWindowLimiter(limit=limit, window_seconds=window)


def test_rate_limiter_resets_on_window_boundary_and_clock_rollback() -> None:
    now = [100.0]
    limiter = security.FixedWindowLimiter(
        limit=1, window_seconds=10.0, clock=lambda: now[0]
    )
    assert limiter.retry_after() is None
    now[0] = 109.1
    assert limiter.retry_after() == 1
    now[0] = 110.0
    assert limiter.retry_after() is None
    assert limiter.retry_after() == 10
    now[0] = 90.0
    assert limiter.retry_after() is None
    assert limiter.retry_after() == 10


def test_structured_metrics_exclude_sensitive_data(caplog: pytest.LogCaptureFixture) -> None:
    import json

    secret_marker = "never-log-this-secret"
    with caplog.at_level("INFO", logger="budget_guard.requests"):
        response = client.post(
            "/v1/budget/check?private=" + secret_marker,
            json=payload(),
            headers={"X-API-Key": TEST_KEY},
        )
    assert response.status_code == 200
    events = [json.loads(record.message) for record in caplog.records
              if record.name == "budget_guard.requests"]
    assert len(events) == 1
    assert events[0]["event"] == "http_request"
    assert events[0]["route"] == "budget_check"
    assert events[0]["status"] == 200
    assert events[0]["duration_ms"] >= 0
    assert set(events[0]) == {"event", "route", "status", "duration_ms"}
    assert secret_marker not in caplog.text
    assert TEST_KEY not in caplog.text


def test_structured_metrics_record_auth_failure_without_key(
    caplog: pytest.LogCaptureFixture,
) -> None:
    import json

    with caplog.at_level("INFO", logger="budget_guard.requests"):
        response = client.post("/v1/budget/check", json=payload())
    assert response.status_code == 401
    events = [json.loads(record.message) for record in caplog.records
              if record.name == "budget_guard.requests"]
    assert len(events) == 1
    assert events[0]["status"] == 401
    assert "X-API-Key" not in caplog.text

def test_rejected_requests_do_not_consume_extra_slots() -> None:
    """A rejected burst must not extend the fixed window or charge extra slots."""
    now = [200.0]
    limiter = security.FixedWindowLimiter(
        limit=1, window_seconds=10.0, clock=lambda: now[0]
    )
    assert limiter.retry_after() is None
    for _ in range(100):
        assert limiter.retry_after() == 10
    now[0] = 209.1
    assert limiter.retry_after() == 1
    now[0] = 210.0
    assert limiter.retry_after() is None
    assert limiter.retry_after() == 10
