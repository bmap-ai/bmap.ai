"""
Risk Scoring Module
"""

class RiskScorer:
    def __init__(self):
        self.weights = {
            'transaction_volume': 0.3,
            'pattern_score': 0.4,
            'bundle_score': 0.3
        }