"""
Seed Database Script
"""

import sys
import random
sys.path.append('..')
from database import get_db, engine
from database.models import Base, Wallet, Transaction
from datetime import datetime, timedelta

def seed_database():
    """Seed database with test data"""
    Base.metadata.create_all(bind=engine)
    
    db = next(get_db())
    
    # Create test wallets
    wallets = []
    for i in range(10):
        wallet = Wallet(
            address=f"0x{'a' * 38}{i:02d}",
            risk_score=random.random(),
            first_seen=datetime.now() - timedelta(days=random.randint(1, 30))
        )
        wallets.append(wallet)
        db.add(wallet)
    
    # Create test transactions
    for _ in range(100):
        tx = Transaction(
            hash=f"0x{'b' * 62}{random.randint(0, 99):02d}",
            from_address=random.choice(wallets).address,
            to_address=random.choice(wallets).address,
            value=random.uniform(0.1, 1000),
            timestamp=datetime.now() - timedelta(hours=random.randint(1, 720))
        )
        db.add(tx)
    
    db.commit()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()