"""
Data Export Module
"""

import json
import csv
import pandas as pd
from typing import List, Dict, Any

class DataExporter:
    def __init__(self):
        self.formats = ['json', 'csv', 'excel', 'parquet']
        
    def export_json(self, data: List[Dict], filepath: str):
        """Export data as JSON"""
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
    
    def export_csv(self, data: List[Dict], filepath: str):
        """Export data as CSV"""
        if not data:
            return
        
        keys = data[0].keys()
        with open(filepath, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
    
    def export_excel(self, data: List[Dict], filepath: str):
        """Export data as Excel"""
        df = pd.DataFrame(data)
        df.to_excel(filepath, index=False)
    
    def export_parquet(self, data: List[Dict], filepath: str):
        """Export data as Parquet"""
        df = pd.DataFrame(data)
        df.to_parquet(filepath, index=False)
    
    def export(self, data: List[Dict], filepath: str, format: str = 'json'):
        """Export data in specified format"""
        if format not in self.formats:
            raise ValueError(f"Unsupported format: {format}")
        
        if format == 'json':
            self.export_json(data, filepath)
        elif format == 'csv':
            self.export_csv(data, filepath)
        elif format == 'excel':
            self.export_excel(data, filepath)
        elif format == 'parquet':
            self.export_parquet(data, filepath)