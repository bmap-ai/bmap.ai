"""
Transaction Parser
"""

from .validator import TransactionValidator

class TransactionParser:
    def __init__(self):
        self.parsed_count = 0
        self.validator = TransactionValidator()
        
    def parse(self, tx_data):
        """Parse a single transaction"""
        self.parsed_count += 1
        parsed = {
            "hash": tx_data.get("hash"),
            "from": tx_data.get("from"),
            "to": tx_data.get("to"),
            "value": float(tx_data.get("value", 0)),
            "timestamp": tx_data.get("timestamp", 0)
        }
        
        # Validate transaction
        is_valid, msg = self.validator.validate_transaction(parsed)
        if not is_valid:
            parsed["validation_error"] = msg
        
        return parsed