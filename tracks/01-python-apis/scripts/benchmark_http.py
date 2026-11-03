"""Measure sequential HTTP-over-loopback latency against a temporary Uvicorn server.

This is NOT a deployed-service, load, throughput, or model-inference benchmark.
"""

import argparse
import json
import math
import os
import secrets
import socket
import subprocess
import sys
import time
from pathlib import Path
from statistics import median
from time import perf_counter_ns
from urllib.error import HTTPError, URLError
from urllib.request import ProxyHandler, Request, build_opener

PAYLOAD = json.dumps(
    {
        "input_tokens": 1000,
        "output_tokens": 500,
        "input_price_usd_per_million": "2",
        "output_price_usd_per_million": "8",
        "max_cost_usd": "0.01",
    }
).encode("utf-8")


def percentile(values: list[float], fraction: float) -> float:
    """Nearest-rank percentile; requires a nonempty sample and fraction in (0, 1]."""
    if not values or not 0 < fraction <= 1:
        raise ValueError("nonempty values and percentile in (0, 1] required")
    ordered = sorted(values)
    return ordered[math.ceil(len(ordered) * fraction) - 1]


def validate_samples(iterations: int, warmup: int) -> None:
    """Stay within the service's default 60-request process-local window."""
    if not 1 <= iterations <= 60 or not 0 <= warmup or iterations + warmup > 60:
        raise ValueError("iterations must be 1..60 and iterations + warmup <= 60")


def reserve_loopback_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def benchmark(iterations: int, warmup: int) -> dict[str, object]:
    validate_samples(iterations, warmup)
    port = reserve_loopback_port()
    base_url = f"http://127.0.0.1:{port}"
    key = secrets.token_urlsafe(32)
    environment = os.environ.copy()
    environment["BUDGET_GUARD_API_KEY"] = key
    opener = build_opener(ProxyHandler({}))  # Do not route local traffic via proxies.
    process = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "app.main:app",
            "--host",
            "127.0.0.1",
            "--port",
            str(port),
            "--no-access-log",
        ],
        cwd=Path(__file__).resolve().parents[1],
        env=environment,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        deadline = time.monotonic() + 15
        while True:
            if process.poll() is not None:
                raise RuntimeError(f"Local Uvicorn exited with code {process.returncode}")
            try:
                with opener.open(f"{base_url}/healthz", timeout=1) as response:
                    if response.status == 200 and response.read() == b'{"status":"ok"}':
                        break
            except (OSError, URLError, HTTPError):
                pass
            if time.monotonic() >= deadline:
                raise RuntimeError("Local Uvicorn did not become healthy within 15 seconds")
            time.sleep(0.05)

        timings_ms: list[float] = []
        for index in range(iterations + warmup):
            request = Request(
                f"{base_url}/v1/budget/check",
                data=PAYLOAD,
                headers={"Content-Type": "application/json", "X-API-Key": key},
                method="POST",
            )
            start = perf_counter_ns()
            with opener.open(request, timeout=5) as response:
                body = json.load(response)
                if response.status != 200 or body.get("estimated_cost_usd") != "0.006":
                    raise RuntimeError("Unexpected HTTP response contract")
            elapsed_ms = (perf_counter_ns() - start) / 1_000_000
            if index >= warmup:
                timings_ms.append(elapsed_ms)
        return {
            "benchmark": "loopback_tcp_http_urllib",
            "python": sys.version.split()[0],
            "iterations": iterations,
            "warmup": warmup,
            "p50_ms": round(median(timings_ms), 3),
            "p95_ms": round(percentile(timings_ms, 0.95), 3),
            "p99_ms": round(percentile(timings_ms, 0.99), 3),
            "min_ms": round(min(timings_ms), 3),
            "max_ms": round(max(timings_ms), 3),
            "limitations": (
                "sequential loopback TCP; new connection per request; "
                "single process; no external deployment, provider, load or real AI costs"
            ),
        }
    finally:
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=5)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--iterations", type=int, default=40)
    parser.add_argument("--warmup", type=int, default=5)
    args = parser.parse_args()
    try:
        validate_samples(args.iterations, args.warmup)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(benchmark(args.iterations, args.warmup), sort_keys=True))


if __name__ == "__main__":
    main()
