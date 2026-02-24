# REPORTE DE AUDITORÍA CONTABLE (FASE 3) — 2026

## 1. IDENTIFICACIÓN DE MODELOS FINANCIEROS (FRAGAMENTACIÓN)

| Entidad | Modelo Holding (Admin) | Modelo Tenant (Mi Negocio) | Base ERP (Core) |
| :--- | :--- | :--- | :--- |
| **Plan de Cuentas** | `AdminChartOfAccounts` | `PlanDeCuentas` | `LedgerAccount` (Base) |
| **Cuenta** | `AdminAccount` | `Cuenta` | `LedgerAccount` (Base) |
| **Periodo Fiscal** | `AdminFiscalPeriod` | `PeriodoContable` | `FinancialPeriod` (Base) |
| **Asiento (Journal)** | `AdminJournalEntry` | `AsientoContable` | `BaseJournalEntry` |
| **Línea (Transaction)** | `AdminAccountingTransaction` | `Transaccion` | `BaseJournalLine` |
| **Orden de Pago** | N/A (Lógica en Service) | `OrdenPago` | `BasePaymentOrder` |
| **Presupuesto** | N/A | `Presupuesto` / `LineaPresupuesto` | N/A |
| **Crédito** | N/A | `CreditoFinanciero` | N/A |

## 2. MOTORES FINANCIEROS Y TRIGGERS
*   **`QuintupleERPService` (Admin Services):** Orquestador de impacto. Ahora desacoplado vía `EventBus`.
*   **`SargentoContable` (Mi Negocio):** Implementa la lógica de partida doble para inquilinos.
*   **`AccountingEngine` (Core ERP):** Ya existe una base en `apps/core_erp/accounting_engine.py`, pero los modelos siguen dispersos.
*   **`impact_subscribers.py` (Core ERP):** Centraliza la recepción de intenciones de impacto financiero.

## 3. DUPLICACIONES E INCONSISTENCIAS POTENCIALES
1.  **Doble Validación:** Ambos dominios (Admin/Tenant) implementan validación de balance (Debito == Credito) de forma independiente.
2.  **Naming:** Divergencia entre nombres en español (`AsientoContable`) e inglés (`JournalEntry`).
3.  **Audit Drift:** `AdminJournalEntry` tiene campos de auditoría diferentes a `AsientoContable`.
4.  **Presupuestos Aislados:** La lógica de presupuestos solo existe para Tenants, la Holding no tiene control presupuestal automatizado en el mismo núcleo.

---
**Generado por:** Jules
**Estado:** Auditoría Finalizada - Fase 3.1
