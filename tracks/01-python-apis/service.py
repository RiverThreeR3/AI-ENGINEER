"""Deterministic customer-request triage API (no model calls or side effects)."""

from enum import StrEnum
import re
import unicodedata
from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field


class Category(StrEnum):
    BILLING = "billing"
    SUPPORT = "support"
    SALES = "sales"
    OTHER = "other"


class TriageRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    message: str = Field(min_length=1, max_length=2000)
    urgency: Literal["normal", "high"] = "normal"


class TriageResponse(BaseModel):
    category: Category
    queue: str
    needs_human: bool
    rule_id: str


# The ordering is intentional: billing issues take precedence over support/sales.
_RULES: tuple[tuple[Category, frozenset[str]], ...] = (
    (Category.BILLING, frozenset({
        "refund", "invoice", "billing", "payment", "reembolso",
        "fatura", "cobranca", "pagamento", "cancelamento",
    })),
    (Category.SUPPORT, frozenset({
        "bug", "error", "broken", "issue", "erro", "falha", "problema",
        "suporte", "ajuda",
    })),
    (Category.SALES, frozenset({
        "demo", "pricing", "quote", "buy", "preco", "orcamento",
        "comprar", "vendas",
    })),
)


def _tokens(text: str) -> set[str]:
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return set(re.findall(r"[a-z0-9]+", ascii_text.lower()))


def classify(request: TriageRequest) -> TriageResponse:
    """Apply transparent, auditable routing rules without taking actions."""
    words = _tokens(request.message)
    category = next(
        (category for category, terms in _RULES if words & terms), Category.OTHER
    )
    needs_human = request.urgency == "high" or category == Category.BILLING
    return TriageResponse(
        category=category,
        queue=f"{category.value}-desk" if category != Category.OTHER else "general-desk",
        needs_human=needs_human,
        rule_id=f"keyword-v1:{category.value}",
    )


app = FastAPI(
    title="AI Engineer — Deterministic Triage Baseline",
    version="0.1.0",
    description="Educational API; no AI inference, persistence, or external actions.",
)


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok", "version": "0.1.0"}


@app.post("/v1/triage", response_model=TriageResponse)
def triage(request: TriageRequest) -> TriageResponse:
    return classify(request)
