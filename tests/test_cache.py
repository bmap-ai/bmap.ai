"""
Test Cache Manager
"""

import sys
import time
sys.path.append('..')
from core.cache import CacheManager

def test_cache():
    cache = CacheManager(ttl=1)
    
    # Test set and get
    cache.set("key1", "value1")
    assert cache.get("key1") == "value1"
    
    # Test TTL expiration
    time.sleep(1.1)
    assert cache.get("key1") is None
    
    print("Cache test passed!")