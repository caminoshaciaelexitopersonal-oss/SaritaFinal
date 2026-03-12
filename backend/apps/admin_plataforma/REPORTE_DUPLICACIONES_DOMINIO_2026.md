# REPORTE DE DUPLICACIONES DE DOMINIO - 2026

Este reporte identifica las redundancias estructurales y lógicas entre los entornos de la Holding (Admin) y los Tenants (Mi Negocio), con el fin de consolidarlas en el núcleo `core_erp`.

## 1. INVENTARIO DE MODELOS DUPLICADOS

| Dominio | Módulo A (Admin) | Módulo B (Tenant) | Tipo de Duplicación | Acción Requerida |
| :--- | :--- | :--- | :--- | :--- |
| **Comercial** | `OperacionComercial` | `OperacionComercial` | **Total (Espejo)** | Mover lógica base a `core_erp.commercial_domain`. |
| **Comercial** | `FacturaVenta` | `FacturaVenta` | **Total (Espejo)** | Consolidar en `BaseInvoice` dentro de `core_erp`. |
| **Comercial** | `SaaSInvoice` | `FacturaVenta` | Funcional | Unificar bajo el motor de facturación de `core_erp`. |
| **Contable** | `AdminAccount` | `Cuenta` | Funcional | Heredar de `core_erp.LedgerAccount` y unificar. |
| **Contable** | `AdminJournalEntry` | `AsientoContable` | Funcional | Unificar en `core_erp.accounting_domain`. |
| **Operativo** | `Reserva` | `Reserva` | **Total (Espejo)** | Mover a `core_erp.operational_domain` como `BaseBooking`. |
| **Operativo** | `Cliente` | `Cliente` | Funcional | Centralizar en un `SharedContact` o `BasePartner` en core. |
| **SaaS** | `SaaSPlan` | `Plan` (Operativo) | Lógica | Consolidar definición de planes en `core_erp`. |

## 2. LÓGICA Y CÁLCULOS REPETIDOS

1. **Motores de Facturación:**
   - La lógica de cálculo de totales, impuestos y validación DIAN está presente en `admin_plataforma.facturacion`, `commercial_engine` y `mi_negocio.facturacion`.
   - **Riesgo:** Inconsistencia en el cálculo de impuestos y redondeo.

2. **Validación de Asientos:**
   - La validación de partida doble se repite en los sargentos contables de ambos dominios.
   - **Riesgo:** Bypass de reglas contables en uno de los dominios.

3. **Gestión de Suscripciones:**
   - La lógica de "Activo/Inactivo" basado en fechas está dispersa.
   - **Riesgo:** Doble cobro o falta de suspensión de servicios.

## 3. REGLAS DE PRICING REPLICADAS

- Los `PricingEngine` o lógica de descuentos se encuentran tanto en la venta de planes SaaS como en la venta de servicios turísticos.
- **Acción:** Centralizar en `core_erp.commercial_domain.pricing`.

---
**Auditado por Jules - Senior Software Engineer.**
