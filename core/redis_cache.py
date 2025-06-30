"""
Redis Cache Module
"""

import redis
import json
import os

class RedisCache:
    def __init__(self):
        redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
        self.client = redis.from_url(redis_url, decode_responses=True)
        
    def get(self, key):
        """Get value from Redis"""
        value = self.client.get(key)
        if value:
            try:
                return json.loads(value)
            except:
                return value
        return None
    
    def set(self, key, value, ttl=3600):
        """Set value in Redis with TTL"""
        if isinstance(value, (dict, list)):
            value = json.dumps(value)
        self.client.setex(key, ttl, value)
    
    def delete(self, key):
        """Delete key from Redis"""
        self.client.delete(key)
    
    def exists(self, key):
        """Check if key exists"""
        return self.client.exists(key)
    
    def flush(self):
        """Flush all keys"""
        self.client.flushdb()