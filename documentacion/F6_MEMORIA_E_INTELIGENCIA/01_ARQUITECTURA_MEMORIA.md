# Arquitectura del Sistema de Memoria y Capa de Inteligencia Adaptativa

## 1. Visión General
El Sistema de Memoria de SARITA permite que la plataforma evolucione de un motor reactivo a un sistema proactivo que aprende de sus propias decisiones, éxitos y fallos. La Capa de Inteligencia Adaptativa utiliza esta memoria para optimizar la gobernanza (MCP), la coordinación (PCA) y la ejecución (WPA).

## 2. Los 4 Niveles de Memoria

### 2.1 Memoria Operativa (Corto Plazo)
- **Propósito:** Mantener el estado inmediato de las misiones en curso.
- **Contenido:** Variables de workflow, resultados parciales de agentes, estados intermedios.
- **Persistencia:** Cache rápida (Redis) y DB Transaccional (TTL: 24h - 7 días).

### 2.2 Memoria Contextual (Por Entidad/Caso)
- **Propósito:** Entender el historial de un usuario, prestador o tipo de servicio específico.
- **Contenido:** Decisiones previas vinculadas a un UUID, patrones de comportamiento, niveles de confianza del actor.
- **Uso:** Personalización de la evaluación de riesgo por el MCP.

### 2.3 Memoria Estratégica (Histórica y Analítica)
- **Propósito:** Identificar tendencias sistémicas globales.
- **Contenido:** Métricas agregadas (Success Rate), rendimiento de agentes (Agent Accuracy), hotspots de conflictos entre agentes.
- **Uso:** Alimentar el motor de ajuste de pesos del PCA.

### 2.4 Memoria Semántica (Vectorial)
- **Propósito:** Recuperar conocimiento basado en el significado, no solo en palabras clave.
- **Contenido:** Embeddings de decisiones críticas, conflictos complejos y planes de acción exitosos.
- **Tecnología:** Vector DB (pgvector / Pinecone) + Modelos de Embedding (OpenAI/SADI).
- **Uso:** Comparación de la situación actual con "casos similares" del pasado.

## 3. Motor de Inteligencia Adaptativa (AIM)

### 3.1 Motor de Análisis de Patrones
Identifica errores repetitivos o divergencias sistemáticas en las propuestas de los agentes para alertar al MCP.

### 3.2 Motor de Ajuste Dinámico de Pesos (PCA Optimizer)
Calcula el `Performance Score` de cada agente. Si un agente consistentemente vota en contra de resultados exitosos, el motor sugiere una reducción de su peso en el consenso.

### 3.3 Motor de Predicción de Riesgo
Analiza el historial semántico para predecir si un nuevo comando tiene alta probabilidad de requerir compensación (Rollback) o generar un conflicto de gobernanza.

### 3.4 Motor de Optimización de Workflow (WPA Suggester)
Sugiere cambios en las definiciones de workflows (e.g., reducir timeouts o cambiar el orden de pasos) basándose en métricas de latencia y éxito históricas.

## 4. Gobernanza del Aprendizaje
El aprendizaje **NUNCA** es autónomo en su aplicación final.
1. El AIM genera una **Propuesta Adaptativa**.
2. El **Agente Auditor** valida la integridad de la propuesta.
3. El **MCP (Soberano)** aprueba o rechaza la aplicación de la nueva configuración o peso.
