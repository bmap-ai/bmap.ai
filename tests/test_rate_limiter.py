"""
Test Rate Limiter
"""

import sys
import time
sys.path.append('..')
from core.rate_limiter import RateLimiter

def test_rate_limiter():
    limiter = RateLimiter(max_requests=3, window_seconds=1)
    
    # Test within limit
    assert limiter.is_allowed("user1") == True
    assert limiter.is_allowed("user1") == True
    assert limiter.is_allowed("user1") == True
    
    # Test exceeding limit
    assert limiter.is_allowed("user1") == False
    
    # Test different user
    assert limiter.is_allowed("user2") == True
    
    # Test window expiry
    time.sleep(1.1)
    assert limiter.is_allowed("user1") == True
    
    print("Rate limiter test passed!")

if __name__ == "__main__":
    test_rate_limiter()