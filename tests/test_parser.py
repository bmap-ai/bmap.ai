"""
Test TransactionParser
"""

import sys
sys.path.append('..')
from core.parser import TransactionParser

def test_parser():
    parser = TransactionParser()
    tx = {"hash": "0x123", "from": "0xA", "to": "0xB", "value": 100}
    result = parser.parse(tx)
    assert result["hash"] == "0x123"
    assert result["value"] == 100.0
    print("Parser test passed!")