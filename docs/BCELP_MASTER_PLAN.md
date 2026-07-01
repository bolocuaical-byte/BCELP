# BCELP Master Plan

**Visión General**
- **Propósito**: BCELP (Battery, Charging, Electric Laboratory Platform) es una plataforma modular para gestionar proyectos de investigación, tesis, experimentos y activos de laboratorio orientada a reproducibilidad, trazabilidad y reutilización de datos.
- **Alcance**: Backend API, modelos de dominio, flujos de laboratorio y adquisición de datos; integración opcional con herramientas de IA científica y visualizaciones en el dashboard.
- **Audiencia**: administradores, investigadores, docentes, estudiantes y técnicos de laboratorio.

**Principios**
- **Modularidad**: el sistema se organiza en módulos independientes (administración, investigación, tesis, laboratorio, vehículos, baterías, instrumentos, sensores, experimentos, adquisición, reportes, dashboard). Cada módulo expone APIs claras y versiones.
- **Trazabilidad**: todo dato creado o modificado debe ser auditable (metadatos, usuario, timestamp, soft-delete y versiones cuando aplique).
- **Reproducibilidad**: los experimentos y pipelines guardan parámetros, versiones de código/datos y artefactos necesarios para reproducir resultados.
- **IA opcional**: capacidades de IA científica son complementarias; deben ser prescindibles y activadas por módulos/feature flags.
- **Datos como fuente de verdad**: los datasets, resultados de pruebas y metadatos son la referencia canónica; los reportes y dashboards se derivan de estos datos.

**Roles de usuario**
- **Administrador**: configuración global, gestión de usuarios/roles/permiso, mantenimiento de infra.
- **Investigador**: crea y gestiona proyectos, experimentos, datasets y publica resultados.
- **Docente**: gestiona tesis, supervisa estudiantes y accede a recursos docentes.
- **Estudiante**: participa en tesis y experimentos, sube resultados y reportes.
- **Técnico de laboratorio**: gestiona equipos, reservas, mantenimiento y calibraciones.

**Módulos principales**
- **Administración**: usuarios, roles, permisos, configuración.
- **Investigación**: proyectos, líneas de investigación, grupos.
- **Tesis**: gestión de tesis, estudiantes, asesores y entregables.
- **Publicaciones**: registros de artículos, conferencias y metadatos bibliográficos.
- **Laboratorio**: laboratorios físicos/virtuales, equipos, inventario, documentos.
- **Equipos**: equipos, instrumentos, sensores, calibraciones, mantenimiento y reservas.
- **Vehículos**: gestión de vehículos y archivos de telemetría (VBOX, OBD).
- **Baterías**: componentes de baterías, packs, celdas, BMS y tests asociados.
- **Instrumentos**: módulos de adquisición conectados a equipos.
- **Sensores**: sensores asociados a instrumentos con calibraciones y metadatos.
- **Experimentos**: definición de campañas, parámetros y ejecuciones.
- **Adquisición de datos**: ingest, almacenamiento y metadatos de datasets y test runs.
- **Reportes**: generación de informes reproducibles (PDF/Word), plantillas y artefactos.
- **Dashboard**: visualizaciones de estado, métricas e indicadores clave.
- **IA científica opcional**: análisis avanzado, detección de anomalías y generación de resúmenes.

**Flujo de un proyecto de investigación**
1. **Creación**: `Investigador` crea un `ResearchProject` con metas, presupuesto y miembros.
2. **Planificación**: definir `ResearchLines`, tareas y recursos (equipos, sensores, vehículos).
3. **Ejecución**: planificar experimentos, reservar equipos y ejecutar `TestRuns`.
4. **Ingesta**: datasets y metadatos se suben a `Adquisición de datos` con referencia al experimento y proyecto.
5. **Análisis**: procesar datasets (pipelines reproducibles); opcionalmente usar módulos de IA.
6. **Publicación**: generar `Report` y registrar `Publication` si procede.
7. **Archivado**: versionado de datasets y cierre del proyecto con registro de artefactos.

**Flujo de una tesis**
1. **Registro**: `Docente` o `Investigador` registra la `Thesis` y asigna `Student` y `Advisor`.
2. **Plan de trabajo**: definir entregables, experimentos y milestones.
3. **Desarrollo**: el `Student` ejecuta experimentos, sube datasets y redacta informes.
4. **Revisión**: asesores revisan entregables; se generan versiones de reportes.
5. **Defensa**: compilar artefactos, resultados y reportes; publicar resultado final.

**Flujo de laboratorio**
1. **Gestión de equipos**: `Técnico` registra equipos, instrumentos y sensores (`Equipment`, `Instrument`, `Sensor`).
2. **Calendario y reservas**: usuarios reservan equipos (`EquipmentReservation`) con detección de conflictos.
3. **Mantenimiento y calibración**: `MaintenanceRecord` y `CalibrationRecord` registran intervenciones y vigencias.
4. **Uso**: durante el uso los `Sensors` generan `TestRuns` y datasets ligados a experimentos.

**Flujo de adquisición de datos**
1. **Configuración**: definir esquema del `TestRun` (parámetros, frecuencia, canales).
2. **Ejecución**: adquisición en tiempo real por instrumentos; archivos crudos (VBOX, OBD, CSV) se registran como `Dataset`.
3. **Metadatos**: cada dataset tiene `metadata` (instrument config, firmware, calibration ids, operator).
4. **Procesado**: pipelines transforman crudos en resultados y métricas (ETL reproducible).
5. **Almacenamiento**: datasets y artefactos se almacenan y versionan; accesos quedan auditados.

**Roadmap hasta BCELP 1.0**
- **MVP (0.1)** — Infra mínima: autenticación, modelos core (users, projects, equipment, datasets), API básica, Docker dev. (0–2 meses)
- **v0.3** — Laboratory module: instruments, sensors, reservations, maintenance, basic UI prototypes, test pipelines. (2–4 meses)
- **v0.5** — Experiments & Data: full test-run model, dataset ingest, processing pipelines, report generator. (4–6 months)
- **v0.7** — Integrations: vehicle telemetry, battery test standards, extended schemas, CI for tests/migrations. (6–9 months)
- **v0.9** — Scalability & QA: load testing, storage tiering, backup, security audit, documentation complete. (9–11 months)
- **BCELP 1.0 (12 months)** — Stable API, tested workflows for research & thesis, dashboards, basic optional IA modules, release and handover.

**Reglas para futuros sprints**
- **Ticket minimal and testable**: cada sprint item debe incluir criterios de aceptación, tests unitarios y (si aplica) integración.
- **No generar migraciones sin aprobación**: las migraciones Alembic autogeneradas deben ser revisadas y ejecutadas en entorno controlado (Docker) y con respaldo.
- **Documentar cambios**: todo cambio de modelo o API requiere actualización en `docs/` y `docs/DATA_MODEL.md`.
- **Backward compatibility**: evitar breaking changes; versionar endpoints cuando necesario.
- **Feature flags**: funcionalidades experimentales (IA o integración externa) se activan vía flags y no son obligatorias.
- **Revisión de seguridad**: cualquier nuevo módulo que maneje datos sensibles debe pasar una revisión de seguridad y permisos.
- **Deploy checklist**: migrations checked, tests passed, docs updated, backup, and rollback plan.

**Conclusión**
- Este master plan guía la evolución de BCELP hacia una plataforma reproducible y trazable para la investigación experimental. Antes de añadir nuevos módulos, el equipo revisará prioridades del roadmap y validará dependencias infra/DB.

***
Archivo creado: `docs/BCELP_MASTER_PLAN.md` — actualizar según feedback.