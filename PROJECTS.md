# AI Engineer Project Portfolio

**Review date:** 2026-11-01. Statuses below describe *documented evidence*; no CI run or deployment was performed as part of organizing this hub.

| Project | Tracks | Status | Next acceptance gate |
| --- | --- | --- | --- |
| [rag-production](https://github.com/raphaelribeirob/rag-production) | 05, 07, 09, 10 | In progress | Fix real-model groundedness gap; add prompt-injection defense, telemetry and tests |
| [agent-benchmark](https://github.com/raphaelribeirob/agent-benchmark) | 06, 07 | Scaffold | Implement task suite and measured comparison with deterministic test runner |
| [InstantCloser public policy lab](projects/instantcloser/README.md) | 01, 06, 07, 10, 11 | Demo implementation; no real-model/production validation | Run CI; add independent held-out evals, authorized tool simulation, cost and latency measurements |
| Python API foundations | 01 | Planned | Typed endpoints + pytest + lint + CI |
| Classical ML prediction service | 02 | Planned | Dataset baseline + holdout evaluation + reproducible API |
| Deep learning training pipeline | 03 | Planned | Train/evaluate/save/reload a PyTorch model |
| Structured-output LLM gateway | 04 | Planned | Provider interface, schema validation, streaming, retries and usage metrics |
| RAG system comparison | 05, 07 | Planned | Compare sparse/dense/hybrid retrieval with identical evaluation sets |
| Permissioned tool-using agent | 06 | Planned | Enforce tool allowlist, approval policy and auditable action logs |
| Fine-tuning vs alternatives | 08 | Planned | Compare baseline, RAG and fine-tune on fixed test data |
| Production AI service | 09, 10 | Planned | Docker, monitoring, rate limits, rollback, budget and security test |
| AI product capstone | 11 | Planned | End-to-end demo and documented real use case |

## Active project and upstream mapping

**Portfolio cadence:** one active project, one independently checkable weekly milestone when feasible, and one bounded implementation stage per BUILD session. These are our operating targets; the upstream curriculum prescribes **one stage per tutor session** and **does not set a projects-per-week quota**. Keep the active project through multiple weeks if needed. Project selection remains grounded in current client-market requirements.

| Priority | Raphael project / actual status | Closest upstream learning or practical reference | Next verified evidence |
| --- | --- | --- | --- |
| Active | [AI Request Budget Guard — Track 01 PR #1](https://github.com/RiverThreeR3/AIEngineer/pull/1), in review; not a deployed or completed portfolio item | [LLM cost optimization](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/11-caching-cost/docs/en.md) and [FinOps for LLMs](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/27-finops-llms/docs/en.md); related course project [Token Counter and Cost Meter](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/projects/token-counter-and-cost-meter) **is not identical** to this API | Validate CI against the latest PR SHA, security and rate-limit boundaries, truthful cost assumptions, and release readiness before completion |
| Next candidate, existing WIP | [rag-production](https://github.com/raphaelribeirob/rag-production) | [Retrieval Evaluation Lab](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/projects/retrieval-evaluation-lab) | Measured retrieval and answer-quality failures, corrected evaluation and regression evidence |
| Next candidate, scaffold | [agent-benchmark](https://github.com/raphaelribeirob/agent-benchmark) | [Agent Trace Debugger](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/projects/agent-trace-debugger) | Executable task suite, trace evidence, tests and meaningful measurements |

These are **learning references**, not proof the upstream exercises are installed, completed, or reused in Raphael's projects. Do not work on unrelated legacy repositories solely because they appear as links here; follow the existing authorized-repository rules for any actual write.

## Project proof and reporting

Each original project should map to the verified upstream curriculum (see [20-phase crosswalk](docs/COURSE_MAPPING.md)), using the official [Applied AI Engineer career route](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/learning-paths/applied-ai-engineer.json) for readiness targets. Use [the evidence bundle](templates/EVIDENCE_BUNDLE.md) to track real inputs, negative cases, CI at an exact SHA, run environment, independently measured metrics, security boundaries, limitations and next acceptance gate.

The official `build-project` tutor advances **one learning stage per session**, not one new project every week. This portfolio keeps one current flagship project until it is independently ready or a justified stop/pivot is documented. Course examples, local course certificates and automated code generation are **not** professional experience by themselves.

## Evidence checklist per project

- Permanent commit SHA and exact installation/run commands
- Dataset provenance, holdout set and baseline
- Tests and CI result (with timestamp)
- Measured evaluation and failure cases
- Latency, token usage, cost or resource use
- Threat model and secrets/PII practices
- Demo or independently verified deployment, explicitly labeled
- Documented limitations and license

**Do not mark planned projects as complete because an upstream tutorial exists.**
