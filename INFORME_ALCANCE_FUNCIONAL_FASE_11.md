# Documento de Alcance Funcional y Puntos de Extensión — FASE 11

Este documento define claramente las capacidades y limitaciones del módulo `gestion_comercial` en su estado actual, y cataloga los puntos de extensión para futuras fases.

## 1. Alcance Funcional

### 1.1. Qué HACE `gestion_comercial`

*   **Gestión de Facturas (CRUD):** Proporciona endpoints de API para crear, leer, actualizar y eliminar (`CRUD`) facturas de venta (`FacturaVenta`).
*   **Integración Contable Básica:** Al crear una factura, genera automáticamente el asiento contable de la venta (ingresos vs. cuentas por cobrar).
*   **Soporte para Productos y Servicios:** El modelo `ItemFactura` está correctamente vinculado al `Product` genérico, permitiendo facturar tanto bienes físicos como servicios intangibles usando UUIDs.
*   **Multi-Tenencia:** Todas las operaciones están correctamente aisladas a nivel de `ProviderProfile`.

### 1.2. Qué NO HACE `gestion_comercial` (y por qué)

*   **Manejo de Inventario:** La lógica para actualizar el stock de inventario al crear una factura está **conscientemente desactivada**.
    *   **Razón:** La implementación anterior era incorrecta y causaba errores críticos. Se requiere una lógica más robusta para diferenciar entre productos que manejan stock y los que no (servicios).
*   **Gestión de Pagos (Recibos de Caja):** Aunque el modelo `ReciboCaja` y su `ViewSet` existen, el `ViewSet` **no está expuesto** a través de ninguna ruta de API.
    *   **Razón:** Habilitar esta funcionalidad requiere una integración más profunda con el módulo `gestion_financiera` que está fuera del alcance de esta fase de cierre.
*   **Funcionalidades de CRM Avanzado:** Módulos como `funnels`, `marketing`, `automation` y `ai` **no están operativos**.
    *   **Razón:** Pertenecen a una arquitectura anterior y requieren una refactorización completa.

## 2. Puntos de Extensión Controlados

A continuación se identifican los puntos donde futuras funcionalidades pueden ser integradas de forma controlada.

### 2.1. Conexión de Inventario

*   **Punto de Conexión:** `gestion_comercial/presentation/views.py`, método `perform_create` del `FacturaVentaViewSet`.
*   **Contrato de Integración:** Se podría añadir una lógica que itere sobre los `items` de la factura. Si un `item.producto.nature` es `'GOOD'`, se debería llamar a un servicio del módulo `inventario` para registrar la salida de stock.

### 2.2. Habilitación de Pagos (Contabilidad Avanzada)

*   **Punto de Conexión:** `gestion_comercial/urls.py`.
*   **Contrato de Integración:** Se debería registrar el `ReciboCajaViewSet` en el router de DRF. Esto expondría los endpoints CRUD para pagos, que ya tienen la lógica de integración básica con `gestion_financiera`.
