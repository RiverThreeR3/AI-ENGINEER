# Track 01 — Python & APIs: AI Request Budget Guard

**Status: In progress (local tests and GitHub Actions CI passed).** This is a deterministic foundation project, not an AI model, provider price feed, or a production-ready spending control.

## Problem and contract

Estimate the maximum **per-request** USD cost of a hypothetical model call using caller-supplied token counts and per-million-token prices. The API returns an exact Decimal calculation and whether the estimate is within a caller-supplied budget. This is useful as a preflight component, but **not** a billing system: actual usage may differ, and the caller controls all values.

- `GET /healthz` returns `{"status":"ok"}`.
- `POST /v1/budget/check` accepts JSON: `input_tokens` and `output_tokens` as strict integers from 0 to 10,000,000; `input_price_usd_per_million` and `output_price_usd_per_million` as decimal **strings** from 0 to 1,000 with at most six fractional digits; `max_cost_usd` as a decimal **string** from 0 to 10,000 with at most six fractional digits.
- Returns `estimated_cost_usd` and `remaining_usd` as exact decimal strings, `within_budget` as boolean, and `pricing_source: caller_supplied`.
- Unknown fields and invalid input return FastAPI/Pydantic HTTP 422; no model calls, external APIs, databases or request-body logging.

## Quickstart

Requires Python 3.12+.

```bash
cd tracks/01-python-apis
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest -q
ruff check .
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Windows PowerShell activation: `.venv\Scripts\Activate.ps1`. Open `http://127.0.0.1:8000/docs` for the generated OpenAPI UI.

```bash
curl -s http://127.0.0.1:8000/v1/budget/check \
  -H 'Content-Type: application/json' \
  -d '{"input_tokens":1000,"output_tokens":500,"input_price_usd_per_million":"2","output_price_usd_per_million":"8","max_cost_usd":"0.01"}'
```

Expected: `{"estimated_cost_usd":"0.006","remaining_usd":"0.004","within_budget":true,"pricing_source":"caller_supplied"}`.

## Container (optional)

```bash
docker build -t ai-budget-guard tracks/01-python-apis
docker run --rm -p 127.0.0.1:8000:8000 ai-budget-guard
```

Container runs as a non-root user. Docker build/run have **not** been independently verified in this delivery.

## Test and evaluation evidence

- Deterministic arithmetic and HTTP contract tests: local pytest execution is recorded in `PROJECTS.md` once run.
- No model evaluation, benchmark, real pricing validation, tokenization accuracy, latency or cost measurement is claimed.
- [GitHub Actions run 41303422258](https://github.com/RiverThreeR3/AI-ENGINEER/actions/runs/41303422258) passed on 2026-11-01 (pytest and Ruff on Python 3.12).

## Security, privacy and limitations

- Do not expose this API publicly without authentication, request-size limits, rate limiting and monitoring at the gateway.
- Caller-supplied prices are **not** authoritative. Token counts must come from a trusted tokenizer or provider; estimates are not spending enforcement.
- No persistence, outbound requests, secrets or PII are required. Avoid submitting sensitive content anyway.
- The base Docker image and GitHub Actions are pinned to version tags, **not immutable digests/SHAs**; pin them before higher-trust deployment.
- There is no live deployment or verified rollback. This project is intentionally a learning foundation.

## Attribution and license

Original example implementation. Uses FastAPI (MIT), Pydantic (MIT), pytest (MIT), HTTPX (BSD-3-Clause), Uvicorn (BSD-3-Clause), and Ruff (MIT). No external code copied. A repository-level license must be selected before redistributing the project under a declared license.

## Next acceptance gate

Confirm CI passes on the PR; add a reproducible latency benchmark and measured gateway protections before claiming portfolio-ready status. Keep this project active until its acceptance criteria pass.
