"""
Machine Learning Pipeline
"""

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from .feature_extractor import FeatureExtractor
import joblib

class MLPipeline:
    def __init__(self):
        self.feature_extractor = FeatureExtractor()
        self.pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', RandomForestClassifier(n_estimators=100))
        ])
        self.is_trained = False
        
    def prepare_features(self, transactions_list):
        """Prepare features for multiple wallets"""
        features = []
        for transactions in transactions_list:
            feat = self.feature_extractor.extract(transactions)
            features.append(feat)
        return features
    
    def train(self, X, y):
        """Train the pipeline"""
        self.pipeline.fit(X, y)
        self.is_trained = True
        
    def predict(self, X):
        """Make predictions"""
        if not self.is_trained:
            raise ValueError("Pipeline not trained")
        return self.pipeline.predict(X)
    
    def predict_proba(self, X):
        """Get prediction probabilities"""
        if not self.is_trained:
            raise ValueError("Pipeline not trained")
        return self.pipeline.predict_proba(X)
    
    def save(self, filepath):
        """Save pipeline to file"""
        joblib.dump(self.pipeline, filepath)
    
    def load(self, filepath):
        """Load pipeline from file"""
        self.pipeline = joblib.load(filepath)
        self.is_trained = True