# INVENTARIO FUNCIONAL: DASHBOARD GUBERNAMENTAL (TORRE DE CONTROL)
**Lead Auditor:** Jules (Senior AI Software Engineer)
**Date:** March 2026

Este inventario define las capacidades que deben ser replicadas en Web, Mobile y Desktop para alcanzar la paridad funcional.

## 1. Analytics Territorial
- **Propósito:** Visualización de KPIs geográficos.
- **Widgets:**
  - Mapa regional interactivo.
  - Indicadores de usuarios, prestadores e ingresos.
- **Endpoints:** `/api/v1/governance/control-tower/analytics/`

## 2. Monitoreo de Prestadores
- **Propósito:** Supervisión del ecosistema empresarial.
- **Widgets:**
  - Tabla/Lista de prestadores con estado (Activo/Inactivo).
  - Filtros por categoría y municipio.
- **Endpoints:** `/api/v1/mi-negocio/prestadores/`

## 3. Alertas Institucionales
- **Propósito:** Detección y gestión de incidentes críticos.
- **Widgets:**
  - Lista de alertas con prioridad (Crítica, Alta, Media, Baja).
  - Detalle de incidentes IA (Auditoría de decisiones).
- **Endpoints:** `/api/v1/governance/control-tower/alerts/`

## 4. Reportes Estratégicos
- **Propósito:** Generación de documentos de impacto territorial.
- **Widgets:**
  - Selector de periodos.
  - Botones de descarga PDF/Excel.
- **Endpoints:** `/api/v1/finance/indicators/reports/`

---
**Nota:** Todos los componentes visuales residen en `@sarita/shared-ui`.
