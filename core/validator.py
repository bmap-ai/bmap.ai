"""
Transaction Validator Module
"""

import re

class TransactionValidator:
    def __init__(self):
        self.rules = {}
        
    def validate_address(self, address):
        """Validate blockchain address format"""
        if not address:
            return False
        # Check if it's a valid hex string
        if not re.match(r'^0x[a-fA-F0-9]{40}$', address):
            return False
        return True
    
    def validate_transaction(self, tx):
        """Validate transaction data"""
        required_fields = ['from', 'to', 'value', 'timestamp']
        
        for field in required_fields:
            if field not in tx:
                return False, f"Missing field: {field}"
        
        if not self.validate_address(tx['from']):
            return False, "Invalid from address"
        
        if not self.validate_address(tx['to']):
            return False, "Invalid to address"
        
        if tx['value'] < 0:
            return False, "Invalid value"
        
        return True, "Valid"