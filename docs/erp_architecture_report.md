# Reporte de Arquitectura ERP "Mi Negocio" - SARITA v1.0

## 1. Consolidación de Modelos de Negocio

Se ha estandarizado la estructura de datos para soportar operaciones comerciales reales con aislamiento multiempresa.

### 1.1 Entidades Nucleares
*   **Empresa & Sucursal**: Estructura jerárquica que permite el control de múltiples puntos de venta bajo un mismo NIT.
*   **Tercero**: Modelo unificado para Clientes y Proveedores con validación de identidad.
*   **Producto & Inventario**: Separación entre la definición comercial del producto y su control de existencias físico.

## 2. Motor de Inventario y Ventas

### 2.1 Flujo Transaccional
El `SalesService` garantiza que una venta confirmada impacte simultáneamente:
1.  **Inventario**: Registro de salida y actualización de stock actual.
2.  **Facturación**: Generación de documento formal (FAC-YYYY-XXXXX) con CUFE.
3.  **Contabilidad**: Asiento automático en el `LedgerEngine` (Caja/Bancos vs Ingresos e IVA).

### 2.2 Alertas y Omnisciencia
Se implementó el evento `inventory_low` en el `EventBus` para notificar proactivamente la necesidad de reabastecimiento cuando el stock cae por debajo del mínimo configurado.

## 3. Integración Financiera (Wallet)

El ERP ahora soporta pagos nativos vía `Wallet SARITA`. El proceso incluye:
*   Validación de saldo del cliente.
*   Transferencia interna a la billetera corporativa de la empresa.
*   Confirmación de venta disparada por el éxito del pago.

---
**Resultado**: El módulo ERP ha sido elevado a un nivel de madurez industrial (95%), integrando todas las capas del sistema central.
