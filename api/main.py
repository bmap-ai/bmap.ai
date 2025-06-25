"""
Main API Module
"""

from fastapi import FastAPI, Depends, HTTPException
from core.analyzer import WalletAnalyzer
from database import get_db, engine, Base
from sqlalchemy.orm import Session
from .auth import AuthManager

app = FastAPI(title="bmap.ai", version="1.0.0")
analyzer = WalletAnalyzer()
auth_manager = AuthManager()

# Create database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"name": "bmap.ai", "status": "active"}

@app.post("/analyze/{address}")
def analyze_wallet(address: str, db: Session = Depends(get_db)):
    """Analyze a wallet address"""
    try:
        result = analyzer.analyze(address)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "healthy"}