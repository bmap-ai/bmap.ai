"""
API v2 Endpoints
"""

from fastapi import APIRouter, Depends
from typing import List
from api.validators import WalletAnalysisRequest
from core.analyzer import WalletAnalyzer

router = APIRouter(prefix="/api/v2")
analyzer = WalletAnalyzer()

@router.post("/analyze/batch")
async def analyze_batch(requests: List[WalletAnalysisRequest]):
    """Batch analysis endpoint"""
    results = []
    for req in requests:
        result = analyzer.analyze(req.address)
        results.append(result)
    return {"results": results}

@router.get("/status")
async def get_status():
    """Get system status"""
    return {
        "version": "2.0.0",
        "status": "operational",
        "features": ["batch_processing", "real_time_updates", "advanced_ml"]
    }