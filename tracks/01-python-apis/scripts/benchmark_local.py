"""Measure in-process TestClient request latency; NOT a network or model benchmark."""

import argparse
import json
import math
import os
import secrets
import sys
from statistics import median
from time import perf_counter_ns

from fastapi.testclient import TestClient

from app import security
from app.main import app

PAYLOAD = {
    "input_tokens": 1000,
    "output_tokens": 500,
    "input_price_usd_per_million": "2",
    "output_price_usd_per_million": "8",
    "max_cost_usd": "0.01",
}


def percentile(values: list[float], fraction: float) -> float:
    ordered = sorted(values)
    return ordered[max(0, math.ceil(len(ordered) * fraction) - 1)]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--iterations", type=int, default=200)
    parser.add_argument("--warmup", type=int, default=20)
    args = parser.parse_args()
    if not 1 <= args.iterations <= 100_000 or not 0 <= args.warmup <= 10_000:
        parser.error("iterations must be 1..100000; warmup must be 0..10000")

    key = os.environ.get("BUDGET_GUARD_API_KEY")
    if not key:
        key = secrets.token_urlsafe(32)
        os.environ["BUDGET_GUARD_API_KEY"] = key
    if len(key) < 16:
        parser.error("BUDGET_GUARD_API_KEY must have at least 16 characters")
    security.limiter = security.FixedWindowLimiter(limit=args.iterations + args.warmup + 1)
    timings_ms: list[float] = []
    with TestClient(app) as client:
        for index in range(args.iterations + args.warmup):
            start = perf_counter_ns()
            response = client.post(
                "/v1/budget/check", json=PAYLOAD, headers={"X-API-Key": key}
            )
            elapsed_ms = (perf_counter_ns() - start) / 1_000_000
            if response.status_code != 200:
                raise RuntimeError(f"Unexpected HTTP status {response.status_code}")
            if index >= args.warmup:
                timings_ms.append(elapsed_ms)
    print(
        json.dumps(
            {
                "benchmark": "in_process_testclient_only",
                "python": sys.version.split()[0],
                "iterations": args.iterations,
                "warmup": args.warmup,
                "p50_ms": round(median(timings_ms), 3),
                "p95_ms": round(percentile(timings_ms, 0.95), 3),
                "p99_ms": round(percentile(timings_ms, 0.99), 3),
                "min_ms": round(min(timings_ms), 3),
                "max_ms": round(max(timings_ms), 3),
                "limitations": "no network, no real AI, rate cap raised for isolated timing",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
