#!/bin/bash

# Deployment script for bmap.ai

echo "Starting deployment..."

# Build Docker image
docker build -t bmap-ai:latest .

# Run database migrations
python scripts/migration.py create

# Start services
docker-compose up -d

# Health check
sleep 10
curl http://localhost:8000/health

echo "Deployment complete!"