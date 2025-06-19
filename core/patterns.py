"""
Pattern Recognition Module
"""

import numpy as np
from collections import Counter

class PatternRecognizer:
    def __init__(self):
        self.patterns = []
        
    def detect(self, transactions):
        """Detect patterns in transactions"""
        if len(transactions) < 3:
            return []
        
        # Simple pattern detection
        patterns = []
        
        # Check for high frequency
        if len(transactions) > 10:
            patterns.append("high_frequency")
            
        # Check for circular transactions
        addresses = set()
        for tx in transactions:
            addresses.add(tx.get("from"))
            addresses.add(tx.get("to"))
        
        if len(addresses) < len(transactions) * 0.5:
            patterns.append("circular_flow")
            
        # Check for mixer pattern
        if len(addresses) > len(transactions) * 1.5:
            patterns.append("mixer_interaction")
        
        # Check for flash loan pattern
        timestamps = [tx.get("timestamp", 0) for tx in transactions]
        if timestamps:
            time_diffs = np.diff(sorted(timestamps))
            if len(time_diffs) > 0 and np.mean(time_diffs) < 60:
                patterns.append("flash_loan")
            
        return patterns