# Plan de Respuesta a Incidentes (IRP) - Sistema SARITA

## 1. Clasificación de Incidentes

| Nivel | Tipo | Impacto | Respuesta |
| :--- | :--- | :--- | :--- |
| **P1** | Brecha de Seguridad | Exfiltración de datos confidenciales. | Inmediata (Kill-switch activo). |
| **P2** | Fallo Crítico MCP | Sistema incapaz de autorizar comandos. | Escalado a DevOps / Admin Superior. |
| **P3** | Desviación de Agente | IA tomando decisiones fuera de umbral. | Suspensión temporal del agente y revisión PCA. |
| **P4** | Degradación | Latencia alta o errores no críticos. | Rebalanceo de infraestructura. |

## 2. Protocolo de Actuación (6 Pasos)

### Fase 1: Detección y Análisis
Monitoreo automático vía Grafana/SADI detecta anomalía (e.g., 100 REJECTS consecutivos).
Se asigna un ID de Incidente.

### Fase 2: Contención
- **Inmediata:** Aislamiento del microservicio o agente afectado.
- **Global:** El MCP activa el modo "Solo Lectura" si se sospecha compromiso de integridad.

### Fase 3: Erradicación
Identificación y eliminación de la causa raíz (parche de código, rotación de llaves, re-entrenamiento de agente).

### Fase 4: Recuperación
Restauración de servicios desde backups inmutables. Verificación de integridad de la cadena SHA-256.

### Fase 5: Post-Mortem
Reunión del Comité de Supervisión para analizar el rastro forense y ajustar el `AdaptiveEngine` para prevenir recurrencia.

## 3. Matriz de Comunicación
- **Equipo Técnico:** Slack #incident-response.
- **Usuarios/Clientes:** Portal de estado (Status Page).
- **Entidades Regulatorias:** Notificación automática en caso de brecha GDPR (dentro de las primeras 72h).
