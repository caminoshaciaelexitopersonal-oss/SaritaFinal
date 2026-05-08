# ARQUITECTURA DEL BUS DE EVENTOS SOBERANO
**Stack Sugerido:** Apache Kafka / Confluent
**Nivel:** Operational Runtime Real

## 1. FLUJO RUNTIME
El Bus de Eventos es el sistema circulatorio de SARITA. A diferencia de los triggers de base de datos (que son sincrónicos y locales), el Bus de Eventos permite una orquestación distribuida, asíncrona y escalable.

- **Productores:** Servicios de Dominio (Finance, ERP, Tourism), Agentes IA, Sensores de Telemetría.
- **Consumidores:** Workers de Ejecución, Agentes de Auditoría, Motores de Reacción Financiera.

## 2. TOPOLOGÍA DE TOPICS
- `sarita.finance.transactions`: Eventos de movimiento de capital, pagos y cobros.
- `sarita.tourism.bookings`: Reservas, check-ins, cancelaciones.
- `sarita.ai.decisions`: Decisiones tomadas por agentes, autorizaciones.
- `sarita.governance.policies`: Cambios en reglas, congelamiento de tenants.
- `sarita.infrastructure.telemetry`: Métricas de runtime, logs de error.

## 3. GARANTÍAS OPERACIONALES
- **Orden de Eventos:** Garantizado por `partition_key` (ej. `tenant_id` o `trace_id`).
- **Idempotencia:** Implementada mediante `message_id` único y verificación en el sumidero (Sink).
- **Retry & DLQ:** Política de reintento exponencial (backoff) con desvío a Dead Letter Queues tras 5 fallos.
