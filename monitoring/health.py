"""
Health Check Module
"""

import psutil
import time

class HealthChecker:
    def __init__(self):
        self.start_time = time.time()
        
    def get_system_health(self):
        """Get system health metrics"""
        return {
            "cpu_percent": psutil.cpu_percent(),
            "memory_percent": psutil.virtual_memory().percent,
            "disk_percent": psutil.disk_usage('/').percent,
            "uptime": time.time() - self.start_time
        }
    
    def check_service_health(self):
        """Check service health"""
        health = {
            "status": "healthy",
            "services": {}
        }
        
        # Check database
        try:
            # Database check logic
            health["services"]["database"] = "up"
        except:
            health["services"]["database"] = "down"
            health["status"] = "degraded"
        
        # Check Redis
        try:
            # Redis check logic
            health["services"]["redis"] = "up"
        except:
            health["services"]["redis"] = "down"
        
        return health