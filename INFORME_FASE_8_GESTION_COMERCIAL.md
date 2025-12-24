# INFORME DE CIERRE TÉCNICO FASE 8 – MÓDULO DE GESTIÓN COMERCIAL

Este documento detalla el estado actual, la arquitectura y los contratos de API del módulo `gestion_comercial` tras la finalización de la Fase 8.

## 1. Verificación Estructural Explícita

### 1.1. Estructura de Archivos Relevante

El análisis del módulo revela que, tras la refactorización y la desactivación de componentes obsoletos, la estructura funcional principal reside en las carpetas `domain` y `presentation`.

```
gestion_comercial/
├── domain/
│   ├── __init__.py
│   └── models.py       # Define los modelos de datos principales.
├── presentation/
│   ├── __init__.py
│   ├── serializers.py  # Define los contratos de datos para la API.
│   └── views.py        # Define la lógica de los endpoints (ViewSets).
├── migrations/         # Contiene el historial de cambios de la base de datos.
├── urls.py             # Enruta las URLs a los ViewSets.
├── apps.py
└── admin.py
```

*Nota: Otros subdirectorios como `ai`, `automation`, `funnels`, `marketing`, `sales`, y `_obsoleto_bff` existen en el código base pero han sido desactivados y no forman parte de la funcionalidad operativa actual.*

### 1.2. Modelos Activos

Los siguientes modelos constituyen el núcleo del dominio de facturación:

*   **`FacturaVenta`**: Representa la cabecera de una factura, incluyendo cliente, fechas, totales y estado. Está ligada a un `ProviderProfile`.
*   **`ItemFactura`**: Representa una línea de producto o servicio dentro de una `FacturaVenta`. Apunta al modelo `Product` genérico, permitiendo facturar tanto bienes como servicios.
*   **`ReciboCaja`**: Representa un pago recibido y asociado a una `FacturaVenta`.

### 1.3. Vistas (ViewSets) Activas

Los siguientes `ModelViewSet` exponen la funcionalidad principal a través de la API:

*   **`FacturaVentaViewSet`**: Proporciona operaciones CRUD completas para las facturas. Incluye lógica de negocio para la creación de asientos contables al crear una factura.
*   **`ReciboCajaViewSet`**: Proporciona operaciones CRUD para los recibos de caja.

## 2. Endpoints y Contratos de Datos

A continuación se detallan los endpoints operativos expuestos por el módulo, listos para ser consumidos por el frontend.

### 2.1. Facturas de Venta (`FacturaVentaViewSet`)

*   **Ruta Base:** `api/v1/mi-negocio/comercial/facturas-venta/`

#### Listar Facturas (GET)
*   **Endpoint:** `/`
*   **Respuesta (BFF):** `200 OK`
    ```json
    [
        {
            "id": 1,
            "numero_factura": "F-001",
            "cliente_nombre": "Cliente de Prueba",
            "fecha_emision": "2025-12-25",
            "total": "300000.00",
            "estado": "BORRADOR",
            "estado_display": "Borrador"
        }
    ]
    ```

#### Obtener Detalle de Factura (GET)
*   **Endpoint:** `/<int:pk>/`
*   **Respuesta (BFF):** `200 OK`
    ```json
    {
        "id": 1,
        "numero_factura": "F-001",
        "cliente": { "id": 1, "nombre": "Cliente de Prueba", "email": "cliente@test.com" },
        "fecha_emision": "2025-12-25",
        "fecha_vencimiento": null,
        "subtotal": "300000.00",
        "impuestos": "0.00",
        "total": "300000.00",
        "total_pagado": "0.00",
        "estado": "BORRADOR",
        "estado_display": "Borrador",
        "items": [
            {
                "id": 1,
                "producto": "504f382a-586f-4096-aa00-d4c65128f6ff",
                "descripcion": "Estadía Navideña",
                "cantidad": "2.00",
                "precio_unitario": "150000.00",
                "subtotal": "300000.00",
                "impuestos": "0.00"
            }
        ]
    }
    ```

#### Crear Factura (POST)
*   **Endpoint:** `/`
*   **Payload de Entrada:**
    ```json
    {
        "cliente_id": 1,
        "numero_factura": "F-002",
        "fecha_emision": "2025-12-26",
        "fecha_vencimiento": "2026-01-25", // Opcional
        "items": [
            {
                "producto_id": "504f382a-586f-4096-aa00-d4c65128f6ff", // UUID del producto/servicio
                "descripcion": "Descripción del ítem",
                "cantidad": 1,
                "precio_unitario": 150000
            }
        ]
    }
    ```
*   **Respuesta:** `201 Created` con el cuerpo del objeto creado (usando `FacturaVentaWriteSerializer`).
*   **Posibles Errores:** `400 Bad Request` si los datos de entrada son inválidos o si las cuentas contables no existen.

#### Actualizar Factura (PUT/PATCH)
*   **Endpoint:** `/<int:pk>/`
*   **Payload de Entrada:** Similar a la creación.
*   **Respuesta:** `200 OK` con el cuerpo del objeto actualizado.
*   **Posibles Errores:** `400 Bad Request` si la factura está en un estado que no permite modificación (Pagada, Anulada).

#### Eliminar Factura (DELETE)
*   **Endpoint:** `/<int:pk>/`
*   **Respuesta:** `204 No Content`.

### 2.2. Recibos de Caja (`ReciboCajaViewSet`)

*   **Estado:** **INACTIVO**.
*   **Descripción:** El `ReciboCajaViewSet` existe en el código pero no está registrado en `urls.py`, por lo que no expone ningún endpoint actualmente. Su funcionalidad CRUD para gestionar pagos está presente pero no es accesible vía API.

## 3. Estado de Migraciones

El módulo `gestion_comercial` tiene un historial de migraciones claro y conciso:

*   **`0001_initial.py`**:
    *   **Propósito:** Crea los modelos iniciales `FacturaVenta`, `ItemFactura`, y `ReciboCaja`.
    *   **Observación:** En su estado inicial, `ItemFactura.producto` apuntaba incorrectamente al modelo `Producto` del módulo de inventario.

*   **`0002_alter_itemfactura_producto.py`**:
    *   **Propósito:** Corrige el campo `producto` en el modelo `ItemFactura`.
    *   **Detalle:** Altera la `ForeignKey` para que apunte al modelo `Product` genérico del módulo `prestadores` (específicamente, `gestion_operativa.modulos_genericos.productos_servicios`), permitiendo así el uso de UUIDs y la facturación de servicios.

## 4. Aislamiento Funcional y Dependencias

El análisis de las importaciones confirma que el módulo `gestion_comercial` es funcionalmente autónomo y no tiene acoplamientos con módulos obsoletos.

*   **Aislamiento:** El módulo no depende de ningún código dentro de los directorios desactivados (`_obsoleto_bff`, `ai`, `automation`, etc.). Su funcionalidad está contenida en su `domain` y `presentation`.
*   **Dependencias Externas Documentadas:** `gestion_comercial` tiene las siguientes dependencias explícitas y necesarias con otros módulos de "Mi Negocio":
    *   `api`: Para el `ProviderProfile`.
    *   `gestion_operativa`: Para los modelos `Cliente` y `Product`.
    *   `gestion_financiera`: Para el modelo `CuentaBancaria`.
    *   `gestion_contable`: Para los modelos `JournalEntry`, `Transaction`, `ChartOfAccount`, `MovimientoInventario` y `Almacen`.

Esta estructura de dependencias está alineada con la arquitectura general del sistema ERP, donde `gestion_comercial` actúa como un orquestador para operaciones de venta.
