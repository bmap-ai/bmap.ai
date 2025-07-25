"""
Security Module
"""

from fastapi import Request
from typing import List
import ipaddress

class SecurityManager:
    def __init__(self):
        self.blocked_ips = set()
        self.allowed_origins = ["http://localhost:3000", "https://bmap.ai"]
        
    def check_ip(self, request: Request) -> bool:
        """Check if IP is allowed"""
        client_ip = request.client.host
        return client_ip not in self.blocked_ips
    
    def block_ip(self, ip: str):
        """Block an IP address"""
        self.blocked_ips.add(ip)
    
    def unblock_ip(self, ip: str):
        """Unblock an IP address"""
        self.blocked_ips.discard(ip)
    
    def validate_origin(self, origin: str) -> bool:
        """Validate request origin"""
        return origin in self.allowed_origins
    
    def is_private_ip(self, ip: str) -> bool:
        """Check if IP is private"""
        try:
            return ipaddress.ip_address(ip).is_private
        except:
            return False