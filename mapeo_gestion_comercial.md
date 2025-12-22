# Mapeo de Contrato de Datos: Módulo Gestión Comercial

Este documento define el contrato de datos entre el backend (fuente de verdad) y el frontend para el módulo de Gestión Comercial. El objetivo es asegurar una integración coherente y sin lógica de negocio duplicada.

## 1. FacturaVenta

Representa la factura principal.

| Campo Backend (`FacturaVenta`) | Tipo de Dato (Backend) | Uso en Frontend | Campo Frontend (Sugerido) | Tipo de Dato (Frontend) | Notas |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `id` | `AutoField` | Lectura | `id` | `number` | Identificador único. |
| `numero_factura` | `CharField` | Lectura/Escritura | `numeroFactura` | `string` | El frontend lo envía, pero el backend podría autogenerarlo. |
| `cliente` | `ForeignKey` a `Cliente` | Lectura/Escritura | `cliente` | `{ id: number; nombre: string; }` | Para la creación, el frontend enviará el `cliente_id`. Para la lectura, el backend devolverá el objeto anidado. |
| `fecha_emision` | `DateField` | Lectura/Escritura | `fechaEmision` | `string` (ISO 8601) | |
| `fecha_vencimiento` | `DateField` | Lectura/Escritura | `fechaVencimiento` | `string` (ISO 8601) | Opcional. |
| `subtotal` | `DecimalField` | **Solo Lectura** | `subtotal` | `number` | **Calculado por el backend.** |
| `impuestos` | `DecimalField` | **Solo Lectura** | `impuestos` | `number` | **Calculado por el backend.** |
| `total` | `DecimalField` | **Solo Lectura** | `total` | `number` | **Calculado por el backend.** |
| `total_pagado` | `DecimalField` | **Solo Lectura** | `totalPagado` | `number` | **Calculado por el backend.** |
| `estado` | `CharField` (Choices) | **Solo Lectura** | `estado` | `'BORRADOR' | 'ENVIADA' | 'PAGADA' ...` | **Gestionado por el backend.** |
| `items` | `ReverseForeignKey` a `ItemFactura` | Lectura/Escritura | `items` | `ItemFactura[]` | Para la creación, el frontend enviará un array de objetos `ItemFactura`. |

## 2. ItemFactura

Representa una línea de producto dentro de la factura.

| Campo Backend (`ItemFactura`) | Tipo de Dato (Backend) | Uso en Frontend | Campo Frontend (Sugerido) | Tipo de Dato (Frontend) | Notas |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `producto` | `ForeignKey` a `Producto` | Lectura/Escritura | `producto` | `{ id: number; nombre: string; }` | Para la creación, se enviará el `producto_id`. |
| `descripcion` | `CharField` | Lectura/Escritura | `descripcion` | `string` | Se puede autocompletar desde el producto, pero debe ser editable. |
| `cantidad` | `DecimalField` | Lectura/Escritura | `cantidad` | `number` | |
| `precio_unitario` | `DecimalField` | Lectura/Escritura | `precioUnitario` | `number` | Se puede autocompletar desde el producto. |
| `subtotal` | `DecimalField` | **Solo Lectura** | `subtotal` | `number` | **Calculado por el backend.** |
| `impuestos` | `DecimalField` | Lectura/Escritura | `impuestos` | `number` | El frontend puede enviar un valor (ej. 19%), el backend calcula el monto. |

## 3. Cliente

Entidad a la que se le emite la factura.

| Campo Backend (`Cliente`) | Tipo de Dato (Backend) | Uso en Frontend | Campo Frontend (Sugerido) | Tipo de Dato (Frontend) | Notas |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `id` | `AutoField` | Lectura | `id` | `number` | |
| `nombre` | `CharField` | Lectura/Escritura | `nombre` | `string` | |
| `email` | `EmailField` | Lectura/Escritura | `email` | `string` | |
| `telefono` | `CharField` | Lectura/Escritura | `telefono` | `string` | Opcional. |

## 4. Producto

El bien o servicio que se está vendiendo.

| Campo Backend (`Producto`) | Tipo de Dato (Backend) | Uso en Frontend | Campo Frontend (Sugerido) | Tipo de Dato (Frontend) | Notas |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `id` | `AutoField` | Lectura | `id` | `number` | |
| `nombre` | `CharField` | Lectura | `nombre` | `string` | |
| `sku` | `CharField` | Lectura | `sku` | `string` | |
| `precio_venta` | `DecimalField` | Lectura | `precioVenta` | `number` | El frontend debe usar este precio para autocompletar. |
| `stock_actual` | `DecimalField` | Lectura | `stockActual` | `number` | Útil para validaciones en el frontend antes de enviar. |
