# FASE 1: Análisis y Plan de Reubicación de Agentes

Este documento resume los hallazgos de las Fases 1.0 a 1.3 de la directriz oficial.

---

## FASE 1.1.A — INVENTARIO DE `backend/apps/sadi_agent`

| Archivo | Rol Principal | ¿Se ejecuta? | ¿Quién lo llama? | ¿Depende de OpenAI / LLM? | ¿Rompe el sistema si se comenta? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `voice_orchestrator.py` | **Orquestador Central de Voz** | **Sí** | `management/commands/run_voice_...` | **Sí** (Whisper para STT, OpenAI para TTS) | **Sí**, es el núcleo del flujo de voz. |
| `agent.py` | **Agente Autónomo** | **Sí** | `tasks.py` (Tarea Celery) | No directamente, pero usa `Planner`. | **Sí**, rompe el flujo de agente autónomo. |
| `planner.py` | **Planner (Planificador)** | **Sí** | `agent.py` | **Sí**, usa un LLM de OpenAI para generar planes. | **Sí**, el agente no puede generar planes. |
| `executor.py` | **Executor (Ejecutor)** | **Sí** | `agent.py` | No | **Sí**, el agente no puede ejecutar planes. |
| `tasks.py` | **Iniciador de Tareas Asíncronas** | **Sí** | (Invocado por el broker de Celery) | No | **Sí**, es el punto de entrada para el agente autónomo. |
| `security.py` | **Seguridad (RBAC para Voz)** | **Sí** | `voice_orchestrator.py` | No | **Sí**, el flujo de voz no tendría validación de permisos. |
| `semantic_engine.py` | **Motor Semántico (simple)** | **Sí** | `voice_orchestrator.py` | No | **Sí**, no se podría interpretar la intención del usuario. |
| `voice_providers.py` | **Tool (Abstracción de Voz)** | **Sí** | `voice_orchestrator.py` | **Sí** (Contiene las implementaciones) | **Sí**, no habría conexión con los servicios de voz. |
| `management/commands/*`| **Puntos de Entrada** | **Sí** | `manage.py` | No directamente (invocan al orquestador) | **Sí**, son los iniciadores del flujo de voz. |
| `views.py` | Vista (Vacío) | No | N/A | No | No, está vacío y documentado como obsoleto. |
| `models.py` | Modelos de Datos | Sí | (Usado por el ORM de Django) | No | **Sí**, toda la persistencia de la app fallaría. |
| `urls.py` | Rutas URL | Probablemente no | (Framework Django) | No | Probablemente no, parece ser un remanente. |

---

## FASE 1.1.B — INVENTARIO DE `backend/apps/sarita_agents`

### 1. Jerarquía Real Existente

*   **General (1):**
    *   `SaritaOrchestrator` (El punto de entrada que delega misiones).
*   **Coroneles (1 de 4 Activo):**
    *   `PrestadoresCoronel` (✅ Activo).
    *   `AdministradorGeneralCoronel` (❌ Inactivo, comentado).
    *   `ClientesTuristasCoronel` (❌ Inactivo, comentado).
    *   `GubernamentalCoronel` (❌ Inactivo, comentado).
*   **Capitanes (1 Activo):**
    *   `OnboardingPrestadorCapitan` (✅ Activo, maneja el alta de nuevos prestadores).
*   **Tenientes (2 Activos):**
    *   `TenienteValidacionPrestador` (✅ Activo, valida los datos de un prestador).
    *   `TenientePersistenciaPrestador` (✅ Activo, guarda el prestador en la base de datos).

### 2. Flujos Activos

*   **Misión:** `Onboarding de Prestadores`.
*   **API que lo dispara:** `POST /api/sarita/directive/`.
*   **Celery Tasks que lo ejecutan:** `ejecutar_mision_completa`, `ejecutar_tarea_teniente`, `consolidar_plan_tactico`, `finalizar_mision`.
*   **Descripción del Flujo:** Un patrón asíncrono robusto donde una directiva API crea una Misión, delegada por la cadena de mando (General -> Coronel -> Capitán). El Capitán define un plan con Tenientes, ejecutados en paralelo vía Celery, con un callback que consolida los resultados.

### 3. ¿Qué está en "Producción Lógica"?

*   **Onboarding de Prestadores:** ✅
*   **Ejecución de Planes Tácticos Asíncronos:** ✅
*   **Auditoría y Persistencia de Misiones:** ✅

---

## FASE 1.2 — ANÁLISIS COMPARATIVO (`backend/agents` vs. `sarita_agents`)

| Criterio | `backend/agents` (Antigua) | `backend/apps/sarita_agents` (Nueva) | Conclusión |
| :--- | :--- | :--- | :--- |
| **Jerarquía** | Estructura completa General -> Coronel -> Capitán. | Estructura esquelética General -> Coronel -> Capitán. | Misma estructura, diferente completitud. |
| **Coroneles** | 4 dominios definidos. | 4 dominios, solo 1 (`prestadores`) activo. | La antigua parece tener todos los dominios implementados. |
| **Capitanes** | **Extremadamente rica.** El Coronel `prestadores` tiene 5 sub-directorios de Capitanes, con `gestion_comercial` conteniendo **12 capitanes** especializados. | **Extremadamente simple.** El Coronel `prestadores` tiene solo **1 capitán** (`onboarding_prestador`). | La antigua es órdenes de magnitud más rica y granular. |
| **Funcionalidad** | Cubre estrategias complejas (marketing, ventas, CRM). Los capitanes son orquestadores. | Cubre un único proceso táctico y lineal (validar y guardar). El capitán es un ejecutor. | La funcionalidad de la antigua **no ha sido migrada**. |

**Veredicto:** La arquitectura en `backend/agents` es, sin lugar a dudas, órdenes de magnitud más completa, específica y rica funcionalmente. GANA EL ANTIGUO.

---

## FASE 1.3 — PLAN DE REUBICACIÓN

**Principio Rector:** Reubicar y adaptar la rica lógica de negocio de `backend/agents` en la infraestructura de ejecución robusta y asíncrona de `backend/apps/sarita_agents`.

**Decisión por Agente Antiguo:**

| Agente / Estructura Antigua | Decisión | Justificación |
| :--- | :--- | :--- |
| `coroneles/prestadores/` | ✅ **Trasladar Luego** | El Coronel de la nueva app es un esqueleto. Se debe trasladar la lógica del antiguo. |
| `capitanes/gestion_comercial/` (y sus 12 capitanes) | ✅ **Trasladar Luego** | Lógica de negocio crítica ausente en la nueva app. |
| `capitanes/gestion_archivistica/` | ✅ **Trasladar Luego** | Lógica de negocio crítica ausente en la nueva app. |
| `capitanes/gestion_contable/` | ✅ **Trasladar Luego** | Lógica de negocio crítica ausente en la nueva app. |
| `capitanes/gestion_financiera/` | ✅ **Trasladar Luego** | Lógica de negocio crítica ausente en la nueva app. |
| `capitanes/gestion_operativa/` | ✅ **Trasladar Luego** | Lógica de negocio crítica ausente en la nueva app. |

**Estrategia de Transición:**

1.  **Reubicación Física:** Mover la estructura completa de directorios de los Capitanes antiguos a la nueva app.
2.  **Adaptación Técnica:**
    *   Hacer que los Capitanes hereden de `CapitanTemplate`.
    *   Adaptar sus métodos para que usen los modelos (`Mision`, `PlanTáctico`) y Celery.
    *   Crear los `Tenientes` necesarios.
3.  **Eliminación del Capitán Simplificado:** El `onboarding_prestador_capitan.py` será eliminado, ya que su funcionalidad será cubierta por los capitanes reales.
