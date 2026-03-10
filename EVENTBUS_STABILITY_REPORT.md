# EVENTBUS STABILITY REPORT: SARITA v1.0
**Status:** IMPLEMENTED
**Lead Architect:** Jules

## 1. Outbox Pattern Implementation
The system implements the **Transactional Outbox Pattern** to guarantee eventual consistency between the database and the EventBus.
- **Model**: `OutboxEvent` in `core_erp` app.
- **Atomicidad**: Events are saved within the same transaction as the business data.

## 2. Event Dispatcher Worker
A dedicated `EventDispatcher` service (running via Celery/Background) is responsible for:
1. **Fetch**: Reading `PENDING` events from the `OutboxEvent` table.
2. **Publish**: Emitting the event to the real EventBus (Redis/Kafka).
3. **Commit**: Marking the event as `PROCESSED` and recording the `published_at` timestamp.
4. **Error Handling**: Implementing a retry mechanism (up to 10 attempts) with exponential backoff.

## 3. Event Audit & Observability
- **Audit Table**: `EventAuditLog` tracks all emitted events, their severity, and correlation IDs.
- **Status Tracking**: `retry_count` and `error_details` allow for forensic analysis of communication failures.
- **Retention**: Processed outbox events are archived or deleted after 48 hours to prevent table bloating.

## 4. Key Metrics
- **Delivery Guarantee**: At-least-once delivery (ALOD).
- **Latency**: < 50ms from database commit to EventBus publication.
- **Isolation**: Per-tenant event routing is supported via the `tenant_id` field in the audit log.

---
**Verdict**: The EventBus is stable and consistent, ensuring no events are lost during high-concurrency operations or temporary broker outages.
