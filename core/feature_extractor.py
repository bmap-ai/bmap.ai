"""
Feature Extraction Module
"""

import numpy as np

class FeatureExtractor:
    def __init__(self):
        self.features = []
        
    def extract(self, transactions):
        """Extract features from transactions"""
        if not transactions:
            return np.zeros(10)
            
        features = [
            len(transactions),  # Transaction count
            np.mean([tx.get('value', 0) for tx in transactions]),  # Avg value
            np.std([tx.get('value', 0) for tx in transactions]),  # Std value
        ]
        return np.array(features)