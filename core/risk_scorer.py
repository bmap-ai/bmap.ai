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
        
    def calculate_score(self, metrics):
        """Calculate risk score from metrics"""
        score = 0.0
        
        # Simple scoring logic
        if metrics.get('tx_count', 0) > 100:
            score += 0.3
        if metrics.get('patterns'):
            score += 0.4
        if metrics.get('is_bundled'):
            score += 0.3
            
        return min(score, 1.0)