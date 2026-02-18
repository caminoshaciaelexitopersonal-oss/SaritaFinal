# Seguridad Operativa y Observabilidad - Sistema SARITA

## 1. Stack de Observabilidad
Para garantizar la estabilidad y el rendimiento, se implementa un stack completo de monitoreo.

| Componente | Herramienta | Función |
| :--- | :--- | :--- |
| **Métricas** | Prometheus | Recolección de métricas de series temporales. |
| **Dashboards** | Grafana | Visualización centralizada de métricas y estados. |
| **Logs** | Grafana Loki / CloudWatch | Agregación y búsqueda de logs distribuidos. |
| **Trazabilidad** | OpenTelemetry + Jaeger | Seguimiento de solicitudes entre microservicios (Tracing). |
| **Alertas** | Alertmanager | Notificación de anomalías (Slack, PagerDuty). |

## 2. Métricas Clave (KPIs Técnicos)
- **Latencia:** Tiempo de respuesta (p95 < 200ms).
- **Tráfico:** Número de solicitudes por segundo (RPS).
- **Errores:** Tasa de errores 5xx (Umbral < 0.1%).
- **Saturación:** Uso de CPU y Memoria de los nodos y pods.

## 3. Seguridad Operativa Continua

### 3.1 Protección de Borde
- **AWS WAF:** Reglas contra SQL Injection, XSS y protección contra bots.
- **AWS Shield:** Protección avanzada contra ataques DDoS.

### 3.2 Detección de Amenazas
- **Amazon GuardDuty:** Análisis inteligente de amenazas basado en el comportamiento de la cuenta y la red.
- **AWS Inspector:** Escaneo automático de vulnerabilidades en las instancias EC2 y contenedores en ECR.

### 3.3 Auditoría de Cumplimiento
- **AWS Config:** Monitoreo continuo de la configuración de los recursos para asegurar que cumplen con las políticas (ej. "Todos los buckets de S3 deben ser privados").

## 4. Gestión de Incidentes
1. **Detección:** Alerta automatizada en Grafana.
2. **Triaje:** Evaluación inicial por el equipo de guardia (On-call).
3. **Resolución:** Aplicación de parches o escalado de recursos.
4. **Post-mortem:** Análisis de causa raíz (RCA) para prevenir recurrencia.

## 5. Dashboards Ejecutivos y Técnicos
- **Global Health:** Estado general de todas las regiones y servicios.
- **Financial Performance:** Métricas de transacciones y facturación en tiempo real.
- **Agent Performance:** Latencia y éxito de las misiones de IA (SADI).
