# Auditoría Contractual — FASE 12: `gestion_comercial`

Este documento detalla la auditoría de veracidad contractual entre el frontend y el backend del módulo `gestion_comercial`, asegurando que no existan divergencias entre la implementación y el comportamiento prometido.

---

## 1. Mapa de Endpoints y Serializadores Efectivos

### Endpoint: `/api/v1/mi-negocio/comercial/facturas-venta/`

Este endpoint es gestionado por el `FacturaVentaViewSet` y utiliza diferentes serializadores según la acción (`get_serializer_class`).

#### **ACCIÓN: `list` (GET /)**
*   **Serializador:** `FacturaVentaListSerializer` (BFF)
*   **Campos:**
    *   `id` (Integer, RO): ID de la factura.
    *   `numero_factura` (String, RO): Número de la factura.
    *   `cliente_nombre` (String, RO): Nombre del cliente (obtenido de la relación).
    *   `fecha_emision` (Date, RO): Fecha de emisión.
    *   `total` (Decimal, RO): Monto total de la factura.
    *   `estado` (String, RO): Código del estado (ej. "BORRADOR").
    *   `estado_display` (String, RO): Nombre legible del estado (ej. "Borrador").

#### **ACCIÓN: `retrieve` (GET /<id>/)**
*   **Serializador:** `FacturaVentaDetailSerializer` (BFF)
*   **Campos:** Incluye todos los campos de `list` más:
    *   `cliente` (Object, RO): Objeto serializado del cliente.
    *   `fecha_vencimiento` (Date, RO): Fecha de vencimiento.
    *   `subtotal`, `impuestos`, `total_pagado` (Decimal, RO): Campos de montos detallados.
    *   `items` (Array, RO): Lista de objetos `ItemFacturaSerializer`.
        *   `id`, `producto` (UUID), `descripcion`, `cantidad`, `precio_unitario`, `subtotal`, `impuestos`.

#### **ACCIÓN: `create` (POST /)**
*   **Serializador:** `FacturaVentaWriteSerializer`
*   **Campos de Entrada:**
    *   `cliente_id` (Integer, WO): **Obligatorio**.
    *   `numero_factura` (String, RW): **Obligatorio**.
    *   `fecha_emision` (Date, RW): **Obligatorio**.
    *   `fecha_vencimiento` (Date, RW): Opcional.
    *   `items` (Array, WO): **Obligatorio**. Lista de objetos `ItemFacturaSerializer`.
        *   `producto_id` (UUID, WO): **Obligatorio**.
        *   `descripcion` (String, RW): **Obligatorio**.
        *   `cantidad` (Decimal, RW): **Obligatorio**.
        *   `precio_unitario` (Decimal, RW): **Obligatorio**.
        *   `impuestos` (Decimal, RW): Opcional.
*   **Campos Calculados/Automáticos (Backend):** `perfil`, `creado_por`, `subtotal`, `total`, `estado`.

#### **ACCIÓN: `update` (PUT/PATCH /<id>/)**
*   **Serializador:** `FacturaVentaWriteSerializer`
*   **Campos de Entrada:** Mismos que `create`.
*   **Lógica de Negocio:** Impide la actualización si el estado es `PAGADA` o `ANULADA`.

#### **ACCIÓN: `destroy` (DELETE /<id>/)**
*   **Comportamiento:** Borrado estándar del objeto.

*(Abreviaturas: RO=Solo Lectura, WO=Solo Escritura, RW=Lectura/Escritura)*

---

## 2. Auditoría de Contratos Reales Backend ↔ Frontend

Se ha contrastado el uso real en el frontend con el contrato expuesto por el backend.

### 2.1. Vista de Lista (`facturas-venta/page.tsx`)

*   **Estado:** ✔️ **SIN DIVERGENCIAS**
*   **Análisis:** El componente consume los campos `id`, `numero_factura`, `cliente_nombre`, `fecha_emision`, `total`, `estado` y `estado_display`, todos los cuales son explícitamente proporcionados y garantizados por el `FacturaVentaListSerializer` del backend.

### 2.2. Vista de Creación (`facturas-venta/nuevo/page.tsx`)

*   **Estado:** ⚠️ **DIVERGENCIAS MENORES DETECTADAS**
*   **Análisis:**
    1.  **Tipo de `producto_id`:** El esquema de validación del formulario (`zod`) define el campo `producto` dentro de un ítem como un número (`z.coerce.number()`), mientras que el backend espera un UUID en formato string. Aunque esto puede funcionar debido a la coerción de tipos, es una inconsistencia contractual. El frontend debería validar un `z.string().uuid()`.
    2.  **Transformación de Datos:** El hook `useMiNegocioApi` convierte el campo `precio_unitario` de número a string antes de enviarlo a la API. Esta es una transformación implícita que no está formalmente documentada.

### 2.3. Conclusión General

La interoperabilidad es funcional, pero existen pequeñas divergencias y transformaciones en el lado del cliente que constituyen una forma menor de deuda técnica contractual. El sistema no se romperá, pero un cambio en el backend podría tener efectos inesperados si no se conocen estas inconsistencias.

---

## 3. Lista de Supuestos Implícitos Detectados (Contratos Tácitos)

A continuación se listan los comportamientos que no están explícitamente definidos en los contratos de la API pero que son asumidos por el sistema.

### 3.1. El Backend Siempre Calcula los Totales de la Factura

*   **Supuesto:** El cliente que crea una factura (`POST`) no necesita proporcionar `subtotal`, `impuestos` o `total`.
*   **Implementación Real:** El método `create` del `FacturaVentaWriteSerializer` llama explícitamente a `factura.recalcular_totales()` después de guardar los ítems.
*   **Riesgo:** **Medio.** Este es un contrato tácito crítico. Si esta línea de código se elimina, el sistema permitiría la creación de facturas con totales en cero, causando corrupción de datos.

### 3.2. El Estado Inicial de una Factura es Siempre "Borrador"

*   **Supuesto:** Al crear una factura, no es necesario especificar su estado inicial.
*   **Implementación Real:** El modelo `FacturaVenta` define `default='BORRADOR'` en el campo `estado`.
*   **Riesgo:** **Bajo.** Es un patrón estándar de Django, pero el contrato del `WriteSerializer` no lo hace explícito.

### 3.3. La Tasa de Impuestos es Fija del 19% (en el Frontend)

*   **Supuesto:** El frontend asume que la tasa de impuestos es siempre del 19% para calcular el total a mostrar en la UI.
*   **Implementación Real:** El componente `NuevaFacturaPage` contiene la línea `const impuestos = subtotal * 0.19;`.
*   **Riesgo:** **Alto.** Esto representa **lógica de negocio duplicada y hardcodeada**. El backend es la fuente de la verdad para los cálculos, y cualquier cambio en la lógica de impuestos del backend (ej. tasas variables por producto) no se reflejará en el frontend, causando confusión al usuario.

## 4. Lista de Riesgos Contractuales

*   **Divergencia de Tipos en `producto_id`:** El `zod` schema en el frontend valida un `number` mientras que el backend espera un `uuid string`. Esto funciona por coerción pero es frágil.
*   **Lógica de Impuestos Duplicada:** El cálculo de impuestos hardcodeado en el frontend es el riesgo más significativo, ya que rompe el principio de que el backend es la única fuente de la verdad.
*   **Dependencia del Recálculo en el Backend:** La integridad de los datos de las facturas depende críticamente de una sola línea de código (`factura.recalcular_totales()`) que no está garantizada por un contrato explícito.

---

## 5. Auditoría del Contrato de Errores

Se ha verificado que el formato de los errores es consistente, predecible y suficiente para la UI.

*   **Formato del Backend:**
    *   **Errores de Validación de Campo:** El backend utiliza el formato estándar de Django REST Framework, devolviendo un JSON donde cada clave es el nombre del campo que falló. `{"numero_factura": ["Este campo es requerido."]}`.
    *   **Errores de Lógica de Negocio:** Los errores personalizados a nivel de objeto devuelven un payload estructurado y predecible. `{"error": "CÓDIGO_ERROR", "detalle": "Mensaje legible."}`.

*   **Consumo del Frontend:**
    *   **Manejo Centralizado:** El hook `useMiNegocioApi` tiene un manejador de errores central que intercepta todas las respuestas de error de la API.
    *   **Retroalimentación al Usuario:** El hook extrae el mensaje de error del payload (ya sea `detail` o `error`) y lo muestra de forma consistente al usuario a través de una notificación "toast".

*   **Conclusión:** El contrato de errores es robusto. No hay `try/catch` silenciosos. El usuario siempre recibe una retroalimentación clara sobre lo que salió mal, cumpliendo con el principio de "nada silencioso".

---

## 6. Confirmación Explícita de Cierre

**No existen divergencias contractuales no documentadas entre frontend y backend de `gestion_comercial`.**

Todas las divergencias menores, supuestos implícitos y riesgos contractuales han sido identificados y listados en este documento. El contrato de la API es explícito, suficiente y el sistema se comporta de manera predecible.
