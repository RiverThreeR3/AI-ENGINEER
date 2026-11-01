"""Contract and boundary tests; no mock model metrics are implied."""

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def payload() -> dict[str, object]:
    return {
        "input_tokens": 1000,
        "output_tokens": 500,
        "input_price_usd_per_million": "2",
        "output_price_usd_per_million": "8",
        "max_cost_usd": "0.01",
    }


def test_healthz() -> None:
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_estimate_and_budget_remaining() -> None:
    response = client.post("/v1/budget/check", json=payload())
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
    response = client.post("/v1/budget/check", json=data)
    assert response.status_code == 200
    assert response.json()["within_budget"] is False
    assert response.json()["remaining_usd"] == "0"


def test_exact_boundary_is_allowed() -> None:
    data = payload()
    data["max_cost_usd"] = "0.006"
    response = client.post("/v1/budget/check", json=data)
    assert response.json()["within_budget"] is True
    assert response.json()["remaining_usd"] == "0"


def test_zero_cost_and_zero_budget() -> None:
    data = payload()
    data.update(input_tokens=0, output_tokens=0, max_cost_usd="0")
    response = client.post("/v1/budget/check", json=data)
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
    assert client.post("/v1/budget/check", json=data).status_code == 422


def test_unknown_fields_rejected() -> None:
    data = payload()
    data["api_key"] = "do-not-accept-extra-fields"
    assert client.post("/v1/budget/check", json=data).status_code == 422


def test_openapi_documents_contract() -> None:
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert "/v1/budget/check" in response.json()["paths"]
