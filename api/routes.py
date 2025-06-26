"""
API Routes
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from database.models import Wallet, Transaction
from core.analyzer import WalletAnalyzer

router = APIRouter()
analyzer = WalletAnalyzer()

@router.get("/wallets/{address}")
def get_wallet(address: str, db: Session = Depends(get_db)):
    """Get wallet information"""
    wallet = db.query(Wallet).filter(Wallet.address == address).first()
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return wallet

@router.post("/wallets/{address}/analyze")
def analyze_wallet(address: str, db: Session = Depends(get_db)):
    """Analyze a wallet"""
    result = analyzer.analyze(address)
    
    # Store in database
    wallet = db.query(Wallet).filter(Wallet.address == address).first()
    if not wallet:
        wallet = Wallet(address=address)
        db.add(wallet)
    
    wallet.risk_score = result.get("risk_score", 0)
    db.commit()
    
    return result

@router.get("/transactions")
def get_transactions(limit: int = 100, db: Session = Depends(get_db)):
    """Get recent transactions"""
    return db.query(Transaction).limit(limit).all()