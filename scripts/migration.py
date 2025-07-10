"""
Database Migration Script
"""

import sys
sys.path.append('..')
from database import engine, Base
from database.models import Wallet, Transaction, Bundle

def create_tables():
    """Create all database tables"""
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

def drop_tables():
    """Drop all database tables"""
    Base.metadata.drop_all(bind=engine)
    print("Database tables dropped!")

def reset_database():
    """Reset the database"""
    drop_tables()
    create_tables()
    print("Database reset complete!")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Database migration')
    parser.add_argument('command', choices=['create', 'drop', 'reset'])
    args = parser.parse_args()
    
    if args.command == 'create':
        create_tables()
    elif args.command == 'drop':
        drop_tables()
    elif args.command == 'reset':
        reset_database()