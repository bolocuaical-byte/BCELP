# BCELP Backend

This directory contains the backend for BC Energy Lab Platform (BCELP).

## Run the application

From the `backend/` directory, start the server with:

```bash
uvicorn app.main:app --reload
```

The FastAPI application will be available at `http://127.0.0.1:8000`.

## Run with Docker Compose

From the `backend/` directory, build and start the services with:

```bash
docker compose up --build
```

This starts the `backend` and `postgres` services. The backend service depends on PostgreSQL and will run Alembic migrations automatically before starting FastAPI.

If you need to recreate the database:

```bash
docker compose down -v
```
## Endpoints

- `GET /` - project status and metadata
- `GET /health` - service health check
