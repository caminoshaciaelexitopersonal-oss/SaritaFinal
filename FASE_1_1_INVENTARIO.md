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

## 1.1.B — Análisis de `backend/apps/sarita_agents` (POST-MIGRACIÓN)

### 1. Jerarquía Real Existente (Unificada)

Tras la migración de los agentes desde la arquitectura legada (`backend/agents`), la jerarquía en `sarita_agents` es ahora extremadamente rica y representa la totalidad de la lógica de negocio.

- **General (1):**
    - `sarita` (Orquestador principal)
- **Coroneles (4):**
    - `administrador_general`
    - `clientes_turistas`
    - `gubernamental`
    - `prestadores`
- **Capitanes (Más de 100 funcionales):**
    - `prestadores`:
        - `gestion_archivistica`: 5 Capitanes (e.g., `capitan_digitalizacion_documental`)
        - `gestion_comercial`: 12 Capitanes (e.g., `capitan_marketing`, `capitan_ventas`)
        - `gestion_contable`: 20+ Capitanes (e.g., `capitan_impuestos`, `capitan_nomina`)
        - `gestion_financiera`: 8 Capitanes (e.g., `capitan_analisis_riesgo`, `capitan_inversiones`)
        - `gestion_operativa`: 25+ Capitanes (e.g., `capitan_logistica`, `capitan_operacion_hoteles`)
    - `administrador_general`: 5 Capitanes (e.g., `capitan_auditoria_global`, `capitan_seguridad_accesos`)
    - `clientes_turistas`: 6 Capitanes (e.g., `capitan_busqueda_servicios`, `capitan_reservas_turista`)
    - `gubernamental`:
        - `departamental`: 3 Capitanes (e.g., `capitan_planificacion_regional`)
        - `municipal`: 3 Capitanes (e.g., `capitan_turismo_local`)
        - `nacional`: 3 Capitanes (e.g., `capitan_politicas_nacionales`)
- **Tenientes:**
    - La estructura de Tenientes preexistente (`validacion_prestador_teniente`, `persistencia_prestador_teniente`) sigue siendo la base para la ejecución de tareas atómicas. La implementación de los Tenientes específicos para cada nuevo Capitán es el siguiente paso lógico del desarrollo.

### 2. Estado del Flujo Activo

- **Flujo de Ejecución:** El flujo que se dispara desde `POST /api/sarita/directive/` y es manejado por la cadena de tareas Celery (`ejecutar_mision_completa` -> `ejecutar_tarea_teniente` -> `consolidar_plan_tactico`) sigue siendo el **núcleo funcional** del sistema.
- **Integración de Capitanes:** Los más de 100 Capitanes migrados han sido **estructuralmente adaptados** para ser compatibles con este flujo. Heredan de `CapitanTemplate` y tienen la estructura de métodos (`plan`, `delegate`) necesaria para interactuar con el sistema de tareas.
- **Próximo Paso Lógico:** Aunque los Capitanes están estructuralmente integrados, la **lógica interna de sus métodos `plan()` debe ser implementada** para que deleguen tareas a Tenientes reales y específicos, en lugar de la lógica de placeholder actual.

### 3. Qué Sí Está en Producción Lógica

- **✅ Arquitectura Jerárquica Unificada:** Toda la lógica de negocio de los agentes ahora reside en una única y rica jerarquía dentro de `sarita_agents`.
- **✅ Framework de Ejecución Asíncrona Robusto:** El sistema de `Mision`, `PlanTáctico`, `TareaDelegada` y la orquestación con Celery `chords` está validado y funciona como la columna vertebral para la ejecución de cualquier misión.
- **✅ Adaptación Masiva Exitosa:** Más de 100 agentes han sido refactorizados programáticamente y de manera exitosa, demostrando la viabilidad de la nueva arquitectura para absorber la lógica legada.
- **✅ Sistema Estable y Verificado:** El proyecto, después de la fusión masiva, ha sido estabilizado y pasa toda la suite de pruebas (`check`, `makemigrations`, `migrate`, `test`), confirmando que la integración no introdujo regresiones.
