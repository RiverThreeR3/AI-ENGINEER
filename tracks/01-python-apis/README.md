# Module 01 — Python & APIs: Deterministic Triage

**Status:** Implementation available; CI / Docker runtime / independent deployment verification pending. **Not production-ready.**

## Problem and engineering choice
An AI application needs a reliable, testable API before introducing a language model. This small FastAPI service routes incoming support requests using explicit keyword rules, providing a measurable deterministic baseline for later LLM comparisons.

- `GET /healthz` — versioned health response.
- `POST /v1/triage` — validated input and stable response schema.
- `GET /docs` — generated OpenAPI documentation.

**No AI model calls, database, customer records, third-party actions, or billing.** Do not treat keyword routing as real-world accuracy evidence.

## Run locally

Use Python 3.12+:

```bash
cd tracks/01-python-apis
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements-dev.txt
uvicorn service:app --reload
```

Send a test request:

```bash
curl -sS http://localhost:8000/v1/triage \
  -H 'Content-Type: application/json' \
  -d '{"message":"Preciso de reembolso","urgency":"normal"}'
```

Expected response:

```json
{"category":"billing","queue":"billing-desk","needs_human":true,"rule_id":"keyword-v1:billing"}
```

## Tests and checks

```bash
cd tracks/01-python-apis
python -m pytest -q
ruff check .
python -m compileall -q service.py tests
```

CI is defined at `.github/workflows/python-apis.yml` from the repository root. Check GitHub Actions before claiming it passes.

## Run with Docker

```bash
cd tracks/01-python-apis
docker build -t ai-engineer-triage:dev .
docker run --rm -p 8000:8000 ai-engineer-triage:dev
```

Docker build/run has not been independently verified. Container runs as an unprivileged user.

## Decisions and limitations

- Whole-word matching normalizes Portuguese accents and English case. Billing takes precedence when several keywords match. Requests with high urgency or billing topics require human review.
- This is **not** a customer-support classifier validated on customer datasets; no precision, recall, uptime, cost or latency claims are made.
- Missing before production: authentication, authorization, rate limiting, request-size controls at proxy, logging/redaction strategy, telemetry, persistent storage policy, load testing, and human-in-the-loop workflow.
- Do not send real PII to a demo service.

## Acceptance gates

- [x] Versioned FastAPI routes with typed request/response models.
- [x] Explicit deterministic classification logic and error responses.
- [x] Automated API contract, business rule, and input validation tests are committed.
- [ ] GitHub Actions checks green on the PR.
- [ ] Docker image built and smoke-tested.
- [ ] Independently deployed and observed (optional for this learning module).

Next: create a small labeled sample of synthetic messages and compare this baseline to a schema-constrained LLM gateway in module 04, reporting accuracy, cost and latency.
