# Recruiter Guide — Raphael Ribeiro | Applied AI Engineering

This is the **public evidence hub** for reviewing original engineering work, not a list of completed course certificates. The focus is reliable Python APIs, LLM product engineering, tool-use safety, RAG, evaluation, and operations. Claims are deliberately limited to what a reviewer can inspect.

## Start here

1. [Portfolio home](../README.md): what is available and its current status.
2. [Project evidence index](../PROJECTS.md): committed code, in-review changes, acceptance gates and explicit limitations.
3. [Engineering standards](../ENGINEERING_STANDARDS.md): what is required before calling work portfolio-ready.
4. [Course-to-practice map](COURSE_MAPPING.md): how the official AI Engineering From Scratch curriculum supports the original portfolio.
5. [Public commercial case destination](https://github.com/RiverThreeR3/AGESOMA-PROJECTS): separate authorized public cases; verify individual examples instead of assuming the whole agency codebase is complete.

## Current project proof

The combined workflow's **single active engineering flagship** is [AGESOMA Knowledge API PR #2](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/2), in the separate authorized commercial evidence repository. Review its current SHA, tests and limitations before attributing any contribution to Raphael. The Budget Guard PR below is **audit/maintenance only**, not a second active feature build.

| Project / access | Engineering skills a reviewer can inspect | Evidence and honest limitations | Interview deep-dive |
| --- | --- | --- | --- |
| [AI Request Budget Guard — PR #1](https://github.com/RiverThreeR3/AIEngineer/pull/1) (open PR; **not merged or deployed**) | Python, FastAPI request contracts, deterministic budget estimation, API guard and tests, bounded errors and observability in proposed code | Review current PR head and CI for **that exact SHA**. Synthetic input costs and local tests do not prove actual provider billing or live service reliability. | How would you calculate cost per successful LLM task and prevent rate-limit bypass across multiple instances? |
| [InstantCloser policy lab](../projects/instantcloser/README.md) (merged public demo) | Deterministic decision policy, consent/opt-out guards, prompt-injection handling examples, and reproducible regression fixtures | Demo with 11 hand-authored synthetic scenarios. No real-model accuracy, customer conversion, tenant security or production integration claim. | What is the trust boundary between a model's proposed action and an authorized external tool call? |
| [RAG Production](https://github.com/raphaelribeirob/rag-production) (separate public WIP) | Retrieval architecture and evaluation design, subject to current independent repository review | Groundedness/faithfulness gap has been documented; this is **not** a certified deployed or finished portfolio project. | How would you build a hold-out retrieval evaluation and block unsupported answers? |
| [Agent Benchmark](https://github.com/raphaelribeirob/agent-benchmark) (separate public scaffold) | Early benchmarking structure only | No end-to-end benchmark or measured agent performance is claimed. | What distinguishes a deterministic agent regression test from a real evaluation of task success? |

**Verification method:** Open the linked source/PR, identify its exact commit, reproduce documented commands, inspect test output and failure cases, read the limitations, and distinguish a local demo from a deployed system. A successful older CI run must not be attributed to a newer commit. Public accessibility should be tested without an authenticated account before sending an application where feasible.

## Skill-to-proof reconciliation

The [official Applied AI Engineer route](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/learning-paths/applied-ai-engineer.json) expects structured outputs, grounded tool/retrieval use, evaluations/guardrails, quality-latency-cost accounting, and reasoned deployment/rollback controls.

| Career skill | Current evidence location | What is still required before a strong CV claim |
| --- | --- | --- |
| Python API engineering | Budget Guard PR #1 | Merge/review status, exact-SHA test evidence and clear demonstration scope |
| Deterministic safety and human approval | InstantCloser public lab | Broader independent cases, adversarial testing, real authorization before any external actions |
| LLM reliability, JSON schemas, RAG | RAG external WIP; local LLM track still planned | Working original LLM flow, grounded evaluation and bounded failures |
| Agents and evaluations | Agent Benchmark scaffold; InstantCloser synthetic fixtures | Executable held-out benchmark, tool-permission failures, measurable quality/latency/cost |
| Production operations and deployment | General engineering standards; project-specific work in progress | Independently verified deployment, meaningful monitoring, data boundaries and rollback evidence |

Never mark a skill complete merely because its upstream course lesson is listed or a project scaffold exists.

## The interview connection

This public guide identifies **technical topics** suitable for discussion; personal mock interview answers, scores, full study notes, job applications, and coaching history remain **private**. Scheduled lessons and interview preparation are **expository reading materials** in Brazilian Portuguese, with authentic English prompts and original English model answers, referencing the [official course](https://github.com/rohitg00/ai-engineering-from-scratch) and [bank](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/interviews). This is not the interactive upstream skills assessment, and it produces no learner score or competence claim. Only verified project improvements and defensible technical explanations are promoted to this public evidence hub.

For each demonstrated capability, the internal process connects:
**official lesson presented (reading only) → optional independently observed learner demonstration (private) → attributable original GitHub change → exact-SHA tests and evaluation → CV-safe bullet in the private master resume → interview explanation and trade-offs.**

## Resume and identity boundaries

The canonical professional resume is kept in a **private** Google Drive folder and may be shared or attached by Raphael to a specific recruiter. The public repository never exposes personal contact details, the private Drive URL, lesson grades or a claim of automatic LinkedIn synchronization.

A professional resume or recruiter outreach can refer to this verified public portfolio. **No automatic resume sharing, job application, LinkedIn edit or recruiter contact is implied by this documentation.**

## Next acceptance gate

Prioritize verification and reviewable progress on the separately hosted [Knowledge API PR #2](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/2); keep Budget Guard PR #1 in the audit queue for exact-SHA CI, security and conflict review. **Never auto-merge** either PR. Link commercial evidence here only with correct status and verified attribution.
