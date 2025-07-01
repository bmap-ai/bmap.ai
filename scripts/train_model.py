"""
Model Training Script
"""

import sys
sys.path.append('..')
from core.ml_pipeline import MLPipeline
import numpy as np

def train_model():
    """Train the ML model"""
    pipeline = MLPipeline()
    
    # Generate synthetic training data
    X_train = np.random.randn(1000, 10)
    y_train = np.random.randint(0, 2, 1000)
    
    # Train
    pipeline.train(X_train, y_train)
    
    # Save model
    pipeline.save('models/risk_model.pkl')
    print("Model trained and saved!")

if __name__ == "__main__":
    train_model()