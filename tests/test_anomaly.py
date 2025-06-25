"""
Test Anomaly Detection
"""

import sys
import numpy as np
sys.path.append('..')
from core.anomaly_detector import AnomalyDetector

def test_anomaly_detection():
    detector = AnomalyDetector()
    
    # Generate normal data
    normal_data = np.random.randn(100, 5)
    
    # Add some anomalies
    anomalies = np.random.randn(10, 5) * 5
    
    all_data = np.vstack([normal_data, anomalies])
    
    # Train model
    detector.train(all_data)
    
    # Test detection
    test_anomaly = np.array([10, 10, 10, 10, 10])
    results = detector.detect(test_anomaly)
    
    assert len(results) > 0
    print("Anomaly detection test passed!")

if __name__ == "__main__":
    test_anomaly_detection()