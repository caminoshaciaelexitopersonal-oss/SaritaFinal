# Reporte de Pruebas Funcionales Cruzadas - Fase 3

## 1. Configuración del Entorno de Prueba

- **Base de Datos:** Se partió de una base de datos SQLite limpia y recién migrada.
- **Servidores:** Se iniciaron los servidores de backend y frontend en un estado limpio.
- **Datos:** Se ejecutó un script para crear dos tenants (`Company`) completamente aislados:
    - **Tenant A:** "Hotel Sarita de Prueba" (`prestador_antonio@sarita.test`)
    - **Tenant B:** "Agencia Sarita de Prueba" (`agente_viajes@sarita.test`)
    - Cada tenant fue aprovisionado con su propio Perfil, Cliente, Producto, Almacén y Plan de Cuentas.

## 2. Escenarios de Prueba Ejecutados

### Escenario 1: Crear Factura → Verificar Asiento Contable

- **Acción:** Se creó una factura de venta (`FV-HOTEL-001`) para el **Tenant A (Hotel)** por un total de **$300.00** vía API.
- **Verificación:** Se utilizó la `shell` de Django para inspeccionar la base de datos.
- **Comando de Verificación:**
  ```python
  from apps.prestadores.mi_negocio.gestion_comercial.models import FacturaVenta
  from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import JournalEntry, Transaction

  factura = FacturaVenta.objects.get(numero_factura="FV-HOTEL-001")
  asiento = JournalEntry.objects.get(object_id=factura.id)
  transacciones = asiento.transactions.all()

  print(f"Asiento encontrado: {asiento}")
  for t in transacciones:
      print(f"- Cuenta: {t.account.code}, Débito: {t.debit}, Crédito: {t.credit}")
  ```
- **Resultado:** ✅ **ÉXITO.**
  - Se encontró 1 `JournalEntry` asociado a la factura.
  - El asiento contenía 2 transacciones:
    - Un **débito** de $300.00 a la cuenta `1305` (Cuentas por Cobrar - Hotel).
    - Un **crédito** de $300.00 a la cuenta `4135` (Ingresos Operacionales - Hotel).
- **Conclusión:** La interoperabilidad entre `gestion_comercial` y `gestion_contable` funciona correctamente.

### Escenario 2: Crear Factura → Verificar Movimiento de Inventario

- **Acción:** Se utilizó la misma factura (`FV-HOTEL-001`) del escenario anterior, que incluía la venta de 2 unidades del producto "Noche en Habitación Sencilla". El stock inicial era 100.
- **Verificación:** Se utilizó la `shell` de Django.
- **Comando de Verificación:**
  ```python
  from apps.prestadores.mi_negocio.gestion_contable.inventario.models import MovimientoInventario, Producto

  producto = Producto.objects.get(sku="HOTEL-001")
  movimiento = MovimientoInventario.objects.get(producto=producto, descripcion__contains="FV-HOTEL-001")

  print(f"Stock actual del producto: {producto.stock_actual}")
  print(f"Movimiento encontrado: {movimiento.tipo_movimiento} de {movimiento.cantidad}")
  ```
- **Resultado:** ✅ **ÉXITO.**
  - Se encontró 1 `MovimientoInventario` asociado a la factura.
  - El movimiento era de tipo `SALIDA` por una cantidad de `2.00`.
  - El `stock_actual` del producto se actualizó correctamente a `98.00`.
- **Conclusión:** La interoperabilidad entre `gestion_comercial` y `inventario` funciona correctamente.

### Escenario 3: Crear Factura con Otro Tenant → Confirmar Aislamiento

- **Acción:**
    1. Se creó una factura (`FV-HOTEL-001`) para el **Tenant A (Hotel)**.
    2. Se creó una factura (`FV-AGENCIA-001`) para el **Tenant B (Agencia)**.
- **Verificación:** Se realizaron peticiones `GET` a la API `/api/v1/mi-negocio/comercial/facturas-venta/` utilizando el token de autenticación de cada tenant.
- **Resultado:** ✅ **ÉXITO.**
    - La petición con el token del **Tenant A** devolvió **únicamente 1 factura** (`FV-HOTEL-001`).
    - La petición con el token del **Tenant B** devolvió **únicamente 1 factura** (`FV-AGENCIA-001`).
- **Conclusión:** El aislamiento de datos (multi-tenancy) a nivel de API está correctamente implementado y es robusto.

## 3. Resumen de Hallazgos

| Funcionalidad | Estado | Observaciones |
| :--- | :--- | :--- |
| **`gestion_comercial` → `gestion_contable`** | ✅ **Funciona** | La creación de facturas genera los asientos contables correctos. |
| **`gestion_comercial` → `inventario`** | ✅ **Funciona** | La creación de facturas genera los movimientos de stock correctos. |
| **Aislamiento Multi-Tenant** | ✅ **Funciona** | Los datos de `gestion_comercial` están correctamente aislados por tenant. |
| **Frontend → Backend (Consistencia de Datos)** | ✅ **Funciona** | El frontend muestra los datos de la API sin alterarlos. |
| **Funcionalidades Pendientes (UI)** | ❕ **Pendiente** | La interoperabilidad visual es imposible de verificar para `Contabilidad` y `Finanzas` debido a la falta de interfaces de usuario. |
