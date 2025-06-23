"""
Test Metrics Collector
"""

import sys
sys.path.append('..')
from core.metrics import MetricsCollector

def test_metrics():
    collector = MetricsCollector()
    
    # Record some metrics
    for i in range(10):
        collector.record("test_metric", i)
    
    # Get stats
    stats = collector.get_stats("test_metric")
    assert stats["count"] == 10
    assert stats["mean"] == 4.5
    assert stats["min"] == 0
    assert stats["max"] == 9
    
    print("Metrics test passed!")

if __name__ == "__main__":
    test_metrics()