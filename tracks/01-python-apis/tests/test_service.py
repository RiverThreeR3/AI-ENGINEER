"""API contract and deterministic decision-policy tests."""

import pytest
from fastapi.testclient import TestClient

from service import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": "0.1.0"}


@pytest.mark.parametrize(
    ("message", "category", "queue", "needs_human"),
    [
        ("Please refund my payment", "billing", "billing-desk", True),
        ("Cobrança errada na fatura", "billing", "billing-desk", True),
        ("Apareceu um erro", "support", "support-desk", False),
        ("Quero um orçamento", "sales", "sales-desk", False),
        ("Bom dia, tudo bem?", "other", "general-desk", False),
    ],
)
def test_triage_categories(
    message: str, category: str, queue: str, needs_human: bool
) -> None:
    response = client.post("/v1/triage", json={"message": message})
    assert response.status_code == 200
    body = response.json()
    assert body == {
        "category": category,
        "queue": queue,
        "needs_human": needs_human,
        "rule_id": f"keyword-v1:{category}",
    }


def test_high_urgency_requires_human() -> None:
    response = client.post(
        "/v1/triage", json={"message": "I need a demo", "urgency": "high"}
    )
    assert response.status_code == 200
    assert response.json()["needs_human"] is True


def test_priority_of_billing_rule_when_multiple_categories_match() -> None:
    response = client.post("/v1/triage", json={"message": "refund bug demo"})
    assert response.json()["category"] == "billing"


def test_word_boundaries_prevent_false_positives() -> None:
    response = client.post("/v1/triage", json={"message": "debugger"})
    assert response.json()["category"] == "other"


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"message": ""},
        {"message": "   "},
        {"message": "x" * 2001},
        {"message": "demo", "urgency": "urgent"},
        {"message": "demo", "admin": True},
    ],
)
def test_rejects_invalid_inputs(payload: dict[str, object]) -> None:
    response = client.post("/v1/triage", json=payload)
    assert response.status_code == 422
    assert "detail" in response.json()


def test_openapi_contract() -> None:
    result = client.get("/openapi.json")
    assert result.status_code == 200
    assert "/v1/triage" in result.json()["paths"]
