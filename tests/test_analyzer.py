"""
Test WalletAnalyzer
"""

import sys
sys.path.append('..')
from core.analyzer import WalletAnalyzer

def test_analyzer():
    analyzer = WalletAnalyzer()
    result = analyzer.analyze("0x123")
    assert result["address"] == "0x123"
    assert result["risk_score"] == 0.0
    print("Test passed!")