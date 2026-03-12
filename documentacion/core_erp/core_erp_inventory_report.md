# Reporte de Inventario Técnico para Core ERP

Este reporte identifica los modelos y la lógica de negocio candidatos para la extracción hacia el núcleo `core_erp`.

## 1. Módulo: Contabilidad (Accounting)

| Modelo | Ubicación Admin | Ubicación Prestador | Candidato Extracción | Observaciones |
| :--- | :--- | :--- | :---: | :--- |
| `PlanDeCuentas` | `gestion_contable/contabilidad` | `gestion_contable/contabilidad` | Sí | Lógica idéntica de catálogo. |
| `Cuenta` | `gestion_contable/contabilidad` | `gestion_contable/contabilidad` | Sí | Estructura jerárquica duplicada. |
| `PeriodoContable` | `gestion_contable/contabilidad` | `gestion_contable/contabilidad` | Sí | Gestión de fechas y estado cerrado. |
| `AsientoContable` | `gestion_contable/contabilidad` | `gestion_contable/contabilidad` | Sí | Encabezado del libro diario. |
| `Transaccion` | `gestion_contable/contabilidad` | `gestion_contable/contabilidad` | Sí | Movimientos de Débito/Crédito. |

## 2. Módulo: Comercial y Facturación (Billing)

| Modelo | Ubicación Admin | Ubicación Prestador | Candidato Extracción | Observaciones |
| :--- | :--- | :--- | :---: | :--- |
| `OperacionComercial` | `gestion_comercial/domain` | `gestion_comercial/domain` | Sí | Registro base de venta/contrato. |
| `ItemOperacionComercial` | `gestion_comercial/domain` | `gestion_comercial/domain` | Sí | Detalle de la operación. |
| `FacturaVenta` | `gestion_comercial/domain` | `gestion_comercial/domain` | Sí | Registro legal de facturación. |
| `ItemFactura` | `gestion_comercial/domain` | `gestion_comercial/domain` | Sí | Detalle de la factura. |
| `ReciboCaja` | `gestion_comercial/domain` | `gestion_comercial/domain` | Sí | Comprobante de pago. |

## 3. Módulo: Gestión Financiera (Treasury)

| Modelo | Ubicación Admin | Ubicación Prestador | Candidato Extracción | Observaciones |
| :--- | :--- | :--- | :---: | :--- |
| `CuentaBancaria` | `gestion_financiera` | `gestion_financiera` | Sí | Gestión de saldos en bancos. |
| `OrdenPago` | `gestion_financiera` | `gestion_financiera` | Sí | Instrucciones de egreso. |

## 4. Módulo: Inventario (Inventory)

| Modelo | Ubicación Admin | Ubicación Prestador | Candidato Extracción | Observaciones |
| :--- | :--- | :--- | :---: | :--- |
| `Almacen` | `gestion_contable/inventario` | `gestion_contable/inventario` | Sí | Depósitos de mercancía. |
| `MovimientoInventario` | `gestion_contable/inventario` | `gestion_contable/inventario` | Sí | Entradas/Salidas/Ajustes. |

---

## Conclusiones del Inventario
Existe una duplicación estructural superior al 80% en los modelos base del ERP. La extracción a `core_erp` permitirá centralizar las reglas de validación contable y financiera, eliminando la deuda técnica por paridad manual.
