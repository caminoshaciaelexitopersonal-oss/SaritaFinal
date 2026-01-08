# FASE 12: Lista de Campos Desacoplados

Este documento lista todas las `ForeignKey` que fueron eliminadas y reemplazadas por campos de referencia `UUIDField` como parte de la refactorización arquitectónica para desacoplar los módulos core.

| Módulo | Modelo | Campo Original (Eliminado) | Campo Nuevo (Reemplazo) |
| :--- | :--- | :--- | :--- |
| **gestion_financiera** | `CuentaBancaria` | `perfil` | `perfil_ref_id` |
| **gestion_financiera** | `CuentaBancaria` | `cuenta_contable` | `cuenta_contable_ref_id` |
| **gestion_financiera** | `OrdenPago` | `perfil` | `perfil_ref_id` |
| **gestion_financiera** | `OrdenPago` | `cuenta_bancaria_origen`| `cuenta_bancaria_ref_id` |
| **gestion_financiera** | `OrdenPago` | `beneficiario_empleado` | `beneficiario` (GenericForeignKey) |
| **gestion_financiera** | `OrdenPago` | `beneficiario_tercero` | `beneficiario` (GenericForeignKey) |
| **gestion_financiera** | `OrdenPago` | `documento_archivistico`| `documento_archivistico_ref_id` |
| --- | --- | --- | --- |
| **gestion_comercial** | `OperacionComercial`| `perfil` | `perfil_ref_id` |
| **gestion_comercial** | `OperacionComercial`| `cliente` | `cliente_ref_id` |
| **gestion_comercial** | `OperacionComercial`| `documento_archivistico`| `documento_archivistico_ref_id` |
| **gestion_comercial** | `ItemOperacionComercial`| `producto` | `producto_ref_id` |
| **gestion_comercial** | `FacturaVenta` | `perfil` | `perfil_ref_id` |
| **gestion_comercial** | `FacturaVenta` | `cliente` | `cliente_ref_id` |
| **gestion_comercial** | `FacturaVenta` | `documento_archivistico`| `documento_archivistico_ref_id` |
| **gestion_comercial** | `ItemFactura` | `producto` | `producto_ref_id` |
| **gestion_comercial** | `ReciboCaja` | `perfil` | `perfil_ref_id` |
| **gestion_comercial** | `ReciboCaja` | `cuenta_bancaria` | `cuenta_bancaria_ref_id` |
| --- | --- | --- | --- |
| **gestion_operativa**| `PoliticaCancelacion`| `perfil` | `perfil_ref_id` |
| **gestion_operativa**| `Reserva` | `perfil` | `perfil_ref_id` |
| **gestion_operativa**| `Reserva` | `cliente` | `cliente_ref_id` |
| **gestion_operativa**| `Reserva` | `documento_archivistico`| `documento_archivistico_ref_id` |
| **gestion_operativa**| `ReservaServicioAdicional`| `servicio` | `servicio_ref_id` |

---
*Este documento confirma que el desacoplamiento de modelos se ha completado.*
