"""
Wallet Similarity Analysis
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from .feature_extractor import FeatureExtractor

class SimilarityAnalyzer:
    def __init__(self):
        self.feature_extractor = FeatureExtractor()
        self.wallet_features = {}
        
    def compute_features(self, wallet_address, transactions):
        """Compute features for a wallet"""
        features = self.feature_extractor.extract(transactions)
        self.wallet_features[wallet_address] = features
        return features
    
    def compute_similarity(self, wallet1, wallet2):
        """Compute similarity between two wallets"""
        if wallet1 not in self.wallet_features or wallet2 not in self.wallet_features:
            return 0.0
        
        feat1 = self.wallet_features[wallet1].reshape(1, -1)
        feat2 = self.wallet_features[wallet2].reshape(1, -1)
        
        similarity = cosine_similarity(feat1, feat2)[0][0]
        return float(similarity)
    
    def find_similar_wallets(self, target_wallet, threshold=0.8):
        """Find wallets similar to target"""
        if target_wallet not in self.wallet_features:
            return []
        
        similar = []
        for wallet in self.wallet_features:
            if wallet != target_wallet:
                sim = self.compute_similarity(target_wallet, wallet)
                if sim >= threshold:
                    similar.append((wallet, sim))
        
        return sorted(similar, key=lambda x: x[1], reverse=True)