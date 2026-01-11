# Agente Coronel de Dominio: Gubernamental Municipal

## 1. Misión Estratégica

El **Coronel Gubernamental Municipal** es un agente de IA especializado, bajo el mando del **General Sarita**, enfocado en la gestión de operaciones y regulaciones a nivel municipal.

Su misión es coordinar la ejecución de directivas relacionadas con la administración pública local, como la gestión de licencias, la supervisión de normativas urbanísticas y la respuesta a solicitudes ciudadanas. Actúa como el centro neurálgico para todas las operaciones de la IA que conciernen al municipio.

## 2. Capacidades Principales

-   `procesar_nueva_licencia`: Orquesta el flujo completo para la solicitud y aprobación de nuevas licencias comerciales.
-   `verificar_estado_establecimiento`: Coordina inspecciones y validaciones de rutina sobre establecimientos existentes.
-   `gestionar_peticion_ciudadana`: Procesa y dirige las peticiones, quejas o reclamos (PQR) de los ciudadanos a las entidades correspondientes.

## 3. Flujo de Operación Típico

1.  **Recepción de Comando:** Recibe una orden del General Sarita (ej. "Procesar nueva licencia para restaurante en la Calle Mayor").
2.  **Planificación (`planner.py`):** Crea un plan de fases como `[recepcion_documental, validacion_legal, inspeccion_fisica, emision_concepto]`.
3.  **Descomposición (`task_decomposer.py`):** Descompone cada fase en tareas atómicas (ej. "verificar_pago_impuestos", "agendar_visita_inspeccion").
4.  **Enrutamiento (`captain_router.py`):** Asigna cada tarea a un Capitán municipal especializado (ej. `Capitan_HaciendaMunicipal`, `Capitan_ObrasPublicas`).
5.  **Supervisión (`memory.py`):** Monitoriza el progreso de cada tarea en tiempo real.
6.  **Consolidación y Reporte:** Consolida los resultados y reporta el estado final (ej. "Licencia Aprobada, #LIC-2024-001") al General Sarita.

## 4. Componentes Internos

-   **`coronel.py`**: Orquestador principal.
-   **`policies.py`**: Define reglas del dominio municipal (ej. qué actividades requieren inspección, días de aviso para vencimientos).
-   **`memory.py`**: Gestiona el estado de las órdenes activas.
-   **`planner.py`**: Cerebro estratégico para operaciones municipales.
-   **`task_decomposer.py`**: Traductor de fases a tareas tácticas.
-   **`captain_router.py`**: Centro logístico para la asignación a Capitanes municipales.
