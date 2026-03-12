# Auditoría de Nomenclatura - Core ERP

Este documento certifica que el núcleo `core_erp` cumple con el estándar de nomenclatura 100% en inglés para todos sus campos y modelos, asegurando el desacoplamiento total.

## 1. Modelos Base (`apps/core_erp/base/base_models.py`)

| Clase Abstracta | Campo (Inglés) | Propósito | Estado |
| :--- | :--- | :--- | :---: |
| `BaseErpModel` | `id` | UUID v4 Identificador único | ✅ |
| | `created_at` | Timestamp de creación | ✅ |
| | `updated_at` | Timestamp de actualización | ✅ |
| `BaseAccount` | `code` | Código contable (e.g., '1105') | ✅ |
| | `name` | Nombre de la cuenta | ✅ |
| | `account_type` | Clase/Tipo de cuenta | ✅ |
| | `is_active` | Estado de habilitación | ✅ |
| `BaseJournalEntry` | `date` | Fecha del asiento | ✅ |
| | `reference` | Referencia externa/documental | ✅ |
| | `description` | Glosa o descripción | ✅ |
| | `is_posted` | Flag de contabilización definitiva | ✅ |
| `BaseAccountingTransaction` | `debit` | Valor al Debe | ✅ |
| | `credit` | Valor al Haber | ✅ |
| `BaseInvoice` | `number` | Número correlativo | ✅ |
| | `issue_date` | Fecha de emisión | ✅ |
| | `due_date` | Fecha de vencimiento | ✅ |
| | `total_amount` | Monto total de la factura | ✅ |
| | `status` | Estado del flujo comercial | ✅ |
| `BaseWarehouse` | `name` | Nombre del almacén | ✅ |
| | `location` | Ubicación física | ✅ |
| `BaseInventoryMovement` | `movement_type` | Entrada/Salida/Ajuste | ✅ |
| | `quantity` | Cantidad afectada | ✅ |
| | `date` | Fecha del movimiento | ✅ |
| | `description` | Motivo del movimiento | ✅ |
| `BaseFiscalPeriod` | `name` | Nombre del periodo | ✅ |
| | `start_date` | Fecha inicial | ✅ |
| | `end_date` | Fecha final | ✅ |
| | `is_closed` | Flag de cierre de periodo | ✅ |
| `BasePaymentOrder` | `payment_date` | Fecha programada | ✅ |
| | `amount` | Monto a pagar | ✅ |
| | `concept` | Concepto del pago | ✅ |
| | `status` | Estado de la orden | ✅ |
| `BaseBankTransaction` | `amount` | Monto transacción | ✅ |
| | `date` | Fecha y hora | ✅ |
| | `description` | Descripción | ✅ |

## 2. Motores de Negocio (`apps/core_erp/accounting/`, `billing/`)

- `AccountingEngine.validate_balance()`: Utiliza `transactions.all()`, `debit` y `credit`.
- `AccountingEngine.post_entry()`: Utiliza `is_posted`.
- `BillingEngine.calculate_totals()`: Utiliza `items.all()`, `subtotal` y `total_amount`.

## 3. Certificación de Idioma

- **Mezcla detectada:** Ninguna.
- **Idioma del Núcleo:** Inglés (UK/US standard).
- **Desacoplamiento:** Los modelos base no contienen ForeignKeys hacia `admin_plataforma` ni `prestadores`.
