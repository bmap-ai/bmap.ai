"""
Bundle Detection Module
"""

class BundleDetector:
    def __init__(self, min_size=3):
        self.bundles = []
        self.min_size = min_size
        
    def detect(self, wallets):
        """Detect wallet bundles"""
        # Simple clustering for now
        if len(wallets) >= self.min_size:
            return [wallets[:self.min_size]]
        return []