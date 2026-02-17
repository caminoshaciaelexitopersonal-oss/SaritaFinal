# Mapa de Dependencias Cruzadas de `ForeignKey` en Módulos Core

Este documento mapea las `ForeignKey` que cruzan los límites entre los sistemas core del ERP, identificando el acoplamiento arquitectónico que causa los conflictos de migraciones.

| App Origen | Modelo Origen | Campo `ForeignKey` | App Destino | Modelo Destino |
| :--- | :--- | :--- | :--- | :--- |
| **gestion_comercial** | `OperacionComercial` | `perfil` | `gestion_operativa` | `ProviderProfile` |
| **gestion_comercial** | `OperacionComercial` | `cliente` | `gestion_operativa` | `Cliente` |
| **gestion_comercial** | `OperacionComercial` | `documento_archivistico` | `gestion_archivistica` | `Document` |
| **gestion_comercial** | `FacturaVenta` | `operacion` | `gestion_comercial` | `OperacionComercial` |
| **gestion_comercial** | `FacturaVenta` | `perfil` | `gestion_operativa` | `ProviderProfile` |
| **gestion_comercial** | `FacturaVenta` | `cliente` | `gestion_operativa` | `Cliente` |
| **gestion_comercial** | `FacturaVenta` | `documento_archivistico` | `gestion_archivistica` | `Document` |
| **gestion_comercial** | `ItemFactura` | `producto` | `gestion_operativa` | `Product` |
| **gestion_comercial** | `ReciboCaja` | `perfil` | `gestion_operativa` | `ProviderProfile` |
| **gestion_comercial** | `ReciboCaja` | `cuenta_bancaria` | `gestion_financiera` | `CuentaBancaria` |
| --- | --- | --- | --- | --- |
| **gestion_financiera** | `CuentaBancaria` | `perfil` | `gestion_operativa` | `ProviderProfile` |
| **gestion_financiera** | `CuentaBancaria` | `cuenta_contable`| `gestion_contable`| `ChartOfAccount` |
| **gestion_financiera** | `OrdenPago` | `perfil` | `gestion_operativa` | `ProviderProfile` |
| **gestion_financiera** | `OrdenPago` | `beneficiario_empleado` | `gestion_contable` | `Empleado` |
| **gestion_financiera** | `OrdenPago` | `beneficiario_tercero` | `gestion_contable` | `Tercero` |
| **gestion_financiera** | `OrdenPago` | `documento_archivistico` | `gestion_archivistica`| `Document` |
| --- | --- | --- | --- | --- |
| **gestion_operativa** | `Reserva` | `perfil` | `gestion_operativa` | `ProviderProfile` |
| **gestion_operativa** | `Reserva` | `cliente` | `gestion_operativa` | `Cliente` |
| **gestion_operativa** | `Reserva` | `documento_archivistico` | `gestion_archivistica`| `Document` |
| **gestion_operativa** | `ReservaServicioAdicional` | `servicio` | `prestadores` | `Product` |

---
**Conclusión del Análisis:**

El mapa de dependencias revela un alto grado de acoplamiento entre los módulos:
-   `gestion_comercial` depende de `gestion_operativa`, `gestion_financiera` y `gestion_archivistica`.
-   `gestion_financiera` depende de `gestion_operativa` y `gestion_contable`.
-   `gestion_operativa` depende de `gestion_archivistica` y `prestadores` (que contiene a `gestion_operativa`).

Este nivel de interdependencia a nivel de `ForeignKey` es la causa raíz de los `NodeNotFoundError`. Para resolverlo, como indica la directriz, procederé a eliminar estas `ForeignKey` y a sustituirlas por un sistema de referencias externas.
