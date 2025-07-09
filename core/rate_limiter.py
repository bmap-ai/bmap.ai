"""
Rate Limiting Module
"""

import time
from collections import defaultdict
from threading import Lock

class RateLimiter:
    def __init__(self, max_requests=100, window_seconds=60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(list)
        self.lock = Lock()
        
    def is_allowed(self, key):
        """Check if request is allowed"""
        with self.lock:
            now = time.time()
            
            # Clean old requests
            self.requests[key] = [
                req_time for req_time in self.requests[key]
                if now - req_time < self.window_seconds
            ]
            
            # Check limit
            if len(self.requests[key]) >= self.max_requests:
                return False
            
            # Add new request
            self.requests[key].append(now)
            return True
    
    def get_remaining(self, key):
        """Get remaining requests"""
        with self.lock:
            now = time.time()
            self.requests[key] = [
                req_time for req_time in self.requests[key]
                if now - req_time < self.window_seconds
            ]
            return self.max_requests - len(self.requests[key])