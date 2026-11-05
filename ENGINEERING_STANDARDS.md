# Definition of Done — AI Engineer Portfolio

A project can be labeled **portfolio-ready** only when applicable gates below pass.

## Reproducibility and software engineering
- Clear problem, architecture, API contract and quickstart.
- Pinned dependencies, example environment file and no committed secrets.
- Automated unit/integration tests, lint and basic CI.
- Typed and validated inputs/outputs, bounded retries and documented failure handling.

## AI-specific evaluation
- Baseline and held-out evaluation set; datasets and metrics are explained.
- RAG: retrieval quality, groundedness, citations and abstention.
- Agents: task success, tool calls, tool authorization, failure categories, cost and latency.
- Models: provenance, licenses, seeds, splits and confidence/variance where feasible.
- Mock results are always labeled mock. Never substitute them for real-model measurements.

## Security, privacy, reliability
- Least-privilege tool access, correct authorization and (where relevant) tenant isolation.
- Prompt injection and retrieved-content trust boundaries tested.
- Secrets and personal data are not leaked in commits, output or logs.
- Rate limiting, timeouts, budgets and monitoring are designed and measured.
- Deployment/rollback/health checks documented; current production status verified.

## Documentation and attribution
- Follow [the reusable README template](templates/PROJECT_README.md).
- Report genuine status and known gaps.
- Credit upstream repositories and retain required notices/licenses.
- Screenshots and demos must show actual behavior, not only mockups.

## Career practice and portfolio proof gates

The [upstream Career Practice guide](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/learning-paths/CAREER-PRACTICE.md) requires more than a green CI badge. Keep a [project evidence bundle](templates/EVIDENCE_BUNDLE.md) that includes:

- Clearly labeled observed versus assumed workflow, acceptance metric, and manual/deterministic baseline.
- An agent task with explicit scope and boundaries when a coding agent is used; inspect the patch independently.
- A failure case that a meaningful test rejects, then a repair that makes it pass (use disposable fixtures/branches).
- Baseline and candidate quality/latency/cost measured on comparable inputs. Include failed attempts, retries, and review labor assumptions in **cost per accepted user outcome**.
- A feedback signal and second iteration where possible; call simulations or missing user access what they are.
- A decision brief explaining what to keep, change, test or stop.

**Evidence state ladder:** Planned → Open PR → Verified at exact commit SHA → Merged → Independently deployed (if applicable) → Portfolio-ready. None of these labels can be skipped solely due to documentation, upstream tutorial completion or synthetic-only evaluations.

Personal quiz/interview history and professional resumes must remain in verified **private** storage. Never commit these to the public portfolio.
