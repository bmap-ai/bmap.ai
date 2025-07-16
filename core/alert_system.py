"""
Alert System Module
"""

from typing import Dict, List
from datetime import datetime
import json

class AlertSystem:
    def __init__(self):
        self.alerts = []
        self.thresholds = {
            "high_risk": 0.8,
            "medium_risk": 0.5,
            "transaction_volume": 1000
        }
        
    def check_risk_threshold(self, wallet_address, risk_score):
        """Check if risk score exceeds threshold"""
        if risk_score >= self.thresholds["high_risk"]:
            self.create_alert("HIGH_RISK", wallet_address, f"Risk score {risk_score}")
            return "high"
        elif risk_score >= self.thresholds["medium_risk"]:
            self.create_alert("MEDIUM_RISK", wallet_address, f"Risk score {risk_score}")
            return "medium"
        return "low"
    
    def create_alert(self, alert_type, target, message):
        """Create new alert"""
        alert = {
            "id": len(self.alerts) + 1,
            "type": alert_type,
            "target": target,
            "message": message,
            "timestamp": datetime.now().isoformat(),
            "status": "active"
        }
        self.alerts.append(alert)
        return alert
    
    def get_active_alerts(self):
        """Get all active alerts"""
        return [a for a in self.alerts if a["status"] == "active"]
    
    def acknowledge_alert(self, alert_id):
        """Acknowledge an alert"""
        for alert in self.alerts:
            if alert["id"] == alert_id:
                alert["status"] = "acknowledged"
                return True
        return False