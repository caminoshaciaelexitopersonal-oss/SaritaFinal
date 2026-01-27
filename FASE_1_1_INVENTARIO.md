# INFORME DE INVENTARIO - FASE 1.1

## 1.1.A — Análisis de `backend/apps/sadi_agent`

### Tabla de Componentes

| Archivo | Rol | ¿Se ejecuta? | ¿Quién lo llama? | Depende de LLM | ¿Rompe si se comenta? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `voice_orchestrator.py` | Orquestador de Voz | ✅ Sí | Se instancia en `management/commands/run_voice_flow_from_audio.py` y `run_voice_command.py` para pruebas. | ❌ No (indirectamente) | ✅ Sí |
| `security.py` | Seguridad (RBAC voz) | ✅ Sí | `VoiceOrchestrator` | ❌ No | ✅ Sí |
| `semantic_engine.py` | Motor Semántico | ✅ Sí | `VoiceOrchestrator` | ❌ No | ✅ Sí |
| `translation_service.py` | Servicio de Traducción | ✅ Sí | `VoiceOrchestrator` | ❌ No | ✅ Sí |
| `voice_providers.py` | Tool (Abstracción STT/TTS) | ✅ Sí | `VoiceOrchestrator` | ❌ No | ✅ Sí |
| `agent.py` | Agente Autónomo | ✅ Sí | Tarea Celery `run_agent_execution` | ❌ No (indirectamente) | ❓ Probablemente |
| `planner.py` | Planner | ✅ Sí | `Agent` | ✅ Sí (OpenAI) | ✅ Sí |
| `executor.py` | Executor | ✅ Sí | `Agent` | ❌ No | ✅ Sí |
| `tasks.py` | Tarea Celery | ✅ Sí | Se dispara desde un `ViewSet` (hoy roto) o manualmente. | ❌ No (indirectamente) | ✅ Sí |
| `tool.py` / `tool_registry.py` | Tool (Definición) | ✅ Sí | `Agent` / `Executor` | ❌ No | ✅ Sí |
| `views.py` / `urls.py` | Vista (API) | ❌ **NO (ROTO)** | Nadie (La URL está rota por `NameError`) | ❌ No | ❌ No |
| `models.py` | Persistencia | ✅ Sí | `VoiceOrchestrator`, `Agent`, Tareas Celery, etc. | ❌ No | ✅ Sí |

### Notas Adicionales:
- **Flujo Principal:** El componente central es el `VoiceOrchestrator`. Este orquesta un flujo de "Voz a Misión": recibe audio, lo transcribe, lo normaliza, entiende la intención, verifica permisos y, si todo es correcto, **delega la ejecución a la API de `sarita_agents`**.
- **Agente Autónomo vs. Orquestador:** `sadi_agent` contiene **dos sistemas conceptualmente distintos**:
    1.  El **Orquestador de Voz**, que es el flujo principal y activo.
    2.  Un **Agente Autónomo** (`agent.py`, `planner.py`, `executor.py`), que parece ser un sistema experimental o heredado. Este agente es invocado por la tarea Celery `run_agent_execution`, pero su `ViewSet` correspondiente está actualmente roto y desconectado del flujo principal.
- **Punto de Falla:** El archivo `urls.py` (y su `views.py` asociado) está **roto e inoperativo** debido a una referencia a un `AgentExecutionViewSet` inexistente. Esto rompe cualquier comando de `manage.py` si no se deshabilita temporalmente.

## 1.1.B — Análisis de `backend/apps/sarita_agents`

### 1. Jerarquía Real Existente

- **General (1):**
    - `sarita` (Orquestador principal)
- **Coroneles (4):**
    - `administrador_general`
    - `clientes_turistas`
    - `gubernamental`
    - `prestadores`
- **Capitanes (1 funcional + 1 dummy):**
    - `prestadores` -> `onboarding_prestador_capitan`
- **Tenientes (2 funcionales + 1 dummy):**
    - `prestadores` -> `validacion_prestador_teniente`
    - `prestadores` -> `persistencia_prestador_teniente`

### 2. Flujos Activos

- **Flujo Principal:** `Onboarding de Prestadores`
    - **API que lo dispara:** `POST /api/sarita/directive/` (manejada por `DirectiveView`).
    - **Tarea Celery que lo ejecuta:**
        1.  `ejecutar_mision_completa` (inicia el proceso).
        2.  El `CapitanOnboardingPrestador` planifica y crea un `PlanTáctico`.
        3.  Se disparan N tareas `ejecutar_tarea_teniente` (una por cada teniente, ej. `validacion` y `persistencia`) en un `chord` de Celery.
        4.  `consolidar_plan_tactico` se ejecuta como *callback* del `chord` para finalizar el plan.
        5.  `finalizar_mision` se ejecuta para guardar el resultado final de la misión.
    - **Misión completa que realiza:** Recibe una directiva para registrar un nuevo prestador, lo valida y (simula) su persistencia en la base de datos, manteniendo un registro de auditoría completo.

### 3. Qué Sí Está en Producción Lógica

- **✅ Arquitectura Jerárquica:** El sistema de General, Coronel, Capitán y Teniente está implementado y es funcional.
- **✅ Ejecución Asíncrona con Celery:** El flujo de delegación de tareas a los tenientes a través de Celery `chords` es el núcleo del sistema y está activo.
- **✅ Persistencia y Auditoría de Misiones:** Los modelos `Mision`, `PlanTáctico`, `TareaDelegada` y `RegistroDeEjecucion` están implementados y registran cada paso del proceso.
- **✅ Flujo Vertical de Onboarding de Prestadores:** El caso de uso para registrar un nuevo prestador es el único "slice" vertical completamente implementado, desde la API hasta la ejecución de los tenientes.
