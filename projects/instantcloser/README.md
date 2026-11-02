# InstantCloser — Deterministic-first Sales Agent Lab

**Portfolio status:** Public, independently authored teaching/demo implementation. **Not** the production InstantCloser app; no deployment or real-model benchmark has been verified. Original product: `raphaelribeirob/InstantCloser` (**private**, remains separate).

## Problem and intended user
Sales agents need to identify customer intent, follow permission rules, avoid premature closes, and propose the smallest safe next step. The engineering challenge is to make the core policy deterministic and measurable rather than having a language model unilaterally send messages, book meetings, or declare revenue.

## Public deliverable
- `agent.py`: side-effect-free policy engine (Portuguese/English phrase patterns) with explicit consent, opt-out, objection and prompt-injection guards.
- `scenarios.json`: **11 hand-authored synthetic examples**, not real customers and not a held-out production dataset.
- `evaluate.py`: exact-match action accuracy and model-review escalation rate on those fixtures.
- `tests/test_agent.py`: regression tests for consent, opt-out, approval requirements, injection and basic input validation.
- CI: dedicated GitHub Actions workflow running those checks.

## Architecture (demo only)

```text
Synthetic buyer message + demo context
          |
          v
     Input validation
          |
          v
  Opt-out / injection / consent guard
          |
          v
   Objection + intent rules
          |
          v
 Proposed next action + human-approval flag
          |
          +----> Semantic-review flag on unrecognized intent
```

**No messages, bookings, purchases, database writes, model calls or outbound tool executions occur.** A proposed slot is not a confirmed appointment; a purchase intent is not a sale.

## Production architecture represented (not copied)
The separate private InstantCloser repository documents a FastAPI/SQLAlchemy backend, PostgreSQL/Neon, Flutter, Meta WhatsApp Cloud API, billing, voice, sales-policy logic and first-party revenue attribution. This public lab isolates **one teaching concern**: evaluating a sales decision policy. It does **not** expose or mirror proprietary production source.

## Run locally
Requires Python 3.11+ and the repository root as working directory; no API keys or dependencies.

```bash
python -m unittest discover -s projects/instantcloser/tests -v
python -m projects.instantcloser.evaluate
```

The benchmark prints `cases`, `passed`, `exact_match`, `model_review_rate` and per-scenario failures. A high score on 11 authored scenarios proves only regression consistency on those scenarios; it does **not** establish conversion uplift, production accuracy, general language coverage or LLM quality.

## AI engineering evaluation plan
1. Add diverse, independently labeled hold-out cases including multilingual negation, mixed intents, injection, refund and cancellation.
2. Establish a rule-only baseline, optional structured-output model fallback, and calibrated escalation thresholds.
3. Measure safety violation rate, precision by action, human-review rate, latency, token usage, cost and changes across releases.
4. Add fault-injected provider simulations and permissioned tool calls; verify provider acknowledgment before marking real-world outcomes.
5. Evaluate tenant isolation and authorization using **server-authenticated** identity, not `tenant_id` supplied by a caller.

## Security, privacy and limitations
- All example data is synthetic; no personal data or credentials are required.
- `tenant_id` is only a validated demo identifier; **there is no authentication or multi-tenant security implementation**.
- `consent_to_contact` and `active_objection` are supplied as test context, not backed by a trusted database.
- Injection phrase matching is illustrative and trivially bypassable; it is **not a complete prompt-injection defense**.
- No verified live integration, deployment, real customer ROI, or production security review is claimed.

## Attribution and license
The public lab is a new educational implementation associated with the author's own private InstantCloser product. No private source code, secrets, customer data, or third-party datasets were copied into this folder. Licensing of the private application is not inferred from this public exercise.

## Acceptance gates
- [x] Runnable no-dependency local regression suite and synthetic evaluator committed
- [x] Explicit action permissions and side-effect-free output in the demo
- [ ] CI result independently observed
- [ ] Broader held-out and adversarial data
- [ ] Real-model versus deterministic baseline comparison
- [ ] End-to-end authorized integration and provider receipt checks
- [ ] Live deployment, costs, latency, security assessment and measured ROI
