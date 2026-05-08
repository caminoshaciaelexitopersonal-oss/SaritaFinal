# STACK DE OBSERVABILIDAD REAL
**Componentes:**
- **Métricas:** Prometheus + VictoriaMetrics (Long-term storage).
- **Logs:** Grafana Loki.
- **Traces:** OpenTelemetry + Tempo / Jaeger.
- **Visualización:** Grafana Dashboards.

## 1. TRACING DISTRIBUIDO
Cada operación en SARITA viaja con un `trace_id` (OpenTelemetry). Esto permite ver el camino de un evento desde el WPC Funnel, pasando por Kafka, hasta el Worker de IA y el Ledger Financiero.

## 2. ANOMALY DETECTION
Un servicio de telemetría procesa los flujos de métricas buscando desviaciones estándar en latencia o tasas de error para disparar el "Crisis Mode" del Super Admin automáticamente.
