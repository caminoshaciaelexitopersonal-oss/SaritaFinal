# Protocolo de Resolución de Conflictos y Anti-Desviación (PCA)

## 1. Detección de Conflictos
Un conflicto se detecta automáticamente cuando:
- El `Consensus Score` está en la "Zona de Incertidumbre" (0.4 - 0.6).
- Un agente con alta autoridad (Nivel 2 o 3) emite un voto que contradice la mayoría simple.
- Existe una `Divergencia Estadística` alta en los razonamientos de los agentes (detectado por NLP).

## 2. Protocolo de Resolución (Step-by-Step)

### Paso 1: Ronda de Evidencia
El PCA solicita a los agentes en conflicto que proporcionen referencias a logs, políticas o datos históricos que sustenten su decisión (`evidence_ref`).

### Paso 2: Recálculo con Pesos de Confianza
Si un agente no proporciona evidencia válida, su `confidence_score` se reduce automáticamente en un 50% para el cálculo de esa ronda.

### Paso 3: Activación del Comité Virtual (CVD)
Si el conflicto persiste tras la ronda de evidencia, el PCA invoca al **Agente Auditor** y al **Agente de Riesgo** para actuar como árbitros finales. Su decisión conjunta tiene peso de veto.

### Paso 4: Escalamiento Soberano (Humano)
Como último recurso, si la IA no logra consenso en una operación crítica, el comando se bloquea y se envía una alerta al Dashboard Administrativo para intervención humana.

## 3. Mecanismo Anti-Desviación (Systemic Guardrails)
Para prevenir el "Alucinamiento" o el compromiso de un agente, el PCA monitorea:

- **Consistencia Histórica:** Si un agente cambia drásticamente su criterio ante parámetros similares sin una razón sistémica (ej: cambio de política), se marca para revisión.
- **Desviación de Ámbito:** Si un Agente de Ventas intenta opinar con autoridad sobre Riesgo Fiscal, el PCA ignora su voto y registra el evento como una anomalía.
- **Detección de Compromiso:** Si un agente emite ráfagas de mensajes incoherentes o fuera de contrato, el PCA Broker bloquea su `agent_id` y notifica al MCP para un reinicio del servicio.

## 4. Registro Forense de Conflictos
Cada conflicto resuelto se almacena en la tabla `Conflict_Events`, incluyendo:
- Identificadores de los agentes implicados.
- El "punto de dolor" (la regla o dato que causó la discrepancia).
- La resolución final y el razonamiento del árbitro.
