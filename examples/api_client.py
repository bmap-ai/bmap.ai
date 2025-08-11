"""
API Client Example
"""

import requests
import json

class BmapClient:
    def __init__(self, base_url="http://localhost:8000", api_key=None):
        self.base_url = base_url
        self.headers = {}
        if api_key:
            self.headers["X-API-Key"] = api_key
    
    def analyze_wallet(self, address):
        """Analyze a wallet"""
        response = requests.post(
            f"{self.base_url}/analyze/{address}",
            headers=self.headers
        )
        return response.json()
    
    def get_health(self):
        """Check API health"""
        response = requests.get(f"{self.base_url}/health")
        return response.json()

# Example usage
if __name__ == "__main__":
    client = BmapClient()
    
    # Check health
    health = client.get_health()
    print(f"API Status: {health['status']}")
    
    # Analyze wallet
    result = client.analyze_wallet("0x" + "a" * 40)
    print(f"Analysis Result: {json.dumps(result, indent=2)}")