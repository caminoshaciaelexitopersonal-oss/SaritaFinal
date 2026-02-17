# Gobierno del Dominio y Evolución Controlada del Sistema

Este documento establece los principios arquitectónicos y las reglas de gobierno que rigen la evolución de este sistema. Su propósito es asegurar que el diseño se mantenga limpio, desacoplado y predecible a largo plazo.

---

### **Regla de Oro**

> **Ningún módulo puede asumir responsabilidades que no le correspondan por dominio.**

Cada módulo debe tener un propósito claro y delimitado. La lógica de negocio que no encaje en su dominio declarado debe implementarse en otro módulo o en uno nuevo, nunca forzarse donde no pertenece.

---

### Catálogo Oficial de Estados: `FacturaVenta` (`gestion_comercial`)

Este catálogo define los únicos estados válidos para una `FacturaVenta` y las transiciones permitidas.

#### Estados Válidos:
- **`BORRADOR`**: Estado inicial. La factura es mutable y no tiene validez contable ni fiscal.
- **`COMERCIAL_CONFIRMADA`**: Estado intermedio. La intención de venta ha sido confirmada. La factura se vuelve inmutable y se envía al pipeline de facturación para su procesamiento contable.
- **`ENVIADA`**: (Uso futuro) El documento contable ha sido enviado al cliente.
- **`PAGADA`**: Estado terminal. La factura ha sido saldada completamente. Es inmutable.
- **`VENCIDA`**: (Uso futuro) La fecha de vencimiento ha pasado sin que se complete el pago.
- **`ANULADA`**: Estado terminal. La factura ha sido invalidada. Es inmutable.

#### Transiciones Permitidas:
- `BORRADOR` -> `COMERCIAL_CONFIRMADA` (vía acción `confirmar/`)
- `BORRADOR` -> `ANULADA`
- `COMERCIAL_CONFIRMADA` -> `ENVIADA` (gestionado por `facturacion`)
- `ENVIADA` -> `PAGADA` (gestionado por `gestion_comercial` al registrar pagos)
- `ENVIADA` -> `VENCIDA` (gestionado por un proceso automático)

---

### Gobierno de Eventos

#### Evento: `FacturaComercialConfirmada.v1`
- **Nombre Canónico:** `factura_comercial_confirmada`
- **Versión:** `v1`
- **Publicador Único:** Módulo `gestion_comercial`, a través del `FacturaVentaViewSet` en la acción `confirmar/`.
- **Consumidores Explícitos:** Módulo `facturacion`.
- **Payload Versionado (`v1`):**
  ```json
  {
    "id_factura_comercial": "UUID",
    "perfil_id": "ID",
    "usuario_id": "ID",
    "fecha_confirmacion": "Timestamp",
    "cliente": { "id": "ID", "nombre": "String", "email": "String" },
    "items": [
      {
        "producto_id": "UUID",
        "descripcion": "String",
        "cantidad": "Decimal",
        "precio_unitario": "Decimal"
      }
    ],
    "moneda": "String"
  }
  ```
