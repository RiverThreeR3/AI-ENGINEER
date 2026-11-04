# AI Engineer Career Roadmap

This is a **project-first** path for applied AI engineering; phases represent skills and gates, not promises about hiring timelines.

| Phase | Tracks | Hands-on outcome |
| --- | --- | --- |
| Foundations | 01–03 | Python service + ML baseline + PyTorch training |
| GenAI systems | 04–05 | LLM interface with schemas + evaluated RAG |
| Agent engineering | 06–07 | Permissioned tool-use agent + repeatable benchmark |
| Advanced AI | 08 | Compare prompting, retrieval and fine-tuning on one task |
| Production engineering | 09–10 | Deploy, observe, secure and cost-control an AI system |
| Capstone | 11 | Deliver a full customer-oriented application |

## Five pillars from theory to evidence

The [five-pillar evidence map](PILLARS.md) groups the 11 tracks without replacing them:

1. **Software Engineering** — tracks 01–03: Python, APIs, software quality, ML/DL foundations.
2. **LLMs & RAG** — tracks 04–05 and 08: model interfaces, retrieval, adaptation.
3. **Agents & Orchestration** — tracks 06–07: permissioned tool use, orchestration, agent evaluation.
4. **Ops & Evaluation** — tracks 07, 09–10: regression evaluation, deployment, observability, safety and costs.
5. **Signal Projects** — track 11 and finished hands-on cases from other tracks: reproducible portfolio proof.

**Current milestone:** Module 01 has a deterministic FastAPI implementation with 16 passing tests observed locally. CI and Docker verification are pending, so this is not a completed production milestone.

## Learning loop

1. Define user problem, inputs, outputs and success criteria.
2. Build the cheapest deterministic baseline first.
3. Add the AI component only where it brings measured improvement.
4. Test timeouts, invalid responses, malicious inputs and authorization boundaries.
5. Evaluate accuracy, latency, tool correctness, cost and failure rate.
6. Publish run commands, exact environment, measured results and limitations.
7. Ship a reproducible demo; independently verify deployment before claiming it.

## Next concrete work

1. Resolve the open quality/security/observability gaps in [rag-production](https://github.com/raphaelribeirob/rag-production).
2. Make [agent-benchmark](https://github.com/raphaelribeirob/agent-benchmark) executable end-to-end with actual measurements.
3. Verify the [01 Python & APIs](tracks/01-python-apis/README.md) PR in GitHub Actions and Docker, then add measurable edge-case evaluations.
4. Build the [04 LLM Engineering](tracks/04-llm-engineering/README.md) structured-output gateway and compare providers.
5. Publish one capstone only after acceptance criteria pass.

## Status definitions

- **Planned** — requirements documented, no implementation claimed.
- **Scaffold** — initial code or structure, not end-to-end validated.
- **In progress** — important requirements still missing.
- **Verified locally** — reproducible run and test evidence exists.
- **Verified deployed** — a live environment was independently checked.
- **Portfolio-ready** — documentation, quality, safety and evidence gates are satisfied.

Do not confuse third-party labels such as “production-ready” with independent verification.
