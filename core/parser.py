"""
Transaction Parser
"""

class TransactionParser:
    def __init__(self):
        self.parsed_count = 0
        
    def parse(self, tx_data):
        """Parse a single transaction"""
        self.parsed_count += 1
        return {
            "hash": tx_data.get("hash"),
            "from": tx_data.get("from"),
            "to": tx_data.get("to"),
            "value": float(tx_data.get("value", 0))
        }