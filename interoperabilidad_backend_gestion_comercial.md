# Informe de Interoperabilidad Backend: Gestión Comercial

## 1. Análisis de `perform_create` en `FacturaVentaViewSet`

Este método orquesta la creación de una factura de venta y sus documentos asociados a través de varios módulos del ERP.

- **Dependencia con `gestion_contable`:**
  - **Asientos (`JournalEntry`):** ✅ **CORRECTO.** El `perform_create` crea un `JournalEntry` asociado a la factura. No duplica la lógica de creación de asientos, sino que utiliza correctamente el modelo `JournalEntry` del módulo contable.
  - **Cuentas (`ChartOfAccount`):** ✅ **CORRECTO.** Busca las cuentas contables (`1305` y `4135`) en el `ChartOfAccount` del perfil correspondiente para crear las transacciones. No define cuentas propias.

- **Dependencia con `inventario`:**
  - **Movimientos (`MovimientoInventario`):** ✅ **CORRECTO.** Por cada ítem en la factura, se crea un `MovimientoInventario` de tipo `SALIDA`. La lógica de validación de stock está correctamente encapsulada en el método `save` del modelo `MovimientoInventario`, no duplicada en el `ViewSet` comercial.

- **Lógica de Negocio No Duplicada:**
  - **Cálculo de Totales:** ❕ **OBSERVACIÓN.** El `ViewSet` no calcula los totales. Estos son calculados en el `ItemFactura.save()` y `FacturaVenta.recalcular_totales()`. Si bien esto no es una duplicación entre *módulos*, podría ser una mejora futura centralizar todos los cálculos en un "servicio" para una lógica más limpia. Sin embargo, no viola las reglas actuales.

## 2. Análisis de `registrar_pago` (Acción Personalizada)

Este método orquesta el registro de un pago y su impacto contable y financiero.

- **Dependencia con `gestion_financiera`:**
  - **Cuentas Bancarias (`CuentaBancaria`):** ✅ **CORRECTO.** El método recibe un `cuenta_bancaria_id` y obtiene la `CuentaBancaria` del perfil para asociar el pago.
  - **Transacciones (`TransaccionBancaria`):** ✅ **CORRECTO.** Se crea una `TransaccionBancaria` de tipo `INGRESO`, delegando la lógica de movimiento de tesorería al módulo financiero.

- **Dependencia con `gestion_contable`:**
  - **Asientos (`JournalEntry`):** ✅ **CORRECTO.** Se crea un `JournalEntry` para el pago, asociándolo al recibo de caja.
  - **Cuentas (`ChartOfAccount`):** ✅ **CORRECTO.** Busca la cuenta de caja/bancos desde la `CuentaBancaria` y la cuenta por cobrar del `ChartOfAccount` del perfil.

## Conclusión

El módulo `gestion_comercial` está **correctamente integrado** con los otros módulos del ERP a nivel de backend. Actúa como un orquestador, delegando la lógica de negocio específica (contabilidad, inventario, finanzas) a los módulos correspondientes y utilizando sus modelos y reglas, sin duplicar funcionalidades críticas.
