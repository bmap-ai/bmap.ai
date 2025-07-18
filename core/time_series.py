"""
Time Series Analysis
"""

import numpy as np
from scipy import stats

class TimeSeriesAnalyzer:
    def __init__(self):
        self.data = []
        
    def analyze_trend(self, timestamps, values):
        """Analyze time series trend"""
        if len(timestamps) < 2:
            return {"trend": "insufficient_data"}
        
        # Linear regression for trend
        slope, intercept, r_value, p_value, std_err = stats.linregress(timestamps, values)
        
        trend = "increasing" if slope > 0 else "decreasing"
        strength = abs(r_value)
        
        return {
            "trend": trend,
            "strength": strength,
            "slope": slope,
            "p_value": p_value
        }
    
    def detect_seasonality(self, values):
        """Detect seasonality in time series"""
        if len(values) < 24:
            return None
        
        # Simple FFT-based seasonality detection
        fft = np.fft.fft(values)
        frequencies = np.fft.fftfreq(len(values))
        
        # Find dominant frequency
        idx = np.argmax(np.abs(fft[1:len(fft)//2])) + 1
        dominant_freq = frequencies[idx]
        
        return {
            "has_seasonality": abs(dominant_freq) > 0.1,
            "period": 1/abs(dominant_freq) if dominant_freq != 0 else None
        }