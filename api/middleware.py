"""
API Middleware
"""

from fastapi import Request
import time

async def timing_middleware(request: Request, call_next):
    """Add request timing"""
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

async def auth_middleware(request: Request, call_next):
    """Simple auth check"""
    api_key = request.headers.get("X-API-Key")
    if request.url.path.startswith("/api/") and not api_key:
        return {"error": "API key required"}
    return await call_next(request)