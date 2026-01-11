# Agente Coronel de Dominio: SG-SST (Seguridad y Salud en el Trabajo)

## 1. Misión Estratégica

El **Coronel SG-SST** es un agente de IA especializado, segundo al mando bajo la supervisión del **General Sarita**. Su misión exclusiva es gestionar todas las operaciones complejas relacionadas con el dominio de Seguridad y Salud en el Trabajo.

Este agente no ejecuta tareas de campo directamente. Su rol es puramente estratégico y de coordinación: **piensa, planifica, descompone, asigna y supervisa**.

## 2. Capacidades Principales

El Coronel SG-SST está diseñado para manejar órdenes de alto nivel como:
- `realizar_auditoria_mensual`: Orquesta una auditoría de seguridad completa en una instalación.
- `investigar_incidente`: Coordina la investigación de un incidente de seguridad reportado.
- `gestionar_plan_capacitacion`: Organiza y verifica la ejecución de planes de capacitación para brigadas.
- `validar_cumplimiento_normativo`: Supervisa la verificación de normativas específicas (ej. alturas, espacios confinados).

## 3. Flujo de Operación Típico

1.  **Recepción de Comando:** Recibe una orden estructurada y validada del General Sarita.
2.  **Planificación (`planner.py`):** Traduce el objetivo de la orden en un plan estratégico de alto nivel, compuesto por fases (ej. recolección de documentos, inspección, entrevistas).
3.  **Descomposición (`task_decomposer.py`):** Toma cada fase del plan y la descompone en tareas tácticas, atómicas y ejecutables (ej. "verificar extintor ABC en cocina").
4.  **Enrutamiento (`captain_router.py`):** Asigna cada tarea táctica a un Capitán especializado (ej. `capitan_inspeccion_equipos`, `capitan_documentacion`).
5.  **Supervisión (`memory.py`):** Mantiene un registro en tiempo real del estado de cada tarea, gestionando fallos, reintentos y resultados parciales.
6.  **Consolidación y Reporte:** Una vez que todas las tareas se completan (o fallan), consolida los resultados en un informe coherente y lo eleva al General Sarita.

## 4. Componentes Internos

-   **`coronel.py`**: El orquestador principal que dirige el flujo.
-   **`policies.py`**: Define las reglas de negocio y normativas del dominio (ej. frecuencia de inspecciones, niveles de riesgo).
-   **`memory.py`**: Gestiona el estado y el progreso de las órdenes activas.
-   **`planner.py`**: El cerebro estratégico.
-   **`task_decomposer.py`**: El traductor de estrategia a táctica.
-   **`captain_router.py`**: El centro logístico para la asignación de tareas.

## 5. Principios de Diseño

-   **Desacoplamiento Total:** No tiene conocimiento del framework Django, la base de datos o la interfaz de usuario.
-   **Autonomía de Dominio:** Opera exclusivamente con la información y las políticas de SG-SST.
-   **Jerarquía Estricta:** Solo se comunica con el General Sarita (hacia arriba) y los Capitanes (hacia abajo).
