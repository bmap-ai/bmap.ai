"""
API Request Validators
"""

from pydantic import BaseModel, validator
from typing import Optional, List

class WalletAnalysisRequest(BaseModel):
    address: str
    include_transactions: bool = True
    max_transactions: int = 1000
    
    @validator('address')
    def validate_address(cls, v):
        if not v.startswith('0x') or len(v) != 42:
            raise ValueError('Invalid address format')
        return v.lower()

class TransactionFilter(BaseModel):
    from_address: Optional[str]
    to_address: Optional[str]
    min_value: Optional[float] = 0
    max_value: Optional[float]
    start_date: Optional[str]
    end_date: Optional[str]

class BundleDetectionRequest(BaseModel):
    transactions: List[dict]
    min_bundle_size: int = 3
    eps: float = 50.0