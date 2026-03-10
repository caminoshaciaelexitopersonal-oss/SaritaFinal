# Reporte de Observabilidad y Monitoreo - SARITA v1.0

## 1. Logging Estructurado (JSON)

El sistema ha sido configurado para generar logs compatibles con arquitecturas de ingesta moderna (ELK / CloudWatch).

*   **Formato**: JSON nativo vía `EnterpriseJSONFormatter`.
*   **Atributos Nucleares**:
    *   `timestamp`: ISO 8601 de alta precisión.
    *   `correlation_id`: Vínculo transaccional entre múltiples servicios.
    *   `tenant_id`: Identificación de la empresa afectada para aislamiento de logs.
    *   `source`: Archivo y línea exacta de generación.
*   **Ingesta**: Configurado para salida a `stdout` (Docker friendly) y rotación de archivos locales para auditoría de emergencia.

## 2. Monitoreo de Infraestructura y Negocio

### 2.1 Métricas Técnicas (TechnicalMonitor)
Integración con `psutil` para monitorización en tiempo real de:
*   Consumo de CPU (> 80% dispara alerta).
*   Uso de Memoria RAM (> 90% dispara alerta).
*   Latencia de API por Endpoint.

### 2.2 Torre de Control (BusinessMonitor)
Visualización de KPIs de negocio:
*   Usuarios activos en las últimas 24h.
*   Tasa de error sistémico (System Error Rate).
*   Métricas de ventas agregadas (GMV).

## 3. Sistema de Alertas

Se han definido los siguientes umbrales de alerta para el equipo de SRE:
*   **Crítica**: `error_rate > 5%` durante 5 minutos.
*   **Advertencia**: `cpu_usage > 75%` por más de 10 minutos.
*   **Forense**: Detección de rupturas de integridad en el Ledger contable (Automático).

---
**Resultado**: El sistema garantiza una visibilidad completa de su estado interno, permitiendo una respuesta reactiva y proactiva ante incidentes.
