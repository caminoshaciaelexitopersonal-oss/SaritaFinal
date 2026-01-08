# Checklist de Integración del Sistema de Gestión Archivística (SGA) - FASE 11

Este documento rastrea el progreso de la integración del SGA con todos los módulos core del ERP Sarita, según la DIRECTRIZ FASE 11.

| Sistema | Módulo / Documento | Evento Disparador | Estado | Prueba de Verificación |
| :--- | :--- | :--- | :--- | :--- |
| **Piloto (Fase 10)** | `gestion_comercial` / `FacturaVenta` | `FacturacionService` en estado `ACEPTADA` | ✅ Completado | `test_facturacion_flow_triggers_archiving` |
| --- | --- | --- | --- | --- |
| **Gestión Financiera** | `gestion_financiera` / `OrdenPago` | Creación en estado `PAGADA` | ⬜ Pendiente | `test_orden_pago_triggers_archiving` |
| **Gestión Financiera** | `gestion_financiera` / `ReciboCaja` | Creación del recibo | ⬜ Pendiente | `test_recibo_caja_triggers_archiving` |
| **Gestión Comercial** | `gestion_comercial` / `OperacionComercial` (Contrato) | Cambio de estado a `CONFIRMADA` | ⬜ Pendiente | `test_contrato_triggers_archiving` |
| **Gestión Comercial** | `gestion_comercial` / `OperacionComercial` (Cotización) | Cambio de estado a `CONFIRMADA` | ⬜ Pendiente | `test_cotizacion_triggers_archiving` |
| --- | --- | --- | --- | --- |
| **G. Operativa (Genérico)** | `reservas` / `Reserva` | Creación de la reserva | ⬜ Pendiente | `test_reserva_triggers_archiving` |
| **G. Operativa (Genérico)** | `inventario` / `MovimientoInventario` | Creación del movimiento | ⬜ Pendiente | `test_movimiento_inventario_triggers_archiving` |
| **G. Operativa (Genérico)** | `clientes` / `Cliente` | Creación o actualización significativa | ⬜ Pendiente | `test_cliente_triggers_archiving` |
| --- | --- | --- | --- | --- |
| **G. Operativa (Especializado)** | `alojamientos` / `CheckIn` | Creación del registro de check-in | ⬜ Pendiente | `test_checkin_triggers_archiving` |
| **G. Operativa (Especializado)** | `restaurantes` / `Pedido` | Cierre o pago del pedido | ⬜ Pendiente | `test_pedido_restaurante_triggers_archiving` |
| **G. Operativa (Especializado)** | `eventos` / `Inscripcion` | Confirmación de la inscripción | ⬜ Pendiente | `test_inscripcion_evento_triggers_archiving` |
| **G. Operativa (Especializado)** | `transporte` / `Manifiesto` | Cierre o confirmación del manifiesto | ⬜ Pendiente | `test_manifiesto_triggers_archiving` |

---
**Leyenda de Estado:**
-   ✅ **Completado:** La integración está implementada, probada y verificada.
-   ⏳ **En Progreso:** Se está trabajando activamente en la integración.
-   ⬜ **Pendiente:** La integración aún no ha comenzado.
-   ❌ **Bloqueado:** Existe un impedimento que debe ser resuelto.
-   ⚠️ **Excluido:** Se ha decidido conscientemente excluir este flujo en esta fase (requiere justificación).
