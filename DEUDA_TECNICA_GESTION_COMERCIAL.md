# Auditoría de Deuda Técnica — Módulo `gestion_comercial`

Este documento cataloga los puntos identificados de deuda técnica dentro del módulo `gestion_comercial` de acuerdo con la FASE 10.

## 1. Lógica de Movimientos de Inventario Desactivada

*   **Ubicación:** `backend/apps/prestadores/mi_negocio/gestion_comercial/presentation/views.py`, dentro del método `perform_create` del `FacturaVentaViewSet`.
*   **Descripción:** El bloque de código que crea un `MovimientoInventario` al momento de generar una factura de venta ha sido comentado.
*   **Justificación de Existencia:** Esta lógica fue desactivada porque creaba un conflicto técnico. `MovimientoInventario` depende del modelo `Producto` (con ID entero) del módulo de inventario, mientras que `ItemFactura` ahora (correctamente) apunta al modelo genérico `Product` (con UUID) para soportar tanto bienes como servicios.
*   **Impacto:** Bajo. La creación de la factura y su asiento contable funcionan correctamente. El único impacto es que la venta de un bien físico no se refleja automáticamente en una disminución del stock en el módulo de inventario.
*   **Fase Futura Recomendada:** Esta lógica debe ser reimplementada en una fase futura dedicada a la "Integración Avanzada de Inventario". La nueva implementación deberá ser capaz de diferenciar entre un `Product` que es un `GOOD` (y por lo tanto requiere un movimiento de inventario) y uno que es un `SERVICE` (que no lo requiere).

## 2. Cálculo de Costo Estimado en Módulo de IA

*   **Ubicación:** `backend/apps/prestadores/mi_negocio/gestion_comercial/ai/views.py`.
*   **Descripción:** Se encontró un comentario `# TODO: Calcular costo real` en el código relacionado con la estimación de costos de interacciones de IA.
*   **Justificación de Existencia:** Este es un placeholder dejado por el desarrollador original. El módulo `ai` es parte de la funcionalidad que fue desactivada (renombrada con `_obsoleto_`) debido a que se basa en una arquitectura anterior.
*   **Impacto:** Nulo. Dado que el módulo `ai` completo está inactivo, este `TODO` no tiene ningún impacto en la funcionalidad actual del sistema.
*   **Fase Futura Recomendada:** Este `TODO` solo sería relevante si se decide reactivar y refactorizar por completo los módulos de `ai`, `funnels` y `marketing` en una futura fase de "Expansión de CRM y Marketing Automation".
