"""
Test ML Pipeline
"""

import sys
import numpy as np
sys.path.append('..')
from core.ml_pipeline import MLPipeline

def test_ml_pipeline():
    pipeline = MLPipeline()
    
    # Generate test data
    X_train = np.random.randn(100, 10)
    y_train = np.random.randint(0, 2, 100)
    
    # Train
    pipeline.train(X_train, y_train)
    
    # Test prediction
    X_test = np.random.randn(10, 10)
    predictions = pipeline.predict(X_test)
    
    assert len(predictions) == 10
    assert all(p in [0, 1] for p in predictions)
    
    # Test probabilities
    proba = pipeline.predict_proba(X_test)
    assert proba.shape == (10, 2)
    
    print("ML Pipeline test passed!")

if __name__ == "__main__":
    test_ml_pipeline()