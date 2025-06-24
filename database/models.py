"""
Database Models
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Wallet(Base):
    __tablename__ = "wallets"
    
    id = Column(Integer, primary_key=True)
    address = Column(String(42), unique=True, index=True)
    risk_score = Column(Float, default=0.0)
    first_seen = Column(DateTime, default=datetime.utcnow)
    last_analyzed = Column(DateTime)
    is_flagged = Column(Boolean, default=False)
    
class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True)
    hash = Column(String(66), unique=True, index=True)
    from_address = Column(String(42), index=True)
    to_address = Column(String(42), index=True)
    value = Column(Float)
    timestamp = Column(DateTime)
    is_anomaly = Column(Boolean, default=False)
    
class Bundle(Base):
    __tablename__ = "bundles"
    
    id = Column(Integer, primary_key=True)
    bundle_id = Column(String(32), unique=True)
    size = Column(Integer)
    confidence = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)