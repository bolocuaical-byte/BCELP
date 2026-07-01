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

## User Management Endpoints

### Authentication
- `POST /auth/token` - Get access token with form fields `username` and `password`
- `POST /auth/refresh` - Refresh access token
- `POST /auth/users` - Create a new user
- `GET /auth/me` - Get current authenticated user

### Users
- `GET /users/` - List users with optional filters `email`, `username`, `is_active`, `skip`, `limit`
- `POST /users/` - Create a user
- `GET /users/{user_id}` - Get a user by ID
- `PUT /users/{user_id}` - Update a user
- `DELETE /users/{user_id}` - Soft delete a user

### Roles
- `GET /roles/` - List roles
- `POST /roles/` - Create a role
- `GET /roles/{role_id}` - Get a role by ID
- `PUT /roles/{role_id}` - Update a role
- `DELETE /roles/{role_id}` - Delete a role

### Permissions
- `GET /permissions/` - List permissions
- `POST /permissions/` - Create a permission
- `GET /permissions/{permission_id}` - Get a permission by ID
- `PUT /permissions/{permission_id}` - Update a permission
- `DELETE /permissions/{permission_id}` - Delete a permission

## Endpoints

- `GET /` - project status and metadata
- `GET /health` - service health check
