"""
Configuration Module
"""

import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "bmap.ai"
    debug: bool = False
    database_url: str = "sqlite:///./bmap.db"
    api_key_header: str = "X-API-Key"
    max_workers: int = 4
    cache_ttl: int = 3600
    rate_limit: int = 100
    
    class Config:
        env_file = ".env"

settings = Settings()