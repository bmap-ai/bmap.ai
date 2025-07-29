# API Documentation

## Base URL
```
http://localhost:8000
```

## Endpoints

### GET /health
Health check endpoint

### POST /analyze/{address}
Analyze a wallet address

### GET /wallets/{address}
Get wallet information

### GET /transactions
Get recent transactions

## Authentication
Include API key in header:
```
X-API-Key: your-api-key
```