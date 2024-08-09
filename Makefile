# Makefile for fastapi-wallet-assets
.PHONY: action

# Variables
PYTHON = python
PIP = pip
PROJECT_NAME = fastapi-wallet-assets
VENV_NAME = venv

# Add new alembic migration
add-migration:
	alembic revision -m $(name)
db-up-all:
	alembic upgrade head

run:
	$(PYTHON) -m uvicorn app.main:app --reload
	# fastapi dev app/main.py

run-live:
	$(PYTHON) -m uvicorn app.main:app --workers 2
	# fastapi run app/main.py