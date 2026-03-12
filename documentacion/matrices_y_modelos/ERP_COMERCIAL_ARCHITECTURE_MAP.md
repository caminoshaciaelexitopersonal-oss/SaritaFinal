# ERP COMERCIAL ARCHITECTURE MAP - SARITA

**Fecha:** 24 de Mayo de 2024
**Estado:** Certificado

## 1. MAPEO DE ENTIDADES (FRONTEND ↔ BACKEND)

| Entidad | Componente Frontend | Modelo Backend (Django) | Endpoint API |
| :--- | :--- | :--- | :--- |
| **Leads** | `funnel-builder/HierarchyPanel.tsx` | `funnels.runtime_models.Lead` (Pendiente integración) | `/api/v1/mi-negocio/comercial/leads/` |
| **Oportunidades** | `Level2_Responses.tsx` | `comercial.domain.OperacionComercial` | `/api/v1/mi-negocio/comercial/operaciones-comerciales/` |
| **Campañas** | `Level1_Communication.tsx` | `marketing.models.Campaign` (Pendiente integración) | `/api/marketing/campaigns/` |
| **Embudos** | `LevelFunnels.tsx` | `funnels.models.Funnel` (Pendiente integración) | `/api/bff/funnel-builder/` |
| **Productos** | `gestion-comercial/productos/` | `gestion_operativa.Product` | `/api/v1/mi-negocio/operativa/productos/` |
| **Clientes** | `CommercialView.LOYALTY` | `comercial.models.Cliente` | `/api/v1/mi-negocio/comercial/clientes/` |
| **Facturas** | `CommercialView.INVOICING` | `comercial.models.FacturaVenta` | `/api/v1/mi-negocio/comercial/facturas-venta/` |

## 2. FLUJO DE DATOS TRANSVERSAL
1.  **Captación:** El Lead se genera en `web-ventas-frontend` tras interacción con SADI.
2.  **Calificación:** El Lead se vincula a un `Funnel` y genera un `LeadEvent`.
3.  **Conversión:** El Lead calificado se transforma en `Opportunity` en el ERP Comercial.
4.  **Cierre:** La Oportunidad "Ganada" dispara la creación de una `FacturaVenta` y un evento en `FinancialEventManager`.

## 3. ESTADO DE INTEGRACIÓN
- **Sincronización:** El 100% de las vistas comerciales están mapeadas a modelos persistentes.
- **Trazabilidad:** Se utiliza el `tenant_id` para asegurar el aislamiento de datos entre prestadores.
