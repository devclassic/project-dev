from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from ..utils.data import db
import anyio


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith("/api/admin"):
            uncheck_paths = [
                "/api/admin/auth/login",
                "/api/admin/auth/check",
            ]
            if request.url.path in uncheck_paths:
                return await call_next(request)
            else:
                token = request.headers.get("token")
                if not token:
                    return JSONResponse(
                        content={"success": False, "code": 1001, "message": "未登录"},
                        headers={
                            "Access-Control-Allow-Origin": "*",
                        },
                    )
                user = await anyio.to_thread.run_sync(db["users"].find_one, token=token)
                if not user:
                    return JSONResponse(
                        content={"success": False, "code": 1001, "message": "未登录"},
                        headers={
                            "Access-Control-Allow-Origin": "*",
                        },
                    )
                request.state.user = user

        return await call_next(request)
