"""
Anomaly Detection Module
"""

import numpy as np
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self, contamination=0.1):
        self.model = IsolationForest(contamination=contamination)
        self.is_trained = False
        
    def train(self, features):
        """Train anomaly detection model"""
        if len(features) < 10:
            return False
        
        X = np.array(features)
        self.model.fit(X)
        self.is_trained = True
        return True
    
    def detect(self, features):
        """Detect anomalies"""
        if not self.is_trained:
            return []
        
        X = np.array(features).reshape(1, -1) if len(features.shape) == 1 else features
        predictions = self.model.predict(X)
        
        # -1 indicates anomaly, 1 indicates normal
        anomalies = []
        for i, pred in enumerate(predictions):
            if pred == -1:
                anomalies.append({
                    "index": i,
                    "score": self.model.score_samples(X[i:i+1])[0]
                })
        
        return anomalies