"""
Data Validation Module
"""

import re
from typing import Dict, List, Any

class DataValidator:
    def __init__(self):
        self.rules = {
            'address': r'^0x[a-fA-F0-9]{40}$',
            'tx_hash': r'^0x[a-fA-F0-9]{64}$',
            'positive_number': lambda x: x >= 0
        }
    
    def validate_address(self, address: str) -> bool:
        """Validate Ethereum address"""
        return bool(re.match(self.rules['address'], address))
    
    def validate_transaction_hash(self, tx_hash: str) -> bool:
        """Validate transaction hash"""
        return bool(re.match(self.rules['tx_hash'], tx_hash))
    
    def validate_batch(self, data: List[Dict]) -> Dict:
        """Validate batch of data"""
        valid = []
        invalid = []
        
        for item in data:
            if self._validate_item(item):
                valid.append(item)
            else:
                invalid.append(item)
        
        return {
            'valid': valid,
            'invalid': invalid,
            'valid_count': len(valid),
            'invalid_count': len(invalid)
        }
    
    def _validate_item(self, item: Dict) -> bool:
        """Validate single item"""
        if 'address' in item and not self.validate_address(item['address']):
            return False
        if 'hash' in item and not self.validate_transaction_hash(item['hash']):
            return False
        if 'value' in item and item['value'] < 0:
            return False
        return True