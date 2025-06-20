"""
Metrics Collection Module
"""

import time
from collections import deque

class MetricsCollector:
    def __init__(self, window_size=1000):
        self.metrics = {}
        self.window_size = window_size
        
    def record(self, metric_name, value):
        """Record a metric"""
        if metric_name not in self.metrics:
            self.metrics[metric_name] = deque(maxlen=self.window_size)
        self.metrics[metric_name].append({
            "value": value,
            "timestamp": time.time()
        })
    
    def get_stats(self, metric_name):
        """Get statistics for a metric"""
        if metric_name not in self.metrics:
            return None
        
        values = [m["value"] for m in self.metrics[metric_name]]
        if not values:
            return None
        
        return {
            "count": len(values),
            "mean": sum(values) / len(values),
            "min": min(values),
            "max": max(values)
        }