"""Single-process demo API-key authentication and bounded request admission.

This is deliberately not a distributed gateway or durable spending limiter.
"""

import math
import os
import secrets
import time
from threading import Lock
from typing import Annotated, Callable

from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


class FixedWindowLimiter:
    """Thread-safe, process-local fixed-window request counter."""

    def __init__(
        self,
        limit: int = 60,
        window_seconds: float = 60.0,
        clock: Callable[[], float] | None = None,
    ) -> None:
        if limit < 1 or window_seconds <= 0:
            raise ValueError("Rate-limit settings must be positive")
        self._limit = limit
        self._window_seconds = window_seconds
        self._clock = clock or time.monotonic
        self._window_start = self._clock()
        self._used = 0
        self._lock = Lock()

    def retry_after(self) -> int | None:
        """Consume a slot, or return seconds until the window resets."""
        with self._lock:
            now = self._clock()
            elapsed = now - self._window_start
            if elapsed >= self._window_seconds or elapsed < 0:
                self._window_start = now
                self._used = 0
                elapsed = 0.0
            if self._used >= self._limit:
                return max(1, math.ceil(self._window_seconds - elapsed))
            self._used += 1
            return None


limiter = FixedWindowLimiter()


def require_access(
    api_key: Annotated[str | None, Security(api_key_header)],
) -> None:
    """Fail closed without a configured secret; never log or echo API keys."""
    expected = os.environ.get("BUDGET_GUARD_API_KEY", "")
    if len(expected) < 16:
        raise HTTPException(status_code=503, detail="API key is not configured")
    if api_key is None:
        raise HTTPException(
            status_code=401,
            detail="API key required",
            headers={"WWW-Authenticate": "ApiKey"},
        )
    if not secrets.compare_digest(api_key, expected):
        raise HTTPException(status_code=403, detail="Invalid API key")
    retry = limiter.retry_after()
    if retry is not None:
        raise HTTPException(
            status_code=429,
            detail="Request limit exceeded",
            headers={"Retry-After": str(retry)},
        )
