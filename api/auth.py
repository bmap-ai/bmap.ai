"""
Authentication Module
"""

from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader
import hashlib
import time

api_key_header = APIKeyHeader(name="X-API-Key")

class AuthManager:
    def __init__(self):
        self.api_keys = {}
        self.rate_limits = {}
        
    def create_api_key(self, user_id):
        """Generate new API key"""
        key = hashlib.sha256(f"{user_id}{time.time()}".encode()).hexdigest()
        self.api_keys[key] = {
            "user_id": user_id,
            "created": time.time(),
            "active": True
        }
        return key
    
    def verify_api_key(self, api_key: str = Security(api_key_header)):
        """Verify API key"""
        if api_key not in self.api_keys:
            raise HTTPException(status_code=403, detail="Invalid API key")
        
        key_data = self.api_keys[api_key]
        if not key_data["active"]:
            raise HTTPException(status_code=403, detail="API key deactivated")
        
        return key_data