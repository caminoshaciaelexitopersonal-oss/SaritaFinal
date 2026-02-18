# Dashboard Operativo de Workflows (WPA)

Para garantizar la observabilidad total, el sistema WPA provee una interfaz de monitoreo en tiempo real para administradores y auditores.

## 1. Métricas en Tiempo Real (Live View)
- **Active Workflows:** Número de instancias en estado `RUNNING`.
- **Success Rate:** Porcentaje de workflows completados vs iniciados (24h).
- **Average Execution Time:** Tiempo medio por cada tipo de workflow.
- **Compensation Rate:** Porcentaje de workflows que requirieron Rollback.

## 2. Mapa de Calor de Fallos (Failure Heatmap)
Visualización que identifica qué pasos específicos o microservicios están causando la mayoría de las interrupciones, permitiendo el mantenimiento proactivo.

## 3. Vista Forense de Instancia
Al seleccionar un `workflow_instance_id`, el dashboard muestra:
- **Timeline:** Grafo visual con el progreso de cada paso.
- **Logs Técnicos:** Salida detallada de cada `StepExecution`.
- **Input/Output:** Datos procesados en cada etapa.
- **Compensation Trail:** Seguimiento de las acciones de reversión en caso de fallo.

## 4. Controles de Emergencia (Intervención MCP)
El dashboard permite al administrador realizar acciones manuales autorizadas por el MCP:
- **Kill Instance:** Detiene inmediatamente un workflow en ejecución.
- **Force Rollback:** Inicia la compensación manual.
- **Retry Step:** Fuerza el reintento de un paso fallido tras corregir un error externo.
- **Resume Instance:** Reanuda un workflow en estado `WAITING`.

## 5. Alertas Automatizadas
- Notificación vía Slack/Email si un workflow crítico entra en estado `COMPENSATING`.
- Alerta roja si una compensación (Rollback) falla, requiriendo intervención humana inmediata.
