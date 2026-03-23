# INVENTARIO DE AGENTES IA: SARITA PLATFORM v1.0
**Lead Architect:** Jules (Senior AI Software Engineer)
**Date:** March 2026

Este inventario documenta los agentes de IA que requieren refactorización para eliminar el acceso directo a la base de datos (violación de capas).

## 1. Agentes de Nivel 6 (Soldados)
| Agente | Función | Tablas Consultadas (Directo) |
| :--- | :--- | :--- |
| `SoldadoFacturacion` | Generación de facturas | `Factura`, `Venta`, `DetalleVenta` |
| `SoldadoInventario` | Control de stock | `InventoryItem`, `Warehouse` |
| `SoldadoNomina` | Liquidación de pagos | `Empleado`, `Contrato`, `Planilla` |
| `SoldadoReservas` | Gestión de bookings | `Reserva`, `Servicio` |
| `SoldadoTerceros` | Gestión de proveedores | `ProviderProfile`, `Tercero` |
| `SoldadoAuditoria` | Verificación de logs | `AuditLog`, `LedgerEntry` |
| `SoldadoMarketing` | Cualificación de leads | `Lead`, `Campaign` |

## 2. Agentes de Nivel 3 (Capitanes)
| Agente | Función | Tablas Consultadas (Directo) |
| :--- | :--- | :--- |
| `CapitanContable` | Orquestación contable | `JournalEntry`, `FiscalPeriod` |
| `CapitanOperativo` | Gestión de recursos | `ProcesoOperativo`, `TareaOperativa` |
| `CapitanComercial` | Estrategia de ventas | `Opportunity`, `Embudo` |

## 3. Diagnóstico Técnico
- **Total Agentes Identificados:** 33+
- **Patrón de Error:** Uso extensivo de `Model.objects.get()` y `Model.objects.filter()` dentro de la lógica del agente.
- **Riesgo:** Acoplamiento extremo que impide el escalado a microservicios y vulnera la integridad de las reglas de negocio.
