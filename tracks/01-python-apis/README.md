# Track 01 — Python & APIs: AI Request Budget Guard

**Status: In progress.** Local tests and 2026-11-02 GitHub Actions pytest, Ruff and Docker smoke checks passed. A 2026-11-03 loopback TCP HTTP benchmark was measured locally and passed in [GitHub Actions run 41625097153](https://github.com/RiverThreeR3/AIEngineer/actions/runs/41625097153); no external deployment is verified. This is a deterministic foundation project, not a production spending control.

## Problem and contract

Estimate the maximum **per-request** USD cost of a hypothetical model call using caller-supplied token counts and per-million-token prices. The API returns an exact Decimal calculation and whether the estimate is within a caller-supplied budget. This is useful as a preflight component, but **not** a billing system: actual usage may differ, and the caller controls all values.

- `GET /healthz` returns `{"status":"ok"}`.
- `POST /v1/budget/check` requires the `X-API-Key` header, configured using `BUDGET_GUARD_API_KEY` (at least 16 characters). It accepts JSON: `input_tokens` and `output_tokens` as strict integers from 0 to 10,000,000; `input_price_usd_per_million` and `output_price_usd_per_million` as decimal **strings** from 0 to 1,000 with at most six fractional digits; `max_cost_usd` as a decimal **string** from 0 to 10,000 with at most six fractional digits.
- Returns `estimated_cost_usd` and `remaining_usd` as exact decimal strings, `within_budget` as boolean, and `pricing_source: caller_supplied`.
- Unknown fields and invalid input return 422. Missing/wrong API keys return 401/403; missing server key returns 503 (fail closed).
- The budget endpoint rejects bodies over 2,048 bytes (413), including chunked bodies, before JSON parsing.
- A thread-safe, process-local fixed-window limiter allows 60 authenticated requests per 60 seconds. Excess requests return 429 with `Retry-After`. No model calls, external APIs, databases or request-body logging.

## Quickstart

Requires Python 3.12+.

```bash
cd tracks/01-python-apis
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
export BUDGET_GUARD_API_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(32))')"
python -m pytest -q
ruff check .
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Windows PowerShell activation: `.venv\Scripts\Activate.ps1`. Set `$env:BUDGET_GUARD_API_KEY` to a random secret. `.env.example` shows the variable name, not a safe real key. Open `http://127.0.0.1:8000/docs` for the generated OpenAPI UI.

```bash
curl -s http://127.0.0.1:8000/v1/budget/check \
  -H "X-API-Key: $BUDGET_GUARD_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"input_tokens":1000,"output_tokens":500,"input_price_usd_per_million":"2","output_price_usd_per_million":"8","max_cost_usd":"0.01"}'
```

Expected: `{"estimated_cost_usd":"0.006","remaining_usd":"0.004","within_budget":true,"pricing_source":"caller_supplied"}`.

## Container (optional)

```bash
docker build -t ai-budget-guard tracks/01-python-apis
docker run --rm -p 127.0.0.1:8000:8000 \
  -e BUDGET_GUARD_API_KEY="$BUDGET_GUARD_API_KEY" ai-budget-guard
```

Container runs as a non-root user. Docker was unavailable locally on 2026-11-02; the GitHub Actions Docker build and live-container HTTP smoke check **passed** in [run 41440781850](https://github.com/RiverThreeR3/AIEngineer/actions/runs/41440781850). This is a CI container check, not a deployed production endpoint.

## Test and evaluation evidence

- Local 2026-11-02: `python -m pytest -q` — **27 passed in 0.35s** (Python 3.13.5). `python -m compileall -q app tests scripts` — passed. Ruff unavailable locally; CI must verify lint.
- Local 2026-11-02: `python -m scripts.benchmark_local --iterations 200 --warmup 20` — in-process TestClient p50 **1.035 ms**, p95 **1.682 ms**, p99 **2.399 ms** (one environment/run; **not network or production latency**). The benchmark raises the local rate cap to isolate processing.
- [GitHub Actions run 41440781850](https://github.com/RiverThreeR3/AIEngineer/actions/runs/41440781850) passed on 2026-11-02 (Python 3.12.15: **27 passed, 1 dependency deprecation warning in 0.57s**; Ruff passed; Docker build and live-container HTTP smoke passed).
- CI in-process TestClient benchmark (100 iterations, 10 warmup): p50 **1.120 ms**, p95 **1.634 ms**, p99 **2.094 ms**. This is not a network or production benchmark.
- Local 2026-11-03: `python -m scripts.benchmark_http --iterations 40 --warmup 5` — **40 measured sequential HTTP requests over loopback TCP** to a temporary Uvicorn process, Python 3.13.5; p50 **2.252 ms**, p95 **3.783 ms**, p99 **4.813 ms**. Fresh TCP connection per request; no concurrency, remote deployment or real provider. Timing varies by host; this is not production latency or throughput. The script generates an ephemeral key, binds only to 127.0.0.1, respects the default 60-request rate cap and cleans up its child process. Ten additional pure validation tests passed locally.
- [GitHub Actions run 41625097153](https://github.com/RiverThreeR3/AIEngineer/actions/runs/41625097153) passed on 2026-11-03: pytest (including 10 new validation tests), Ruff, in-process benchmark, loopback TCP HTTP benchmark, Docker build and live-container HTTP smoke. CI job success does not validate production latency.
- No model evaluation, provider calls, tokenizer accuracy, real pricing, deployment or production cost measurement is claimed.

## Security, privacy and limitations

- Single-key demonstration only. The fixed-window limiter is **per process** and resets on restart; replicas do not share a quota. For production, use HTTPS, per-tenant authentication, a distributed gateway limiter, monitoring, centralized secrets and ingress controls.
- Invalid API keys are not rate-limited in-process; network-layer abuse protection is required. The 2,048-byte middleware applies only to the budget route; other paths need ingress limits.
- Caller-supplied prices and token counts are **not authoritative**. Actual token usage and provider charges are not controlled by this estimator.
- No persistence, outbound requests, PII or secret/body logging is required. Never commit a real key or log the header at a proxy.
- The Docker base image and Actions are pinned to tags, not immutable digests/SHAs. No verified deployment or rollback exists.

## Attribution and license

Original example implementation. Uses FastAPI (MIT), Pydantic (MIT), Starlette (BSD-3-Clause), pytest (MIT), HTTPX (BSD-3-Clause), Uvicorn (BSD-3-Clause), and Ruff (MIT). No external code copied. A repository-level license must be selected before redistributing the project under a declared license.

## Next acceptance gate

CI and Docker smoke checks passed on 2026-11-02 and 2026-11-03. The new loopback TCP HTTP benchmark passed in CI on 2026-11-03. Next measure deployed network latency/throughput and implement distributed rate limits, production authentication, deployment and rollback. Keep Track 01 active until the acceptance gates pass.
