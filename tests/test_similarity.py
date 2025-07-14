"""
Test Similarity Analysis
"""

import sys
import numpy as np
sys.path.append('..')
from core.similarity import SimilarityAnalyzer

def test_similarity():
    analyzer = SimilarityAnalyzer()
    
    # Create test transactions
    txs1 = [{"value": 100, "timestamp": i} for i in range(10)]
    txs2 = [{"value": 100, "timestamp": i} for i in range(10)]
    txs3 = [{"value": 500, "timestamp": i*2} for i in range(5)]
    
    # Compute features
    analyzer.compute_features("wallet1", txs1)
    analyzer.compute_features("wallet2", txs2)
    analyzer.compute_features("wallet3", txs3)
    
    # Test similarity
    sim = analyzer.compute_similarity("wallet1", "wallet2")
    assert sim > 0.9  # Should be very similar
    
    sim2 = analyzer.compute_similarity("wallet1", "wallet3")
    assert sim2 < sim  # Should be less similar
    
    # Test finding similar wallets
    similar = analyzer.find_similar_wallets("wallet1", threshold=0.8)
    assert len(similar) > 0
    
    print("Similarity test passed!")

if __name__ == "__main__":
    test_similarity()