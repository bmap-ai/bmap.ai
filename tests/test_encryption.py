"""
Test Encryption
"""

import sys
sys.path.append('..')
from core.encryption import Encryption

def test_encryption():
    enc = Encryption()
    
    # Test encryption/decryption
    original = "sensitive data"
    encrypted = enc.encrypt(original)
    decrypted = enc.decrypt(encrypted)
    
    assert decrypted == original
    assert encrypted != original.encode()
    
    # Test hashing
    hash1 = Encryption.hash_data("test")
    hash2 = Encryption.hash_data("test")
    assert hash1 == hash2
    
    print("Encryption test passed!")

if __name__ == "__main__":
    test_encryption()