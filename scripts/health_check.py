"""
Health Check Script
"""

import sys
import requests
import psutil
import time

def check_api():
    """Check API health"""
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        return response.status_code == 200
    except:
        return False

def check_system():
    """Check system resources"""
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    return {
        "cpu_ok": cpu < 80,
        "memory_ok": memory < 80,
        "disk_ok": disk < 90
    }

def main():
    """Run health checks"""
    print("Running health checks...")
    
    api_healthy = check_api()
    system_stats = check_system()
    
    print(f"API Status: {'OK' if api_healthy else 'DOWN'}")
    print(f"CPU: {'OK' if system_stats['cpu_ok'] else 'HIGH'}")
    print(f"Memory: {'OK' if system_stats['memory_ok'] else 'HIGH'}")
    print(f"Disk: {'OK' if system_stats['disk_ok'] else 'FULL'}")
    
    all_healthy = api_healthy and all(system_stats.values())
    return 0 if all_healthy else 1

if __name__ == "__main__":
    sys.exit(main())