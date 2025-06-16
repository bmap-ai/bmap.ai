"""
Test Pattern Recognition
"""

import sys
sys.path.append('..')
from core.patterns import PatternRecognizer

def test_patterns():
    recognizer = PatternRecognizer()
    
    # Test high frequency
    txs = [{"from": "A", "to": "B"} for _ in range(15)]
    patterns = recognizer.detect(txs)
    assert "high_frequency" in patterns
    print("Pattern test passed!")