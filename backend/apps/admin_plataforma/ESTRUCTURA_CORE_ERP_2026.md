# PROPUESTA ESTRUCTURAL - FASE 2: NÚCLEO ERP COMPARTIDO (core_erp)

Para eliminar las dependencias laterales y consolidar el "cerebro" del sistema, se propone la siguiente reestructuración de `core_erp`.

## 1. ESTRUCTURA DEFINITIVA DE CARPETAS

```text
backend/apps/core_erp/
├── tenant_kernel/          # Gestión de aislamiento, jerarquía y seguridad de inquilinos
│   ├── models.py           # BaseTenant, TenantIsolationKey
│   └── services/           # TenantProvisioner
├── commercial_domain/      # Lógica de venta, contratos y suscripciones
│   ├── models/             # BaseOperation, BaseSubscription, BasePlan
│   └── pricing/            # PricingEngine, DiscountRules
├── accounting_domain/      # Contabilidad pura y motores de balance
│   ├── models/             # LedgerAccount, JournalEntry, FiscalPeriod
│   └── engine/             # AccountingEngine (Balanced Entry Validator)
├── finance_domain/         # Tesorería, flujo de caja y pagos
│   ├── models/             # BasePayment, BankAccount, PaymentOrder
│   └── engine/             # TreasuryEngine, ReconciliationEngine
├── operational_domain/     # Abstracción de procesos y recursos
│   ├── models/             # BaseBooking, BaseAsset, BaseResource
│   └── inventory/          # InventoryEngine, StockMovement
├── event_bus/              # Orquestador de comunicación asíncrona
│   ├── bus.py              # EventBus implementation
│   └── handlers/           # Global event listeners
├── base_models/            # Cimientos técnicos del sistema
│   └── base.py             # BaseErpModel (UUID, English, Audit)
└── interfaces/             # Contratos formales de servicios (Interfaces)
    ├── commercial.py       # ICommercialService
    ├── accounting.py       # IAccountingService
    └── tenant.py           # ITenantService
```

## 2. MODELOS CRÍTICOS PARA MIGRACIÓN INMEDIATA

| Modelo | Origen Actual | Destino en Core |
| :--- | :--- | :--- |
| `Company` | `apps.companies` | `tenant_kernel.BaseTenant` |
| `SaaSSubscription` | `commercial_engine` | `commercial_domain.BaseSubscription` |
| `SaaSInvoice` | `commercial_engine` | `commercial_domain.BaseInvoice` |
| `AsientoContable` | `mi_negocio.contabilidad`| `accounting_domain.JournalEntry` |
| `AdminJournalEntry`| `admin_plataforma` | `accounting_domain.JournalEntry` |
| `Reserva` | `mi_negocio.operativa` | `operational_domain.BaseBooking` |

## 3. BENEFICIOS ARQUITECTÓNICOS
- **Aislamiento de Dominio:** Las apps (admin/prestadores) solo conocen interfaces y modelos base.
- **Cero Dependencia Lateral:** Se rompe el vínculo directo entre Holding y Tenants.
- **Auditoría Unificada:** Todos los datos financieros siguen el mismo estándar de integridad.

---
**Diseño propuesto por Jules.**
