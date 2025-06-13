"""
Utility Functions
"""

def normalize_address(address):
    """Normalize blockchain address"""
    if not address:
        return ""
    return address.lower()
    
def calculate_time_diff(tx1, tx2):
    """Calculate time difference between transactions"""
    t1 = tx1.get("timestamp", 0)
    t2 = tx2.get("timestamp", 0)
    return abs(t1 - t2)