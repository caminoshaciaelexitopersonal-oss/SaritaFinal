# ARQUITECTURA OFFLINE MOBILE - SARITA
**Objetivo:** Garantizar la soberanía operativa de la aplicación móvil en zonas rurales sin conexión.

## 1. COMPONENTES DEL SISTEMA
- **SQLite Local:** Base de datos de alta velocidad para persistencia inmediata.
- **SyncSargento:** Orquestador de la cola de transacciones inmutable.
- **shared-sdk (SyncService):** Capa de comunicación con el backend para reconciliación.

## 2. INTEGRIDAD DE DATOS (CADENA SHA-256)
Cada operación móvil se registra siguiendo un patrón de ledger:
1. Se genera un `transaction_id` único.
2. Se captura el `hash` de la transacción anterior.
3. Se genera el `hash` actual firmando el payload + timestamp + metadata.
4. Cualquier alteración manual del SQLite local rompería la cadena de firmas, invalidando la sincronización.

## 3. FLUJO DE SINCRONIZACIÓN
- **Modo Offline:** La app guarda en la tabla `offline_transactions`.
- **Detección de Red:** Al recuperar señal, el `SyncSargento` recorre la cola en orden cronológico.
- **Idempotencia:** El backend valida el `transaction_id` para evitar duplicidad si el paquete de confirmación se pierde.

## 4. MÓDULOS CUBIERTOS
- Reservas Turísticas.
- Pagos POS Móvil.
- Registro de Visitantes.
- Firmas de Consentimiento.

**Resultado:** Operatividad 100% resiliente y auditable.
