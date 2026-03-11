# INVENTARIO: SISTEMA DE REPORTES ANALÍTICOS (WEB SOURCE)
**Lead Implementer:** Jules (Senior AI Software Engineer)
**Date:** March 2026

Este documento desglosa el estado actual del sistema de reportes en Web para ser replicado en Mobile y Desktop.

## 1. Datasets Identificados (Backend Core)
- **Turismo:** Atractivos más visitados, flujo por municipio, calificación promedio.
- **Economía:** GMV Regional, MRR/ARR SaaS, Recaudación por impuestos.
- **Prestadores:** Distribución por categoría, estado de RNT, cumplimiento de capacitaciones.
- **Operativo:** Reservas activas, ocupación hotelera, alertas de integridad.

## 2. Métricas y KPIs (Control Tower)
- `DAILY_REVENUE` (Financial)
- `DAILY_NET_PROFIT` (Financial)
- `EBITDA` / `BURN_RATE` (Strategic)
- `SYSTEMIC_RISK` (Technical)
- `AVG_USAGE_RATE` (Operational)

## 3. Capacidades de Visualización
- **Tablas:** Ranking de prestadores, log de transacciones.
- **Gráficos:** Torta (Roles), Barras (Categorías), Líneas (Registros en el tiempo).
- **Widgets:** KPI Cards con tendencia.

## 4. Filtros Disponibles
- Periodo (Fecha inicio/fin).
- Territorio (Municipio/Zona).
- Categoría de Prestador.
- Severidad de Alerta (para reportes de riesgo).

## 5. Formatos de Exportación (Requeridos)
- **PDF:** Reporte institucional formal.
- **Excel:** Análisis de datos crudos.
- **CSV:** Integración con sistemas externos.

---
**Gap Analysis:**
- **Mobile:** Requiere simplificación de gráficos (recharts -> nativo o simplificado) y enfoque en KPIs.
- **Desktop:** Requiere integración con el motor de exportación local y visualización de gran densidad de datos.
