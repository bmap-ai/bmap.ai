"""
Feature Extraction Module
"""

import numpy as np
from collections import Counter

class FeatureExtractor:
    def __init__(self):
        self.features = []
        
    def extract(self, transactions):
        """Extract features from transactions"""
        if not transactions:
            return np.zeros(10)
            
        features = []
        
        # Basic statistics
        features.append(len(transactions))
        
        # Value statistics
        values = [tx.get('value', 0) for tx in transactions]
        features.append(np.mean(values) if values else 0)
        features.append(np.std(values) if values else 0)
        features.append(np.max(values) if values else 0)
        features.append(np.min(values) if values else 0)
        
        # Address diversity
        addresses = set()
        for tx in transactions:
            addresses.add(tx.get('from'))
            addresses.add(tx.get('to'))
        features.append(len(addresses))
        
        # Time features
        timestamps = [tx.get('timestamp', 0) for tx in transactions]
        if len(timestamps) > 1:
            time_diffs = np.diff(sorted(timestamps))
            features.append(np.mean(time_diffs))
            features.append(np.std(time_diffs))
        else:
            features.extend([0, 0])
        
        # Pad or truncate to 10 features
        while len(features) < 10:
            features.append(0)
        
        return np.array(features[:10])