"""
Encryption Module
"""

import hashlib
import hmac
from cryptography.fernet import Fernet

class Encryption:
    def __init__(self, key=None):
        if key:
            self.cipher = Fernet(key)
        else:
            self.cipher = Fernet(Fernet.generate_key())
    
    def encrypt(self, data):
        """Encrypt data"""
        if isinstance(data, str):
            data = data.encode()
        return self.cipher.encrypt(data)
    
    def decrypt(self, encrypted_data):
        """Decrypt data"""
        return self.cipher.decrypt(encrypted_data).decode()
    
    @staticmethod
    def hash_data(data):
        """Hash data using SHA256"""
        if isinstance(data, str):
            data = data.encode()
        return hashlib.sha256(data).hexdigest()
    
    @staticmethod
    def verify_signature(data, signature, secret):
        """Verify HMAC signature"""
        expected = hmac.new(secret.encode(), data.encode(), hashlib.sha256).hexdigest()
        return hmac.compare_digest(expected, signature)