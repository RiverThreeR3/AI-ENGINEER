"""A small, typed FastAPI service with no provider calls or persistence."""

from decimal import Decimal
from typing import Annotated

from fastapi import Depends, FastAPI
from pydantic import BaseModel, ConfigDict, Field, StrictInt, field_validator

from app.body_limit import BodyLimitMiddleware
from app.security import require_access

MILLION = Decimal("1000000")
MAX_TOKENS = 10_000_000

app = FastAPI(
    title="AI Request Budget Guard",
    description="Deterministic, caller-priced cost estimates. No model inference.",
    version="0.2.0",
)
app.add_middleware(BodyLimitMiddleware, max_bytes=2048)


class BudgetRequest(BaseModel):
    """Amounts are decimal JSON strings; tokens must be JSON integers."""

    model_config = ConfigDict(extra="forbid")

    input_tokens: StrictInt = Field(ge=0, le=MAX_TOKENS)
    output_tokens: StrictInt = Field(ge=0, le=MAX_TOKENS)
    input_price_usd_per_million: Decimal = Field(
        ge=Decimal("0"), le=Decimal("1000"), decimal_places=6
    )
    output_price_usd_per_million: Decimal = Field(
        ge=Decimal("0"), le=Decimal("1000"), decimal_places=6
    )
    max_cost_usd: Decimal = Field(
        ge=Decimal("0"), le=Decimal("10000"), decimal_places=6
    )

    @field_validator(
        "input_price_usd_per_million",
        "output_price_usd_per_million",
        "max_cost_usd",
        mode="before",
    )
    @classmethod
    def require_decimal_string(cls, value: object) -> str:
        if not isinstance(value, str):
            raise ValueError("USD amounts must be JSON strings, not numbers")
        return value


class BudgetResponse(BaseModel):
    estimated_cost_usd: str
    remaining_usd: str
    within_budget: bool
    pricing_source: str = "caller_supplied"


def usd_text(value: Decimal) -> str:
    """Render a Decimal without scientific notation or binary-float rounding."""
    return format(value, "f")


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/v1/budget/check", response_model=BudgetResponse)
def check_budget(
    request: BudgetRequest,
    _authorized: Annotated[None, Depends(require_access)],
) -> BudgetResponse:
    estimated = (
        request.input_tokens * request.input_price_usd_per_million
        + request.output_tokens * request.output_price_usd_per_million
    ) / MILLION
    remaining = max(Decimal("0"), request.max_cost_usd - estimated)
    return BudgetResponse(
        estimated_cost_usd=usd_text(estimated),
        remaining_usd=usd_text(remaining),
        within_budget=estimated <= request.max_cost_usd,
    )
