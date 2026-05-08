# MOTOR DE ORQUESTACIÓN DISTRIBUIDA
**Tecnología Recomendada:** Temporal.io

## 1. WORKFLOWS Y SAGAS
Las operaciones complejas en SARITA (ej. "Reserva de Hotel + Pago + Comisión + Factura") se implementan como **Workflows de Temporal**.
- **Sagas:** Patrón para transacciones largas con compensación (rollback) automática si un paso falla.
- **State Management:** El estado del flujo no reside en la DB de negocio, sino en el motor de orquestación, garantizando resiliencia ante caídas de workers.

## 2. COMPENSACIÓN (ROLLBACK DISTRIBUIDO)
Si falla el paso de "Pago", el orquestador dispara automáticamente la actividad de "Cancelar Reserva" y "Notificar Usuario", manteniendo la consistencia eventual.

## 3. CONSISTENCIA
- **Event Sourcing:** Cada cambio de estado en el workflow es un evento persistido.
- **Atomicidad:** Se garantiza que todas las actividades del workflow se completen o se compensen.
