"""
Main API Module
"""

from fastapi import FastAPI, Depends, HTTPException, WebSocket
from core.analyzer import WalletAnalyzer
from database import get_db, engine, Base
from sqlalchemy.orm import Session
from .auth import AuthManager
from .websocket import websocket_endpoint
from monitoring import track_request
import time

app = FastAPI(title="bmap.ai", version="1.0.0")
analyzer = WalletAnalyzer()
auth_manager = AuthManager()

# Create database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    track_request("GET", "/")
    return {"name": "bmap.ai", "status": "active"}

@app.websocket("/ws")
async def websocket_route(websocket: WebSocket):
    await websocket_endpoint(websocket)

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
    return {"status": "healthy", "version": "1.0.0", "timestamp": time.time()}