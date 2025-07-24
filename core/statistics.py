"""
Statistical Analysis Module
"""

import numpy as np
from scipy import stats as scipy_stats

class Statistics:
    @staticmethod
    def calculate_summary(values):
        """Calculate summary statistics"""
        if not values:
            return {}
        
        arr = np.array(values)
        return {
            'mean': float(np.mean(arr)),
            'median': float(np.median(arr)),
            'std': float(np.std(arr)),
            'min': float(np.min(arr)),
            'max': float(np.max(arr)),
            'q25': float(np.percentile(arr, 25)),
            'q75': float(np.percentile(arr, 75))
        }
    
    @staticmethod
    def detect_outliers(values, method='iqr'):
        """Detect outliers in data"""
        if len(values) < 4:
            return []
        
        arr = np.array(values)
        
        if method == 'iqr':
            q1 = np.percentile(arr, 25)
            q3 = np.percentile(arr, 75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            outliers = np.where((arr < lower_bound) | (arr > upper_bound))[0]
        elif method == 'zscore':
            z_scores = np.abs(scipy_stats.zscore(arr))
            outliers = np.where(z_scores > 3)[0]
        else:
            outliers = []
        
        return outliers.tolist()