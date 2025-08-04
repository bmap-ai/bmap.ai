# Architecture Overview

## System Components

### Core Layer
- **WalletAnalyzer**: Main analysis orchestrator
- **PatternRecognizer**: Pattern detection engine
- **BundleDetector**: DBSCAN-based clustering
- **RiskScorer**: Risk assessment module
- **NeuralNetwork**: Deep learning model

### API Layer
- **FastAPI**: REST API framework
- **WebSocket**: Real-time updates
- **Authentication**: API key management
- **Rate Limiting**: Request throttling

### Data Layer
- **PostgreSQL**: Primary database
- **Redis**: Caching layer
- **SQLAlchemy**: ORM

### Infrastructure
- **Docker**: Containerization
- **Kubernetes**: Orchestration
- **Prometheus**: Monitoring
- **nginx**: Reverse proxy

## Data Flow
1. Request → API → Analyzer
2. Analyzer → Pattern Detection
3. Pattern Detection → Risk Scoring
4. Risk Scoring → Response