"""
Cache Management Module
"""

import time
from functools import lru_cache

class CacheManager:
    def __init__(self, ttl=3600):
        self.cache = {}
        self.ttl = ttl
        
    def get(self, key):
        """Get value from cache"""
        if key in self.cache:
            value, timestamp = self.cache[key]
            if time.time() - timestamp < self.ttl:
                return value
            else:
                del self.cache[key]
        return None
    
    def set(self, key, value):
        """Set value in cache"""
        self.cache[key] = (value, time.time())
    
    def clear(self):
        """Clear cache"""
        self.cache = {}