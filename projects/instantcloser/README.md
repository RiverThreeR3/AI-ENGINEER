# InstantCloser — Deterministic Decision Policy Lab

**Status:** Public Python demonstration on `main`. It is **not a deployed agent**, does not call a language model and performs no external actions.

## Problem

An automated assistant must not schedule, quote prices or pursue a conversation solely because a message contains a promising keyword. Consent, explicit opt-out, active objections and untrusted instructions must take priority over an action proposal.

## What is implemented

- [`agent.py`](agent.py): immutable request/decision structures and a pure rule-based `decide()` function. The parser normalizes Unicode, validates the demo tenant identifier and message length, and chooses an action by ordered policy checks.
- [`scenarios.json`](scenarios.json): **11 hand-authored synthetic messages**, including English/Portuguese opt-out, missing consent, booking, pricing, objections, purchase intent, ambiguity and a basic injection-pattern example.
- [`evaluate.py`](evaluate.py): compares expected vs actual actions for the fixtures and reports exact-match agreement, model-review flags and failures.
- [`tests/test_agent.py`](tests/test_agent.py): unit tests for synthetic regression, opt-out priority, missing consent, suspicious instruction patterns and invalid inputs.

### Decision path

```text
Synthetic message and supplied consent context
  -> validate fields and normalize text
  -> opt-out and suspicious-instruction checks
  -> consent and objection checks
  -> intent-specific rule
  -> proposed next action, optional approval/review flag
```

The proposed action is a **data result**. No message, appointment, CRM write, purchase or external tool call is executed.

## How to inspect

From the repository root, with Python 3.11+:

```bash
python -m unittest discover -s projects/instantcloser/tests -v
python -m projects.instantcloser.evaluate
```

These are documented reproduction commands; this documentation audit **did not run them**. The synthetic evaluator is useful for detecting regressions on its authored examples. It does not validate real-world accuracy or LLM performance.

## Security and evaluation limits

- Consent and objections are test inputs, **not verified against an authenticated source**.
- `tenant_id` is a validated string only; **there is no authentication or tenant isolation**.
- Phrase matching for instruction overrides is illustrative and bypassable; **not** a comprehensive prompt-injection defense.
- No independently verified CI result for this component, independent held-out dataset, real-model comparison, latency/cost measurement or deployment is claimed here.

## Next engineering gates

Add independently labeled ambiguous and adversarial cases, record failures by action category, compare against an optional model-assisted baseline, and test permission boundaries before considering any real-world integration.

This public lab contains a standalone demonstration only. It does not expose or claim the implementation state of a separate private application.
