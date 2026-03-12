# MATRIZ DE RIESGOS TÉCNICOS Y ESTRATEGIA DE MITIGACIÓN

**Sistema:** SARITA
**Jurisdicción:** Nacional / Internacional

## 1. CLASIFICACIÓN DE RIESGOS

| ID | Riesgo | Probabilidad | Impacto | Estrategia de Mitigación |
| :--- | :--- | :--- | :--- | :--- |
| **R1** | Inconsistencia de Datos en Escalado Nacional | Media | Alto | Uso de UUIDs universales y sincronización asíncrona por nodos. |
| **R2** | Fallo de Gobernanza por Voz (SADI Off-line) | Baja | Alto | Fallback a interfaz visual obligatoria y procesamiento local. |
| **R3** | Desviación Ética de la IA Autónoma | Baja | Crítico | Auditoría XAI mandatoria + Revisión humana aleatoria de logs. |
| **R4** | Latencia en Decisiones de Misión Crítica | Media | Medio | Orquestación basada en Celery con priorización de colas. |
| **R5** | Incumplimiento de GDPR / AI Act (UE) | Baja | Crítico | Capa normativa adaptable por jurisdicción (Fase F-G). |

## 2. PLAN DE ACCIÓN ANTE INCIDENTES (KILL SWITCH)
En caso de detectar una anomalía operativa o violación de límites:
1. **Activación Global:** El SuperAdmin dispara el Kill Switch desde el Centro de Autonomía.
2. **Congelamiento:** Los agentes detienen la ejecución de misiones `EN_PROGRESO`.
3. **Persistencia de Evidencia:** Se genera un snapshot del estado del sistema y los logs de los últimos 5 minutos.
4. **Análisis XAI:** Se solicita a la IA una reconstrucción de la cadena de eventos que llevó al fallo.

## 3. MONITOREO DE INTEGRIDAD
Se ha implementado un servicio de **Observador Sistémico** que reporta desviaciones en:
- Tiempo de respuesta de la IA.
- Tasa de rechazo de intenciones por el Kernel.
- Volumen de intervenciones soberanas requeridas.

---
**Documento de Trabajo - Fase F-G**
