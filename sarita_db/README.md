# SARITA ERP - Gestión Contable Real (Fase 10.8)

## Mapeo del Motor Contable y Tributario

Este módulo representa la traducción física del sistema contable y tributario actualmente operativo en el backend de SARITA, garantizando persistencia inmutable y auditable.

### Estructura de Submódulos

- `01_catalogos/`: Plan Único de Cuentas (PUC) y Cuentas Contables con soporte IFRS.
- `02_configuracion/`: Ajustes de moneda base y reglas de encadenamiento de hashes.
- `03_movimientos/`: Asientos contables (Journal Entries) y líneas de detalle con soporte multi-divisa.
- `04_periodos/`: Gestión de periodos fiscales y cierres contables con auditoría de balance.
- `05_impuestos/`: Motor tributario (IVA, Retenciones, ICA) con reglas de aplicación dinámica.
- `06_conciliacion/`: Gestión de cuentas bancarias y movimientos para cuadre de libros.
- `07_analitica/`: Centros de costo y distribución de gastos.
- `08_auditoria/`: Logs forenses y registro de eventos contables automáticos.

## Reglas de Integridad Financiera

1. **Hash Chained**: Los asientos contables están encadenados mediante hashes criptográficos (`system_hash`, `previous_hash`) para evitar alteraciones retroactivas.
2. **Doble Entrada Estricta**: Cada línea de asiento debe cumplir `(debit > 0 AND credit = 0) OR (credit > 0 AND debit = 0)`.
3. **Inmutabilidad**: Una vez posteado (`is_posted = true`), un asiento no puede ser modificado ni eliminado físicamente; requiere reversión.
4. **Trazabilidad de Origen**: Todas las transacciones contables deben vincularse a un documento fuente (Factura, Pago, Nómina) vía `transaction_links`.
