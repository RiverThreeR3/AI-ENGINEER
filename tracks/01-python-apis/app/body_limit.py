"""Bounded ASGI body buffering for the JSON budget endpoint only."""

from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Message, Receive, Scope, Send


class BodyLimitMiddleware:
    """Reject oversized Content-Length and chunked bodies before JSON parsing."""

    def __init__(self, app: ASGIApp, max_bytes: int = 2048) -> None:
        if max_bytes < 1:
            raise ValueError("max_bytes must be positive")
        self.app = app
        self.max_bytes = max_bytes

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http" or scope.get("path") != "/v1/budget/check":
            await self.app(scope, receive, send)
            return

        async def reject(status_code: int, detail: str) -> None:
            response = JSONResponse({"detail": detail}, status_code=status_code)
            await response(scope, receive, send)

        for name, value in scope.get("headers", []):
            if name.lower() != b"content-length":
                continue
            try:
                declared = int(value)
            except ValueError:
                await reject(400, "Invalid Content-Length")
                return
            if declared < 0:
                await reject(400, "Invalid Content-Length")
                return
            if declared > self.max_bytes:
                await reject(413, "Request body too large")
                return

        body = bytearray()
        while True:
            message = await receive()
            if message["type"] == "http.disconnect":
                return
            if message["type"] != "http.request":
                continue
            chunk = message.get("body", b"")
            if len(chunk) > self.max_bytes - len(body):
                await reject(413, "Request body too large")
                return
            body.extend(chunk)
            if not message.get("more_body", False):
                break

        buffered_body = bytes(body)
        pending = True

        async def replay() -> Message:
            nonlocal pending
            if pending:
                pending = False
                return {"type": "http.request", "body": buffered_body, "more_body": False}
            return await receive()

        await self.app(scope, replay, send)
