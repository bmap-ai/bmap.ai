"""
Batch Processing Module
"""

from concurrent.futures import ThreadPoolExecutor
from .analyzer import WalletAnalyzer
import time

class BatchProcessor:
    def __init__(self, max_workers=4):
        self.max_workers = max_workers
        self.analyzer = WalletAnalyzer()
        
    def process_batch(self, addresses):
        """Process multiple addresses in parallel"""
        results = []
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = []
            for address in addresses:
                future = executor.submit(self.analyzer.analyze, address)
                futures.append((address, future))
            
            for address, future in futures:
                try:
                    result = future.result(timeout=30)
                    results.append(result)
                except Exception as e:
                    results.append({
                        "address": address,
                        "error": str(e)
                    })
        
        return results
    
    def process_large_batch(self, addresses, batch_size=100):
        """Process large batch in chunks"""
        all_results = []
        
        for i in range(0, len(addresses), batch_size):
            batch = addresses[i:i + batch_size]
            results = self.process_batch(batch)
            all_results.extend(results)
            time.sleep(1)  # Rate limiting
        
        return all_results