"""
Bundle Detection Module
"""

from sklearn.cluster import DBSCAN
import numpy as np
from collections import defaultdict

class BundleDetector:
    def __init__(self, min_size=3):
        self.bundles = []
        self.min_size = min_size
        
    def detect(self, transactions):
        """Detect transaction bundles using DBSCAN"""
        if len(transactions) < self.min_size:
            return []
        
        # Extract features for clustering
        features = []
        for tx in transactions:
            features.append([
                tx.get("timestamp", 0),
                hash(tx.get("from", "")) % 1000,
                hash(tx.get("to", "")) % 1000,
                tx.get("value", 0)
            ])
        
        # Apply DBSCAN clustering
        X = np.array(features)
        clustering = DBSCAN(eps=50, min_samples=self.min_size).fit(X)
        
        # Group transactions by cluster
        bundles = defaultdict(list)
        for i, label in enumerate(clustering.labels_):
            if label != -1:
                bundles[label].append(transactions[i])
        
        # Format results with metadata
        result = []
        for bundle_id, txs in bundles.items():
            result.append({
                "bundle_id": bundle_id,
                "size": len(txs),
                "confidence": min(0.95, len(txs) / 10),
                "transactions": txs
            })
        
        self.bundles = result
        return result