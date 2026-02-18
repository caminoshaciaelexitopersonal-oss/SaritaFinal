# Arquitectura Detallada del Núcleo MCP (Main Control Platform)

## 1. Visión del MCP
El Marco de Control Principal (MCP) es el cerebro estratégico del Sistema SARITA. Su función no es la ejecución operativa, sino la orquestación, validación y autorización de todas las acciones que impactan el estado del sistema.

## 2. Los 6 Pilares del MCP

### 2.1 Módulo de Recepción (Command Gateway)
Es la única puerta de entrada para comandos críticos.
- **Validación de Esquema:** Asegura que el comando cumpla con el formato JSON-Schema definido.
- **Autenticación y Firma:** Verifica que el emisor sea legítimo y que el mensaje no haya sido alterado (Hmac/SHA-256).
- **Asignación de ID Global:** Genera un UUID v4 que rastreará la solicitud en todo el ecosistema.

### 2.2 Motor de Evaluación Estratégica
Determina si una acción es "segura" y "pertinente".
- **Análisis de Impacto:** Evalúa qué módulos serán afectados.
- **Consulta de Agentes:** Invoca al Agente de Riesgo y al Agente de Cumplimiento.
- **Plan de Acción:** Genera una secuencia de pasos aprobados para la orquestación.

### 2.3 Motor de Orquestación
Ejecuta el Plan de Acción.
- **Gestión de Workflows:** Soporta flujos secuenciales (Saga Pattern) y paralelos.
- **Control de Transacciones:** Asegura que si un paso falla, se activen los mecanismos de compensación (Rollback).
- **Timeouts y Reintentos:** Maneja la resiliencia ante fallos temporales de red o servicios.

### 2.4 Módulo de Supervisión de Agentes
Actúa como el "tribunal" de la IA.
- **Detección de Conflictos:** Si dos agentes (e.g., SADI vs Auditor) discrepan, activa el protocolo de consenso.
- **Análisis de Consistencia:** Verifica que las respuestas de los agentes sean coherentes con el estado actual del sistema.

### 2.5 Módulo de Auditoría Total (Shadow Ledger)
Registro inmutable de la verdad.
- **Encadenamiento SHA-256:** Cada log contiene el hash del anterior, creando una cadena de custodia.
- **Persistencia de Intenciones:** Guarda no solo lo que pasó, sino lo que se *intentó* hacer.

### 2.6 Módulo de Gestión de Riesgo (The Kill-Switch)
Vigilancia activa en tiempo real.
- **Bloqueo Preventivo:** Capacidad de detener una ejecución si el nivel de riesgo detectado supera el umbral permitido.
- **Limites Dinámicos:** Ajusta la autoridad de los agentes según el contexto (e.g., modo de emergencia).

## 3. Principio de No-Delegación
El MCP puede delegar la *ejecución* a los microservicios (PCA), pero nunca delega la *autoridad final*. Cada paso crítico del PCA debe ser re-validado o supervisado por el MCP.
