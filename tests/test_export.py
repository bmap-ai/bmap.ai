"""
Test Data Export
"""

import sys
import os
import json
sys.path.append('..')
from core.data_export import DataExporter

def test_data_export():
    exporter = DataExporter()
    
    # Test data
    data = [
        {"address": "0xa1", "risk_score": 0.3},
        {"address": "0xa2", "risk_score": 0.7},
        {"address": "0xa3", "risk_score": 0.1}
    ]
    
    # Test JSON export
    exporter.export_json(data, "test_output.json")
    assert os.path.exists("test_output.json")
    
    with open("test_output.json", 'r') as f:
        loaded = json.load(f)
        assert len(loaded) == 3
    
    # Clean up
    os.remove("test_output.json")
    
    print("Export test passed!")

if __name__ == "__main__":
    test_data_export()