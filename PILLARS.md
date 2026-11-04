# Five pillars of AI Engineering

This is a **portfolio evidence map**, not a substitute for the 11 detailed hands-on tracks. A topic being listed does not imply mastery or a completed implementation.

| Pillar | Connected tracks | Required portfolio evidence | Current state |
| --- | --- | --- | --- |
| 1. Software Engineering | 01 Python & APIs; 02 Machine Learning; 03 Deep Learning | Typed service, unit/integration tests, CI, reproducible environment | Module 01 API implemented on this branch; 16 tests passed locally; CI/Docker pending. Tracks 02–03 planned. |
| 2. LLMs & RAG | 04 LLM Engineering; 05 RAG & Search; 08 Model Adaptation | Structured responses, retrieval metrics, hallucination controls, model comparison | RAG external work in progress; others planned. |
| 3. Agents & Orchestration | 06 AI Agents & MCP; 07 Evaluations | Permissioned tools, approval gates, executable agent benchmark | External agent benchmark scaffold; broader tests planned. |
| 4. Ops & Evaluation | 07 Evaluations; 09 MLOps & Deployment; 10 Security & System Design | CI, reproducible evals, observability, budget/latency, threat model | Standards documented; most implementation planned. |
| 5. Signal Projects | 11 Capstone Products plus practical cases from the other tracks | One or more end-to-end demos with measurable results, documented trade-offs and a truthful status | InstantCloser public policy lab exists; full real-world validation pending. |

A track can support more than one pillar. The status labels come from the linked track and project documentation.

## Delivery order and evidence gates

1. **Module 01** — reproducible Python/FastAPI baseline, tests and Docker smoke test.
2. **Module 04** — LLM gateway with validated output, retries, provider errors and per-request token/cost reporting. Compare to module 01's deterministic baseline.
3. **Module 05** — repair and evaluate existing `rag-production`; publish retrieval and grounded-answer metrics.
4. **Modules 06–07** — complete `agent-benchmark` with permissioned tools and real measured runs.
5. **Modules 09–10** — security, observability, deployment and incident/rollback procedures.
6. **Module 11** — a capstone that runs end-to-end and passes the standards.
7. **Modules 02, 03 and 08** — complete the classical ML, deep learning and model adaptation evidence as dedicated, reproducible projects.

## Definition of evidence

- **Planned:** requirements only.
- **Implementation:** source code exists, but end-to-end verification may be missing.
- **Locally tested:** command and result were observed locally; environment and limitations recorded.
- **CI verified:** published automated checks have passed for the relevant commit.
- **Deployed verified:** reachable live environment was independently tested.
- **Portfolio-ready:** independent reproduction, metrics, tests, security review and truthful limitations meet `ENGINEERING_STANDARDS.md`.

Do not treat a lesson, a folder or 16 passing synthetic test cases as proof of professional or production competence.

## Interview deliverables

For every project, document: problem, architecture diagram, trade-offs, failure cases, evaluation design, cost/latency, controls, reproducible setup and a two-minute English explanation. The best capstone demonstrates an engineering decision with a measured baseline rather than only an attractive demo.
