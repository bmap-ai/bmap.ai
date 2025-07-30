"""
Performance Optimization Module
"""

import functools
import time
from typing import Any, Callable

def memoize(func: Callable) -> Callable:
    """Memoization decorator"""
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    return wrapper

def profile_time(func: Callable) -> Callable:
    """Time profiling decorator"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    
    return wrapper

class PerformanceOptimizer:
    def __init__(self):
        self.metrics = {}
    
    def optimize_batch_size(self, data_size: int) -> int:
        """Determine optimal batch size"""
        if data_size < 100:
            return data_size
        elif data_size < 1000:
            return 50
        elif data_size < 10000:
            return 100
        else:
            return 500