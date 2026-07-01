# Sprint 5 — Digital Laboratory

Objetivo

Construir el módulo de Laboratorio Digital para BCELP que modele equipos, instrumentos y sensores, además de soportar registros de calibración, mantenimiento, reservas y documentos asociados.

Contenido implementado

- Modelos SQLAlchemy añadidos/actualizados en `backend/app/models/lab.py`:
  - `Instrument`, `Sensor`, `CalibrationRecord`, `MaintenanceRecord`, `EquipmentReservation`, `EquipmentDocument`.
  - `Equipment` ampliado con `model`, `manufacturer`, `instruments`, `documents`.
- Schemas Pydantic en `backend/app/schemas/lab.py` para lectura/creación de Equipment, Instrument, Sensor y registros.
- Servicios en `backend/app/services/`:
  - `laboratory_service.py` — CRUD para `Laboratory`.
  - `equipment_service.py` — CRUD para `Equipment` y helpers para instrumentos/sensores.
- Endpoints CRUD:
  - `GET/POST/PUT/DELETE /equipment/` (`backend/app/api/equipment.py`).
  - Labs helpers remain in `backend/app/api/labs.py`.
- Tests básicos en `backend/app/tests/test_digital_lab.py`.

Notas importantes

- No se generaron migraciones Alembic (por instrucción).
- No frontend añadido en este sprint.

Cómo probar

1. Levantar servicios con Docker Compose (si usas Postgres):

```bash
cd backend
docker compose up --build
```

2. Ejecutar tests (requiere entorno y DB según configuración):

```bash
cd backend
python -m pytest backend/app/tests/test_digital_lab.py -q
```

Futuras mejoras

- Endpoints para `Instrument`, `Sensor`, `CalibrationRecord` y `EquipmentReservation`.
- Subida/gestión segura de `EquipmentDocument` con almacenamiento en S3/MinIO.
- Reservas con detección de conflictos y notificaciones.
