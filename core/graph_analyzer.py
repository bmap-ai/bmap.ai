"""
Graph Analysis Module
"""

import networkx as nx
import numpy as np

class GraphAnalyzer:
    def __init__(self):
        self.graph = nx.DiGraph()
        
    def build_graph(self, transactions):
        """Build transaction graph"""
        for tx in transactions:
            if tx.get("from") and tx.get("to"):
                self.graph.add_edge(
                    tx["from"], 
                    tx["to"], 
                    weight=tx.get("value", 0),
                    timestamp=tx.get("timestamp", 0)
                )
    
    def analyze(self):
        """Analyze graph metrics"""
        if self.graph.number_of_nodes() == 0:
            return {}
        
        metrics = {
            "nodes": self.graph.number_of_nodes(),
            "edges": self.graph.number_of_edges(),
            "density": nx.density(self.graph)
        }
        
        # Centrality measures
        if self.graph.number_of_nodes() > 1:
            try:
                metrics["avg_degree"] = sum(dict(self.graph.degree()).values()) / self.graph.number_of_nodes()
                metrics["avg_clustering"] = nx.average_clustering(self.graph)
            except:
                pass
        
        return metrics
    
    def find_communities(self):
        """Find communities in graph"""
        if self.graph.number_of_nodes() < 2:
            return []
        
        # Convert to undirected for community detection
        undirected = self.graph.to_undirected()
        communities = list(nx.community.greedy_modularity_communities(undirected))
        
        return [list(community) for community in communities]