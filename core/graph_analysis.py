"""
Graph Analysis Module
"""

import networkx as nx

class GraphAnalyzer:
    def __init__(self):
        self.graph = nx.DiGraph()
        
    def build_graph(self, transactions):
        """Build transaction graph"""
        for tx in transactions:
            from_addr = tx.get("from")
            to_addr = tx.get("to")
            if from_addr and to_addr:
                self.graph.add_edge(from_addr, to_addr, weight=tx.get("value", 0))
        return self.graph
        
    def find_important_nodes(self, top_n=5):
        """Find most important nodes by PageRank"""
        if not self.graph:
            return []
        
        try:
            pagerank = nx.pagerank(self.graph)
            sorted_nodes = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)
            return sorted_nodes[:top_n]
        except:
            return []