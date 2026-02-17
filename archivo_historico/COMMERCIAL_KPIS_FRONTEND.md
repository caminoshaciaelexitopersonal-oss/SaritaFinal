# COMMERCIAL KPIS FRONTEND - SARITA

**Fecha:** 24 de Mayo de 2024
**Estado:** Certificado

## 1. INDICADORES DE RENDIMIENTO (KPIs)
| Métrica | Origen de Dato | Visualización |
| :--- | :--- | :--- |
| **Conversion Rate** | `/api/dashboard/analytics/` | Dashboard Principal ERP |
| **Ticket Promedio** | `/api/dashboard/analytics/` | Dashboard Principal ERP |
| **Ventas por Periodo** | `/api/v1/mi-negocio/comercial/facturas-venta/` | Resumen de Facturación |
| **Estado del Pipeline** | `/api/bff/sales/opportunities/` | Kanban View (Level 2) |
| **Leads Activos** | `/api/v1/mi-negocio/comercial/leads/` | Hierarchy Panel |

## 2. SEGMENTACIÓN VISUAL
- **ROI Sistémico:** Visualizado en el "Monitor de Salud del Ecosistema" (Vía 1), con impacto directo de las ventas en Vía 2.
- **Trazabilidad de Ingresos:** Cada factura emitida en el frontend es sumada automáticamente a los ingresos del periodo en el dashboard comercial.

## 3. INTEGRACIÓN FINANCIERA
- **Eventos:** El cierre de una oportunidad ("Ganada") dispara visualmente el flujo de facturación, el cual genera un evento económico real que actualiza los KPIs financieros globales.
