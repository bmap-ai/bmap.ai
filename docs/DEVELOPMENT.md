# Development Guide

## Setup
```bash
pip install -r requirements.txt
```

## Running Tests
```bash
python scripts/run_tests.py
```

## Database Setup
```bash
python scripts/migration.py create
python scripts/seed_data.py
```

## Starting the API
```bash
uvicorn api.main:app --reload
```

## Docker Development
```bash
docker-compose up
```