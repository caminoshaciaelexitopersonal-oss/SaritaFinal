# EVENTOS CANÓNICOS SOBERANOS

| Evento | Productor | Consumidores | Idempotency Key | Retry Policy |
|--------|-----------|--------------|-----------------|--------------|
| `financial.payment.created` | Finance API | Ledger Worker, Tax Worker | `payment_id` | Exponential Backoff (5) |
| `tourism.booking.confirmed` | Tourism API | Finance Worker, Notify Worker | `booking_id` | Fixed Retry (3) |
| `ai.agent.decision_authorized` | AI Command | Operational Worker, Auditor | `decision_id` | Instant Retry (2) |
| `infra.tenant.isolation_trigger` | Governance | All Workers, RLS Engine | `trace_id` | Infinite (Critical) |

## ESTRATEGIA DE TRAZA
Todo evento debe portar un `ContextHeader`:
- `trace_id`: ID único de la petición original.
- `correlation_id`: ID para agrupar eventos relacionados en una saga.
- `tenant_id`: ID del cliente afectado.
- `span_id`: ID del paso actual en el runtime.
