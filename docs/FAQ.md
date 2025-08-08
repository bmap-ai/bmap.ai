# Frequently Asked Questions

## General

### What is bmap.ai?
bmap.ai is an AI-powered blockchain wallet analysis platform that detects patterns, assesses risks, and identifies transaction bundles.

### What blockchains are supported?
Currently Ethereum and EVM-compatible chains.

## Technical

### What ML models are used?
- Random Forest for classification
- DBSCAN for clustering
- Neural networks for pattern recognition
- Isolation Forest for anomaly detection

### How accurate is the risk scoring?
Our models achieve 92% accuracy on test datasets.

## API

### How do I get an API key?
Contact support or use the authentication endpoint.

### What are the rate limits?
Default: 100 requests per minute per API key.

## Troubleshooting

### API returns 500 error
Check database connection and logs.

### High memory usage
Enable Redis caching and optimize batch sizes.