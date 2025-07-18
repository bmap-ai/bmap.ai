"""
Test Time Series Analysis
"""

import sys
import numpy as np
sys.path.append('..')
from core.time_series import TimeSeriesAnalyzer

def test_time_series():
    analyzer = TimeSeriesAnalyzer()
    
    # Test trend analysis
    timestamps = np.arange(100)
    values = timestamps * 2 + np.random.randn(100) * 5
    
    result = analyzer.analyze_trend(timestamps, values)
    assert result["trend"] == "increasing"
    assert result["strength"] > 0.8
    
    # Test seasonality
    t = np.linspace(0, 4*np.pi, 100)
    seasonal_values = np.sin(t) + np.random.randn(100) * 0.1
    
    seasonality = analyzer.detect_seasonality(seasonal_values)
    assert seasonality["has_seasonality"] == True
    
    print("Time series test passed!")

if __name__ == "__main__":
    test_time_series()