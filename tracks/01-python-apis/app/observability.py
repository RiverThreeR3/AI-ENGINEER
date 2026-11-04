"""Privacy-conscious request metrics via standard-library structured logging.

Only a fixed route label, HTTP status and elapsed milliseconds are emitted.
No query strings, bodies, headers, client IPs or credentials are recorded.
"""

import json
import logging
import time
from typing import Any

logger = logging.getLogger("budget_guard.requests")


class RequestMetricsMiddleware:
    """Pure ASGI middleware: observe responses without reading request bodies."""

    def __init__(self, app: Any) -> None:
        self.app = app

    async def __call__(self, scope: dict[str, Any], receive: Any, send: Any) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        # Fixed labels prevent accidental exposure of URL/query/tenant identifiers.
        route = (
            "budget_check"
            if scope.get("path") == "/v1/budget/check"
            else "health"
            if scope.get("path") == "/healthz"
            else "other"
        )
        start = time.perf_counter()
        status = 500

        async def send_observed(message: dict[str, Any]) -> None:
            nonlocal status
            if message["type"] == "http.response.start":
                status = int(message["status"])
            await send(message)

        try:
            await self.app(scope, receive, send_observed)
        finally:
            elapsed_ms = round((time.perf_counter() - start) * 1000, 3)
            logger.info(
                json.dumps(
                    {"event": "http_request", "route": route, "status": status,
                     "duration_ms": elapsed_ms},
                    separators=(",", ":"),
                )
            )
