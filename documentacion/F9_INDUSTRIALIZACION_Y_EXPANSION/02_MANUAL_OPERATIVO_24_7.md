# Manual Operativo 24/7 y Gestión de Incidentes

Este manual define los protocolos para la operación continua, segura y resiliente del Sistema SARITA.

## 1. NOC (Network Operations Center)
El NOC es el centro de vigilancia permanente del sistema.

### 1.1 Funciones Principales
- Monitoreo de dashboards globales (Fase 8).
- Gestión de alertas tempranas de seguridad y rendimiento.
- Ejecución de protocolos de failover manual si falla el automático.
- Coordinación de ventanas de mantenimiento.

### 1.2 Estructura de Turnos
- Cobertura 24/7/365 en tres turnos rotativos (8 horas).
- Solapamiento de 30 minutos para transferencia de contexto y misiones activas.

## 2. Clasificación de Incidentes por Severidad

| Severidad | Descripción | Tiempo Respuesta (SLA) | Escalamiento |
| :--- | :--- | :--- | :--- |
| **P1 - Crítico** | Interrupción total o brecha de seguridad. | < 15 min | CTO / Súper Admin |
| **P2 - Alto** | Degradación significativa o fallo en región activa. | < 1 hora | Arquitectura Core |
| **P3 - Medio** | Fallo en funcionalidad no crítica o agente desviado. | < 4 horas | Líder de DevOps |
| **P4 - Bajo** | Dudas operativas o sugerencias de mejora. | < 24 horas | Soporte N1 |

## 3. Protocolo de Gestión de Incidentes (IM)

1. **Detección:** Alerta automatizada o reporte de usuario.
2. **Triaje:** Clasificación de severidad y asignación de ID de incidente.
3. **Comunicación Inicial:** Notificación en portal de estado (Status Page).
4. **Resolución:** Ejecución del IRP (Fase 7) para contener y erradicar.
5. **Validación:** Confirmación de que el servicio ha vuelto a sus SLOs.

## 4. Gestión de Problemas y Postmortems
Cada incidente P1 o P2 requiere un informe **Blameless Postmortem** dentro de las 72 horas siguientes a la resolución.

### Estructura del Postmortem:
- **Resumen:** Qué pasó y cuál fue el impacto.
- **Timeline:** Cronología exacta desde la detección hasta la recuperación.
- **Causa Raíz (5 Whys):** Identificación del fallo profundo (técnico, humano o de IA).
- **Acciones Preventivas:** Tareas técnicas para evitar que el problema se repita.
- **Integración con Fase 6:** Alimentación de los hallazgos al motor adaptativo para ajustar riesgos.

## 5. Ventanas de Mantenimiento
- **Preventivo:** Programado los domingos de 02:00 a 04:00 UTC.
- **Emergencia:** Autorizado por el MCP tras validación de riesgo alto.
- **Zero-Downtime Deploy:** Se priorizan los Rolling Updates (Fase 2) para evitar interrupciones.
