# AI Engineer Project Portfolio

**Review date:** 2026-11-01. Statuses below describe *documented evidence*. The Python API test suite was executed locally with Python 3.13.5, FastAPI 0.128.2, Pydantic 2.13.5, pytest 9.0.2 and HTTPX 0.28.1. CI, Docker and deployment have not yet been independently verified.

| Project | Tracks | Status | Next acceptance gate |
| --- | --- | --- | --- |
| [AI Request Budget Guard](tracks/01-python-apis/README.md) | 01 | **In progress — 17/17 local tests passed** | Verify PR CI and Ruff; benchmark and add gateway controls before portfolio-ready |
| [rag-production](https://github.com/raphaelribeirob/rag-production) | 05, 07, 09, 10 | In progress (external reference only) | Fix real-model groundedness gap; add prompt-injection defense, telemetry and tests |
| [agent-benchmark](https://github.com/raphaelribeirob/agent-benchmark) | 06, 07 | Scaffold (external reference only) | Implement task suite and measured comparison with deterministic test runner |
| Classical ML prediction service | 02 | Planned | Dataset baseline + holdout evaluation + reproducible API |
| Deep learning training pipeline | 03 | Planned | Train/evaluate/save/reload a PyTorch model |
| Structured-output LLM gateway | 04 | Planned | Provider interface, schema validation, streaming, retries and usage metrics |
| RAG system comparison | 05, 07 | Planned | Compare sparse/dense/hybrid retrieval with identical evaluation sets |
| Permissioned tool-using agent | 06 | Planned | Enforce tool allowlist, approval policy and auditable action logs |
| Fine-tuning vs alternatives | 08 | Planned | Compare baseline, RAG and fine-tune on fixed test data |
| Production AI service | 09, 10 | Planned | Docker, monitoring, rate limits, rollback, budget and security test |
| AI product capstone | 11 | Planned | End-to-end demo and documented real use case |

## Local evidence — 2026-11-01

- Command: `cd tracks/01-python-apis && python -m pytest -q`
- Result: `17 passed in 0.28s` (Python 3.13.5; local environment only).
- Syntax: `python -m compileall -q app tests` succeeded.
- Ruff was **not** run locally: package unavailable in the offline environment. CI must independently verify it.
- No model inference, provider calls, tokenization, latency/cost benchmarking or external service was exercised.
- No verified CI status, Docker build or deployed endpoint is claimed.

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
