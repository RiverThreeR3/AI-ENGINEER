# AI Engineer Project Portfolio

**Review date:** 2026-11-02. Evidence is local unless otherwise labeled. Previous CI passed 2026-11-01; updated CI and Docker smoke checks are pending verification.

| Project | Tracks | Status | Next acceptance gate |
| --- | --- | --- | --- |
| [AI Request Budget Guard](tracks/01-python-apis/README.md) | 01 | **In progress — 27/27 local tests passed; new CI pending** | Verify CI/Docker, then network benchmarks and production gateway controls |
| [rag-production](https://github.com/raphaelribeirob/rag-production) | 05, 07, 09, 10 | In progress (external reference only) | Fix real-model groundedness gap; add prompt-injection defense, telemetry and tests |
| [agent-benchmark](https://github.com/raphaelribeirob/agent-benchmark) | 06, 07 | Scaffold (external reference only) | Implement task suite and measured comparison with deterministic test runner |
| [InstantCloser public policy lab](projects/instantcloser/README.md) | 01, 06, 07, 10, 11 | Demo implementation; no real-model/production validation | Independent evals, authorized tool simulation, cost/latency measurements |
| Classical ML prediction service | 02 | Planned | Dataset baseline + holdout evaluation + reproducible API |
| Deep learning training pipeline | 03 | Planned | Train/evaluate/save/reload a PyTorch model |
| Structured-output LLM gateway | 04 | Planned | Provider interface, schema validation, streaming, retries and usage metrics |
| RAG system comparison | 05, 07 | Planned | Compare sparse/dense/hybrid retrieval with identical evaluation sets |
| Permissioned tool-using agent | 06 | Planned | Enforce tool allowlist, approval policy and auditable action logs |
| Fine-tuning vs alternatives | 08 | Planned | Compare baseline, RAG and fine-tune on fixed test data |
| Production AI service | 09, 10 | Planned | Docker, monitoring, rate limits, rollback, budget and security test |
| AI product capstone | 11 | Planned | End-to-end demo and documented real use case |

## Track 01 evidence — 2026-11-02

- Local `cd tracks/01-python-apis && python -m pytest -q`: **27 passed in 0.35s** (Python 3.13.5; FastAPI 0.128.2, Pydantic 2.13.5, pytest 9.0.2, HTTPX 0.28.1).
- Local `python -m compileall -q app tests scripts`: passed. Ruff unavailable locally; CI must verify it.
- Added tests: fail-closed API key, 401/403, 413 on oversized/chunked bodies, fixed-window 429 and thread safety.
- Local `python -m scripts.benchmark_local --iterations 200 --warmup 20`: in-process TestClient p50 **1.035 ms**, p95 **1.682 ms**, p99 **2.399 ms**. Single run; not network latency or production throughput.
- [Previous CI run 41303475616](https://github.com/RiverThreeR3/AIEngineer/actions/runs/41303475616) passed 2026-11-01 with 17 tests and Ruff, **before** this update.
- Updated CI includes Docker build and HTTP smoke. **Not yet verified.** Local Docker unavailable; no deployment or rollback verification.
- No real model, provider, tokenizer, billing, external service or production cost measurement.

## Evidence checklist per project

- Permanent commit SHA and exact installation/run commands
- Dataset provenance, holdout set and baseline (when relevant)
- Tests and CI result (with timestamp)
- Measured evaluation and failure cases
- Latency, token usage, cost or resource use
- Threat model and secrets/PII practices
- Demo or independently verified deployment, explicitly labeled
- Documented limitations and license

**Do not mark planned projects as complete because an upstream tutorial exists.**
