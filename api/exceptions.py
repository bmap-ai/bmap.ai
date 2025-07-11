"""
Custom API Exceptions
"""

from fastapi import HTTPException
from typing import Any, Dict

class APIException(HTTPException):
    def __init__(self, status_code: int, detail: Any = None, headers: Dict[str, Any] = None):
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class NotFoundError(APIException):
    def __init__(self, detail: str = "Resource not found"):
        super().__init__(status_code=404, detail=detail)

class ValidationError(APIException):
    def __init__(self, detail: str = "Validation failed"):
        super().__init__(status_code=422, detail=detail)

class RateLimitError(APIException):
    def __init__(self, detail: str = "Rate limit exceeded"):
        super().__init__(status_code=429, detail=detail)

class AuthenticationError(APIException):
    def __init__(self, detail: str = "Authentication failed"):
        super().__init__(status_code=401, detail=detail)

class ServerError(APIException):
    def __init__(self, detail: str = "Internal server error"):
        super().__init__(status_code=500, detail=detail)