"""
Data Loading Script
"""

import json
import pandas as pd
from typing import List, Dict

class DataLoader:
    def __init__(self):
        self.data = []
        
    def load_json(self, filepath):
        """Load data from JSON file"""
        with open(filepath, 'r') as f:
            self.data = json.load(f)
        return self.data
    
    def load_csv(self, filepath):
        """Load data from CSV file"""
        df = pd.read_csv(filepath)
        self.data = df.to_dict('records')
        return self.data
    
    def filter_by_address(self, address):
        """Filter transactions by address"""
        filtered = []
        for tx in self.data:
            if tx.get('from') == address or tx.get('to') == address:
                filtered.append(tx)
        return filtered
    
    def get_statistics(self):
        """Get basic statistics"""
        if not self.data:
            return {}
        
        return {
            'total_transactions': len(self.data),
            'unique_addresses': len(set([tx.get('from') for tx in self.data] + [tx.get('to') for tx in self.data])),
            'date_range': self._get_date_range()
        }
    
    def _get_date_range(self):
        """Get date range of transactions"""
        timestamps = [tx.get('timestamp', 0) for tx in self.data]
        if timestamps:
            return {
                'start': min(timestamps),
                'end': max(timestamps)
            }
        return {}