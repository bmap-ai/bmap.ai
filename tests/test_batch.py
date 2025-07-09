"""
Test Batch Processing
"""

import sys
sys.path.append('..')
from core.batch_processor import BatchProcessor

def test_batch_processing():
    processor = BatchProcessor(max_workers=2)
    
    # Test addresses
    addresses = ["0x" + "a" * 40, "0x" + "b" * 40, "0x" + "c" * 40]
    
    # Process batch
    results = processor.process_batch(addresses)
    
    assert len(results) == 3
    for result in results:
        assert "address" in result or "error" in result
    
    print("Batch processing test passed!")

if __name__ == "__main__":
    test_batch_processing()