# Sprint 4 — Research Management

Este documento describe los cambios realizados en el Sprint 4 para el módulo de gestión de investigaciones.

Contenido

- Endpoints CRUD para `ResearchProject` (`/projects/`).
- Endpoints CRUD para `ResearchLine` (`/research-lines/`).
- Endpoints CRUD para `ResearchGroup` (`/research-groups/`).
- Servicios (`app/services/*`) que encapsulan la lógica de persistencia.
- Tests de integración en `backend/app/tests/test_research_management.py`.

Decisiones importantes

- Se creó `ProjectService`, `ResearchLineService` y `ResearchGroupService` para mantener la lógica de negocio separada de los routers.
- Los endpoints requieren autenticación JWT (reutilizan `get_current_user`) y guardan `owner_id` automáticamente para proyectos.
- No se ejecutaron migraciones Alembic; los modelos están preparados para migraciones futuras.

Cómo probar localmente

1. Levantar servicios (Postgres + backend) con Docker Compose.

```bash
cd backend
docker compose up --build
```

2. Ejecutar tests (puede requerir una base de datos disponible):

```bash
cd backend
python -m pytest backend/app/tests/test_research_management.py -q
```

Archivos añadidos/modificados

- `backend/app/schemas/research.py` (schemas para `ResearchLine`).
- `backend/app/services/project_service.py`.
- `backend/app/services/researchline_service.py`.
- `backend/app/services/researchgroup_service.py`.
- `backend/app/api/research_lines.py`.
- `backend/app/api/research_groups.py`.
- `backend/app/tests/test_research_management.py`.
- `backend/app/api/__init__.py` (routers registrados).
- `docs/DATA_MODEL.md` (actualizado).
