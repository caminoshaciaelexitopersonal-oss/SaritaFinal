# ARQUITECTURA DE RUNTIME DE AGENTES IA

## 1. AGENT EXECUTION PIPELINE
Los agentes no son solo "prompts"; son procesos activos que:
1. **Receive Task:** Desde Kafka o Temporal.
2. **Context Retrieval:** Acceso a la Memoria Cognitiva (Vector DB).
3. **Reasoning:** Inferencia mediante LLM (OpenAI, Anthropic, Local Llama).
4. **Tool Execution:** Llamada a funciones reales (ej. `update_ledger`, `send_email`).
5. **Output Generation:** Envío de resultado al Bus de Eventos.

## 2. RUNTIME SUPERVISION
Un "Supervisor Agent" monitorea las ejecuciones de los agentes tácticos para detectar:
- **Hallucinations:** Inconsistencias con el estado de la DB.
- **Infinite Loops:** Llamadas recursivas sin salida.
- **Ethics Violations:** Acciones fuera de las `sovereign_policies`.
