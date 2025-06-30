"""
Test Graph Analysis
"""

import sys
sys.path.append('..')
from core.graph_analyzer import GraphAnalyzer

def test_graph_analysis():
    analyzer = GraphAnalyzer()
    
    # Create test transactions
    transactions = [
        {"from": "A", "to": "B", "value": 100},
        {"from": "B", "to": "C", "value": 50},
        {"from": "C", "to": "A", "value": 25},
        {"from": "A", "to": "D", "value": 75}
    ]
    
    analyzer.build_graph(transactions)
    metrics = analyzer.analyze()
    
    assert metrics["nodes"] == 4
    assert metrics["edges"] == 4
    assert "density" in metrics
    
    communities = analyzer.find_communities()
    assert len(communities) > 0
    
    print("Graph analysis test passed!")

if __name__ == "__main__":
    test_graph_analysis()