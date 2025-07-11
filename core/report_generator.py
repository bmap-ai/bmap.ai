"""
Report Generation Module
"""

from datetime import datetime
import json

class ReportGenerator:
    def __init__(self):
        self.template = {
            "title": "Wallet Analysis Report",
            "generated_at": None,
            "summary": {},
            "details": []
        }
    
    def generate_wallet_report(self, analysis_result):
        """Generate wallet analysis report"""
        report = self.template.copy()
        report["generated_at"] = datetime.now().isoformat()
        
        report["summary"] = {
            "address": analysis_result.get("address"),
            "risk_score": analysis_result.get("risk_score"),
            "patterns_detected": len(analysis_result.get("patterns", [])),
            "transaction_count": analysis_result.get("tx_count", 0)
        }
        
        report["details"] = {
            "patterns": analysis_result.get("patterns", []),
            "graph_metrics": analysis_result.get("graph_metrics", {}),
            "recommendations": self._generate_recommendations(analysis_result)
        }
        
        return report
    
    def _generate_recommendations(self, analysis_result):
        """Generate recommendations based on analysis"""
        recommendations = []
        risk_score = analysis_result.get("risk_score", 0)
        
        if risk_score > 0.7:
            recommendations.append("High risk - detailed investigation recommended")
        elif risk_score > 0.4:
            recommendations.append("Medium risk - monitor activity")
        else:
            recommendations.append("Low risk - standard monitoring")
        
        if "mixer_interaction" in analysis_result.get("patterns", []):
            recommendations.append("Mixer interaction detected - verify source of funds")
        
        return recommendations
    
    def export_report(self, report, filepath):
        """Export report to file"""
        with open(filepath, 'w') as f:
            json.dump(report, f, indent=2)