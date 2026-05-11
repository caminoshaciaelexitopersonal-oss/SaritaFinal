# INTERACCIONES RUNTIME
**Principio:** Coreografía de Eventos y Orquestación de Sagas.

## 1. FLUJO DE PRODUCCIÓN / CONSUMO
- **Finance Runtime:** Produce `payment.settled`. Consumido por `Tourism` para confirmar reserva.
- **AI Runtime:** Consume `anomaly.detected`. Produce `decision.made` (ej: aislamiento automático).
- **Governance Runtime:** Consume `decision.made`. Ejecuta bloqueo en SQL/RLS.

## 2. MUTACIÓN DE ESTADO
- Solo el worker "Owner" de la entidad puede realizar UPDATE en la tabla correspondiente.
- Ej: Solo `financial_worker` puede tocar `finance.ledger_entries`.
- Otros dominios deben emitir un evento de "Solicitud" (`request.ledger_update`).
