"""
Basic Usage Example
"""

import sys
sys.path.append('..')
from core.analyzer import WalletAnalyzer

def main():
    # Initialize analyzer
    analyzer = WalletAnalyzer()
    
    # Example wallet address
    address = "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb0"
    
    # Analyze wallet
    result = analyzer.analyze(address)
    
    # Print results
    print(f"Wallet: {result['address']}")
    print(f"Risk Score: {result['risk_score']:.2f}")
    print(f"Patterns: {result.get('patterns', [])}")
    print(f"Transaction Count: {result['tx_count']}")

if __name__ == "__main__":
    main()