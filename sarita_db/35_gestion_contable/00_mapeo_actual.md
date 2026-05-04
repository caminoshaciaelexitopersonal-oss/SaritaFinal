# Mapeo Actual del Sistema Contable SARITA

## Modelos Identificados en el Backend

### Módulo Core ERP (`apps/core_erp/accounting/models.py`)
- **ChartOfAccounts**: Define los planes de cuentas por tenant.
- **Account**: Cuentas contables con código, nombre, tipo, saldo inicial y mapeos IFRS.
- **FiscalPeriod**: Periodos de tiempo para segregación contable.
- **JournalEntry**: Cabecera de asiento contable (asociado a periodo, usuario, evento financiero). Soporta encadenamiento de hashes e inmutabilidad.
- **LedgerEntry**: Líneas de detalle (débito/crédito) vinculadas a asientos.
- **AccountingAuditLog**: Registro forense de acciones sobre la contabilidad.

### Módulo de Impuestos (`apps/core_erp/taxation/models.py`)
- **Country / Jurisdiction**: Definición territorial fiscal.
- **Tax**: Definición de impuestos (IVA, Retenciones, ICA).
- **TaxRate**: Tasas vigentes por periodo.
- **TaxRule**: Reglas de aplicación basadas en tipo de documento y entidad.
- **TaxTransaction**: Registro de impacto fiscal por documento.
- **TaxAccountMapping**: Vinculación de impuestos con cuentas del PUC.

## Flujos de Datos Detectados

1. **Ventas -> Contabilidad**: Las facturas generadas en `core.invoices` disparan la creación de un `JournalEntry` con sus respectivas `LedgerEntry` (Ingreso vs Cuentas por Cobrar/Impuestos).
2. **Pagos -> Contabilidad**: El registro de un pago en `core.payments_erp` genera asientos de movimiento de caja/banco vs cuentas por cobrar.
3. **Validación de Integridad**: El sistema actual ya implementa una lógica de `immutable_signature` y `system_hash` que encadena los asientos contables para evitar alteraciones retroactivas.
4. **Nivel de Aislamiento**: Multi-tenant estricto basado en `tenant_id`.

## Mapeo a Estructura Física (sarita_db)

- `01_catalogos`: Traduce `ChartOfAccounts` y `Account`.
- `03_movimientos`: Traduce `JournalEntry` y `LedgerEntry`.
- `04_periodos`: Traduce `FiscalPeriod`.
- `05_impuestos`: Traduce el módulo de `taxation`.
- `08_auditoria`: Traduce `AccountingAuditLog`.
