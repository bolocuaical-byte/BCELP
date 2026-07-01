# BCELP Backend

This directory contains the backend for BC Energy Lab Platform (BCELP).

## Run the application

From the `backend/` directory, start the server with:

```bash
uvicorn app.main:app --reload
```

The FastAPI application will be available at `http://127.0.0.1:8000`.

## Endpoints

- `GET /` - project status and metadata
- `GET /health` - service health check
