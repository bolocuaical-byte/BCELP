# BCELP Master Architecture Document

## 1. Visión general de BCELP

BCELP (BC Energy Lab Platform) es una plataforma integral para investigación, desarrollo y explotación de soluciones energéticas avanzadas. Integra herramientas para investigación académica, desarrollo de tesis, experimentación en laboratorio, gestión de baterías y vehículos, análisis de datos, generación de reportes y soporte de IA.

## 2. Objetivo de la plataforma

El objetivo de BCELP es ofrecer un entorno colaborativo y modular que permita a científicos, estudiantes e ingenieros:

- Diseñar y ejecutar experimentos energéticos.
- Modelar y documentar proyectos de tesis e investigación.
- Gestionar datos de baterías y vehículos.
- Generar reportes técnicos y visualizaciones.
- Conectar con asistentes de IA para aprendizaje y soporte técnico.

## 3. Arquitectura general

### Frontend

- Interfaz de usuario web responsiva.
- Paneles de control para proyectos, laboratorios, baterías, vehículos y reportes.
- Visualización de datos y dashboards interactivos.
- Capacidad de autenticación y roles de usuario.

### Backend

- API RESTful construida en FastAPI.
- Separación en capas: API, servicios, datos, modelos y utilidades.
- Motor de negocio modular para futuras integraciones.
- Autenticación JWT preparada, aun no implementada.
- Manejo de excepciones globales, logging y CORS.

### Database

- Base de datos PostgreSQL como fuente de verdad.
- Estructura relacional para entidades principales.
- Soporte para migraciones con Alembic.
- Capacidad de escalar y soportar carga analítica moderada.

### Modules

- Colección de módulos especializados dentro del backend y la aplicación.
- Cada módulo encapsula su propia lógica de negocio y datos.
- Facilita la extensibilidad y el desarrollo incremental por sprints.

### AI connector

- Componente de integración con servicios de IA externa.
- Diseñado para ofrecer soporte conversacional, recomendaciones y generación de contenido.
- Debe operar como un módulo desacoplado que no es crítico para la ejecución básica.

### Reporting engine

- Motor de generación de reportes basado en datos procesados.
- Soporta salida en PDF, Excel y dashboards web.
- Enfocado en reproducibilidad y trazabilidad de resultados.

## 4. Módulos principales

### Research

- Gestión de proyectos de investigación.
- Registro de hipótesis, metodologías y bibliografía.
- Trazabilidad de cambios y versiones de investigación.

### Thesis

- Plantillas y estructura para tesis académicas.
- Control de versiones de capítulos y anexos.
- Documentación de avance y entregables.

### Laboratory

- Registro de experimentos y pruebas de laboratorio.
- Configuración de equipamiento, calibraciones y resultados.
- Control de condiciones ambientales y trazabilidad.

### Batteries

- Gestión de parámetros de baterías, celdas y packs.
- Monitoreo de ciclos, estado de salud y rendimiento.
- Soporte para ensayos de carga/descarga y análisis térmico.

### Vehicles

- Administración de flotas y vehículos energéticos.
- Registro de especificaciones, rutas y datos de consumo.
- Integración con telemetría y simulaciones de eficiencia.

### Tests / Experiments

- Plataforma para planificar y ejecutar pruebas controladas.
- Registro de entradas, resultados y evaluaciones.
- Comparación de experimentos y generación de métricas.

### Data processing

- Pipelines de ingestión, limpieza y transformación de datos.
- Normalización de resultados experimentales.
- Preparación para análisis y reportes.

### Reports

- Generación de reportes estructurados y visualizaciones.
- Exportación en formatos estándares.
- Historial de reportes y metadatos de publicación.

### AI assistant

- Módulo de asistencia para usuarios.
- Soporte en la formulación de experimentos y análisis.
- Integración futura con modelos de lenguaje y herramientas de conocimiento.

### Dashboard

- Vista unificada de métricas clave.
- Monitorización de estado del sistema y resultados.
- Acceso rápido a secciones críticas del proyecto.

## 5. Modelo de datos inicial con tablas propuestas

### Tablas principales

- `users`
  - id
  - email
  - hashed_password
  - full_name
  - is_active
  - created_at

- `projects`
  - id
  - name
  - description
  - owner_id
  - status
  - created_at
  - updated_at

- `research_items`
  - id
  - project_id
  - title
  - summary
  - methodology
  - status
  - created_at

- `thesis_documents`
  - id
  - project_id
  - chapter_title
  - content
  - version
  - created_at

- `laboratory_experiments`
  - id
  - project_id
  - name
  - description
  - start_date
  - end_date
  - status

- `battery_records`
  - id
  - experiment_id
  - pack_id
  - voltage
  - current
  - capacity
  - temperature
  - cycle_count
  - recorded_at

- `vehicle_records`
  - id
  - project_id
  - vehicle_id
  - distance
  - energy_consumption
  - recorded_at

- `test_runs`
  - id
  - experiment_id
  - run_name
  - parameters
  - results
  - status
  - executed_at

- `data_events`
  - id
  - source
  - event_type
  - payload
  - created_at

- `reports`
  - id
  - project_id
  - report_type
  - generated_by
  - generated_at
  - status
  - file_url

- `ai_requests`
  - id
  - user_id
  - prompt
  - response_summary
  - created_at
  - status

## 6. Roadmap por sprints

### Sprint 1

- Fundamentos del backend.
- Estructura básica de FastAPI.
- Endpoints de salud y metadata.
- Primeros paquetes de backend.

### Sprint 2

- Arquitectura profesional de backend.
- PostgreSQL y SQLAlchemy.
- Alembic y logging.
- Docker y Docker Compose.
- JWT-ready authentication structure.

### Sprint 3

- Documento maestro de arquitectura.
- Definición de módulos y modelo de datos inicial.
- Estándares de diseño y directrices.

### Sprint 4 (futuro)

- Implementación de autenticación.
- Primeros módulos funcionales: research, laboratory, reports.
- Integración de datos y dashboards.

### Sprint 5 (futuro)

- Conectores de AI.
- Motor de reportes completo.
- Tests end-to-end y documentación de usuario.

## 7. Reglas de diseño

### Modularidad

- El sistema debe estar organizado en módulos independientes.
- Cada módulo debe exponer APIs claras y contratos de datos.
- La implementación debe ser intercambiable y extensible.

### Trazabilidad

- Registrar el origen de datos y cada cambio significativo.
- Documentar experimentos y decisiones de diseño.
- Mantener historiales de versiones y resultados.

### Reproducibilidad

- Garantizar que los experimentos y reportes puedan reproducirse.
- Versionar configuraciones, dataflows y modelos.
- Evitar cambios irreversibles sin registro.

### No depender de IA

- La plataforma debe ser funcional sin IA.
- Los conectores de IA son asistenciales y no críticos.
- El flujo de negocio principal debe operar de forma determinista.

### Documentación obligatoria

- Cada módulo y componente debe tener documentación técnica.
- Todos los endpoints y modelos de datos deben describirse.
- La documentación debe mantenerse actualizada con el desarrollo.

## 8. APIs futuras

- Auth API
  - `POST /auth/login`
  - `POST /auth/register`
  - `POST /auth/refresh`

- Projects API
  - `GET /projects`
  - `POST /projects`
  - `GET /projects/{project_id}`
  - `PATCH /projects/{project_id}`
  - `DELETE /projects/{project_id}`

- Research API
  - `GET /research`
  - `POST /research`
  - `GET /research/{id}`

- Thesis API
  - `GET /thesis`
  - `POST /thesis`

- Laboratory API
  - `GET /experiments`
  - `POST /experiments`
  - `POST /experiments/{id}/results`

- Batteries API
  - `GET /batteries`
  - `POST /batteries`

- Vehicles API
  - `GET /vehicles`
  - `POST /vehicles`

- Reports API
  - `GET /reports`
  - `POST /reports`

- AI Assistant API
  - `POST /ai/assist`
  - `GET /ai/history`

- Dashboard API
  - `GET /dashboard/metrics`
  - `GET /dashboard/summary`

## 9. Recomendaciones técnicas

- Usar Python 3.11+ y FastAPI para baja latencia.
- Mantener la base de datos en PostgreSQL con migraciones Alembic.
- Separar la lógica de negocio de los controladores.
- Aplicar pruebas unitarias y de integración desde el inicio.
- Utilizar Docker para entornos reproducibles.
- Versionar la documentación junto al código.
- Emplear validación de datos con Pydantic v2.
- Diseñar APIs RESTful claras y consistentes.
- Priorizar seguridad, escalabilidad y robustez.
