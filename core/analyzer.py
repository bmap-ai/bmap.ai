"""
Wallet Analyzer Module
"""

from .parser import TransactionParser
from .patterns import PatternRecognizer

class WalletAnalyzer:
    def __init__(self):
        self.wallets = {}
        self.parser = TransactionParser()
        self.pattern_recognizer = PatternRecognizer()
        
    def analyze(self, address, transactions=None):
        """Analyze a wallet address"""
        result = {
            "address": address,
            "risk_score": 0.0,
            "tx_count": 0
        }
        
        if transactions:
            result["tx_count"] = len(transactions)
            
            # Parse transactions
            parsed_txs = [self.parser.parse(tx) for tx in transactions]
            
            # Detect patterns
            patterns = self.pattern_recognizer.detect(parsed_txs)
            result["patterns"] = patterns
            
        return result