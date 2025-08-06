# Deployment Guide

## Prerequisites
- Docker
- Kubernetes (optional)
- PostgreSQL
- Redis

## Quick Start

### Using Docker Compose
```bash
docker-compose up -d
```

### Manual Deployment

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set environment variables:
```bash
export DATABASE_URL=postgresql://user:pass@localhost/bmap
export REDIS_URL=redis://localhost:6379
```

3. Run migrations:
```bash
python scripts/migration.py create
```

4. Start the application:
```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

## Production Deployment

### Kubernetes
```bash
kubectl apply -f deployment/kubernetes.yaml
```

### Monitoring
- Prometheus metrics available at `/metrics`
- Health check at `/health`

## Scaling
- Horizontal scaling via load balancer
- Database read replicas for high traffic
- Redis cluster for distributed caching