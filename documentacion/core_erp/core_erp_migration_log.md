# Log de Migración - Core ERP

Registro histórico de la extracción de componentes desde los dominios específicos hacia el núcleo compartido.

## 1. Extracción de Modelos (Mapping Table)

| Concepto | Origen (Admin/Prestador) | Destino (Core ERP) | Renombrado (De -> A) |
| :--- | :--- | :--- | :--- |
| Cuenta Contable | `Cuenta` | `BaseAccount` | `codigo` -> `code`, `nombre` -> `name`, `tipo` -> `account_type`, `activa` -> `is_active` |
| Asiento Contable | `AsientoContable` | `BaseJournalEntry` | `fecha` -> `date`, `descripcion` -> `description`, `contabilizado` -> `is_posted` |
| Transacción | `Transaccion` | `BaseAccountingTransaction` | `debito` -> `debit`, `credito` -> `credit` |
| Factura | `FacturaVenta` | `BaseInvoice` | `numero_factura` -> `number`, `fecha_emision` -> `issue_date`, `fecha_vencimiento` -> `due_date`, `total` -> `total_amount`, `estado` -> `status` |
| Periodo Fiscal | `PeriodoContable` | `BaseFiscalPeriod` | `nombre` -> `name`, `fecha_inicio` -> `start_date`, `fecha_fin` -> `end_date`, `cerrado` -> `is_closed` |
| Almacén | `Almacen` | `BaseWarehouse` | `nombre` -> `name`, `ubicacion` -> `location` |
| Movimiento | `MovimientoInventario` | `BaseInventoryMovement` | `cantidad` -> `quantity`, `fecha` -> `date`, `descripcion` -> `description` |
| Orden Pago | `OrdenPago` | `BasePaymentOrder` | `fecha_pago` -> `payment_date`, `monto` -> `amount`, `concepto` -> `concept`, `estado` -> `status` |

## 2. Consolidación de Lógica

- **Validación de Balance:** Movida desde `ContabilidadService` y `SargentoContable` a `AccountingEngine.validate_balance`.
- **Cálculo de Totales:** Movida desde modelos `FacturaVenta` a `BillingEngine.calculate_totals`.
- **Registro Definitivo:** Toda operación de "posteo" financiero ahora debe invocar a los Engines del Core.

## 3. Resolución de Dependencias

- Se eliminaron las ForeignKeys directas en el Core.
- Los dominios heredan de las clases abstractas y añaden el campo `provider` (inquilino) o `organization`.
- Se implementó `CORE_ERP_VERSION = "1.0.0"` con guardia en `AppConfig.ready()`.
