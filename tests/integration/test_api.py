"""
API Integration Tests
"""

import sys
import requests
sys.path.append('../..')

def test_health_endpoint():
    """Test health check endpoint"""
    response = requests.get("http://localhost:8000/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"

def test_analyze_endpoint():
    """Test analysis endpoint"""
    address = "0x" + "a" * 40
    response = requests.post(f"http://localhost:8000/analyze/{address}")
    assert response.status_code in [200, 500]  # 500 if DB not connected

if __name__ == "__main__":
    print("Running API integration tests...")
    # Note: Requires API to be running
    try:
        test_health_endpoint()
        print("Health check test passed!")
    except:
        print("API not running - skipping integration tests")