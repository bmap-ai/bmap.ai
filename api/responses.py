"""
API Response Models
"""

from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class SuccessResponse(BaseModel):
    status: str = "success"
    data: Any
    timestamp: datetime = datetime.now()

class ErrorResponse(BaseModel):
    status: str = "error"
    error: str
    detail: Optional[str] = None
    timestamp: datetime = datetime.now()

class WalletResponse(BaseModel):
    address: str
    risk_score: float
    patterns: List[str]
    tx_count: int
    graph_metrics: Optional[Dict] = None

class AnalysisResponse(BaseModel):
    status: str
    result: WalletResponse
    processing_time: float
    timestamp: datetime