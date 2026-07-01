# BCELP Database Design

This document describes the database design for BC Energy Lab Platform (BCELP).

## Design principles

- Use UUID primary keys for global uniqueness and easier replication.
- Track `created_at`, `updated_at` for auditing.
- Soft-delete records via `is_deleted` + `deleted_at` to preserve history.
- Relational normalization for core entities; JSON fields allowed for flexible payloads.
- Alembic-ready SQLAlchemy 2.0 models.

## Tables (summary)

See `docs/ERD.md` for a visual summary and relationship map. The database contains the following logical groups:

- Authentication & Authorization: `users`, `roles`, `permissions`, association tables
- Research: `projects`, `research_lines`
- People: `researchers`, `students`, `advisors`
- Thesis: `theses`
- Laboratory: `equipment`, `inventory_items`, `maintenance_events`
- Vehicles & Telemetry: `vehicles`, `vbox_files`, `obd_files`
- Batteries: `battery_cells`, `battery_packs`, `bms`
- Experiments: `experiments`, `test_sessions`
- Datasets: `csv_datasets`
- Publications: `publications`, `authors`, `journals`
- Reports: `reports`

Each table includes a description and columns in the model docstrings under `backend/app/models`.

## Migration strategy

- Create an initial migration scaffolding using Alembic with `alembic revision --autogenerate -m "initial"` after the models are confirmed.
- Use separate migrations for refactors and additions.

## Backups and retention

- Regular logical backups (pg_dump) and point-in-time recovery when using WAL archiving are recommended.

## Notes

- The schema favors auditability and reproducibility. Sensitive data (passwords, secrets) must be stored hashed and encrypted as appropriate.
