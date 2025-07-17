"""
Advanced Clustering Module
"""

from sklearn.cluster import KMeans, AgglomerativeClustering
import numpy as np

class AdvancedClustering:
    def __init__(self):
        self.models = {}
        
    def kmeans_clustering(self, features, n_clusters=5):
        """Perform K-means clustering"""
        model = KMeans(n_clusters=n_clusters, random_state=42)
        labels = model.fit_predict(features)
        self.models['kmeans'] = model
        return labels
    
    def hierarchical_clustering(self, features, n_clusters=5):
        """Perform hierarchical clustering"""
        model = AgglomerativeClustering(n_clusters=n_clusters)
        labels = model.fit_predict(features)
        self.models['hierarchical'] = model
        return labels
    
    def get_cluster_centers(self, model_name='kmeans'):
        """Get cluster centers"""
        if model_name in self.models and hasattr(self.models[model_name], 'cluster_centers_'):
            return self.models[model_name].cluster_centers_
        return None