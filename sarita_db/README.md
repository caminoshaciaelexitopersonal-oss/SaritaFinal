# SARITA DB - Hardening Fase 10 (Operatividad Crítica)

## Módulos de Resiliencia Operativa

- `27_concurrency/`: Control de bloqueo transaccional mediante `pg_advisory_xact_lock`.
- `28_retry_queue/`: Gestión de reintentos y Dead Letter Queue para operaciones asíncronas.
- `29_webhooks/`: Motor de recepción de webhooks con verificación de firmas HMAC.
- `31_scheduler/`: Programador de tareas internas para mantenimiento (Conciliación, KYC).
- `26_transaction_engine/`: Orquestador atómico con soporte de `trace_id`.

## Reglas de Endurecimiento

1. **Idempotencia**: Todas las transacciones financieras requieren una referencia única.
2. **Trazabilidad**: Uso de `trace_id` para vincular eventos, asientos contables y logs.
3. **Bloqueo por Recurso**: Las operaciones sobre un agregado deben obtener un bloqueo advisory transaccional.
4. **Cumplimiento KYC**: Integración de estados de expiración y re-verificación de riesgo.
5. **Aislamiento**: Transacciones financieras aisladas mediante bloqueos preventivos.
