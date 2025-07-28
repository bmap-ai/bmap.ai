.PHONY: install test run build clean

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/

run:
	uvicorn api.main:app --reload

build:
	docker build -t bmap-ai:latest .

migrate:
	python scripts/migration.py create

seed:
	python scripts/seed_data.py

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

deploy:
	bash deployment/deploy.sh