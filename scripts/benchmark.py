"""
Performance Benchmark Script
"""

import time
import sys
sys.path.append('..')
from core.analyzer import WalletAnalyzer
from core.batch_processor import BatchProcessor

def benchmark_single():
    """Benchmark single analysis"""
    analyzer = WalletAnalyzer()
    
    start = time.time()
    for _ in range(100):
        analyzer.analyze("0x" + "a" * 40)
    elapsed = time.time() - start
    
    print(f"Single analysis: {elapsed:.2f}s for 100 iterations")
    print(f"Average: {elapsed/100:.4f}s per analysis")

def benchmark_batch():
    """Benchmark batch processing"""
    processor = BatchProcessor(max_workers=4)
    addresses = ["0x" + str(i).zfill(40) for i in range(100)]
    
    start = time.time()
    processor.process_batch(addresses)
    elapsed = time.time() - start
    
    print(f"Batch processing: {elapsed:.2f}s for 100 addresses")

if __name__ == "__main__":
    benchmark_single()
    benchmark_batch()