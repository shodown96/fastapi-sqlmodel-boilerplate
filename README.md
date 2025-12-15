# FastAPI Boilerplate

A minimal and opinionated FastAPI boilerplate for building scalable, production-ready APIs.

## Features
- FastAPI with async support
- Structured project layout
- Pydantic models for validation
- Dependency injection
- Environment-based configuration
- Automatic interactive API docs (Swagger & ReDoc)

## Getting Started

### 1. Install dependencies
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the server
```bash
fastapi dev main.py
```

## Docs
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

## Todos
Switch to SQLAlchemy