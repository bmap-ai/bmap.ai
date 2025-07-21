"""
Wallet Analyzer Module
"""

from .parser import TransactionParser
from .patterns import PatternRecognizer
from .risk_scorer import RiskScorer
from .bundle_detector import BundleDetector
from .cache import CacheManager
from .metrics import MetricsCollector
from .anomaly_detector import AnomalyDetector
from .graph_analyzer import GraphAnalyzer
from .alert_system import AlertSystem
from utils import logger

class WalletAnalyzer:
    def __init__(self):
        self.wallets = {}
        self.parser = TransactionParser()
        self.pattern_recognizer = PatternRecognizer()
        self.risk_scorer = RiskScorer()
        self.bundle_detector = BundleDetector()
        self.cache = CacheManager()
        self.metrics = MetricsCollector()
        self.anomaly_detector = AnomalyDetector()
        self.graph_analyzer = GraphAnalyzer()
        self.alert_system = AlertSystem()
        
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
            
            # Calculate risk score
            risk_score = self.risk_scorer.calculate_score(result)
            result["risk_score"] = risk_score
            
            # Record metrics
            self.metrics.record("analysis_count", 1)
            self.metrics.record("risk_score", risk_score)
            
            # Graph analysis
            self.graph_analyzer.build_graph(parsed_txs)
            graph_metrics = self.graph_analyzer.analyze()
            result["graph_metrics"] = graph_metrics
            
            logger.info(f"Analyzed wallet {address}: risk_score={risk_score}")
            
        return result