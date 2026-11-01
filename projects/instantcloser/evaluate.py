"""Deterministic, synthetic policy regression benchmark; not a real-model eval."""
from __future__ import annotations

import json
from pathlib import Path

from .agent import LeadRequest, decide

CASES_PATH = Path(__file__).with_name("scenarios.json")


def run_benchmark() -> dict[str, object]:
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    failures: list[dict[str, str]] = []
    model_reviews = 0
    for case in cases:
        decision = decide(LeadRequest(**case["request"]))
        model_reviews += int(decision.needs_model_review)
        if decision.action != case["expected_action"]:
            failures.append({"id": case["id"], "expected": case["expected_action"], "actual": decision.action})
        if decision.external_action_executed:
            failures.append({"id": case["id"], "expected": "no side effects", "actual": "side effect"})
    return {
        "dataset": "synthetic, hand-authored, not real customer data",
        "cases": len(cases),
        "passed": len(cases) - len({f["id"] for f in failures}),
        "exact_match": (len(cases) - len({f["id"] for f in failures})) / len(cases),
        "model_review_rate": model_reviews / len(cases),
        "failures": failures,
    }


if __name__ == "__main__":
    result = run_benchmark()
    print(json.dumps(result, indent=2, ensure_ascii=False))
    raise SystemExit(1 if result["failures"] else 0)
