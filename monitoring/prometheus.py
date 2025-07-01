"""
Prometheus Metrics
"""

from prometheus_client import Counter, Histogram, Gauge
import time

# Metrics
request_count = Counter('bmap_requests_total', 'Total requests', ['method', 'endpoint'])
request_duration = Histogram('bmap_request_duration_seconds', 'Request duration')
active_connections = Gauge('bmap_active_connections', 'Active connections')
risk_scores = Histogram('bmap_risk_scores', 'Risk score distribution')

def track_request(method, endpoint):
    """Track request metrics"""
    request_count.labels(method=method, endpoint=endpoint).inc()

def track_duration(func):
    """Decorator to track function duration"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        request_duration.observe(duration)
        return result
    return wrapper