# Agente Coronel de Dominio: [NOMBRE DEL DOMINIO]

## 1. Misión Estratégica

El **Coronel de [NOMBRE DEL DOMINIO]** es un agente de IA especializado, segundo al mando bajo la supervisión del **General Sarita**. Su misión exclusiva es gestionar todas las operaciones complejas relacionadas con el dominio de [NOMBRE DEL DOMINIO].

Este agente no ejecuta tareas finales directamente. Su rol es puramente estratégico y de coordinación: **piensa, planifica, descompone, asigna y supervisa**.

## 2. Capacidades Principales

El Coronel está diseñado para manejar órdenes de alto nivel específicas de su dominio.

## 3. Flujo de Operación Típico

1.  **Recepción de Comando:** Recibe una orden estructurada y validada del General Sarita.
2.  **Planificación (`planner.py`):** Traduce el objetivo de la orden en un plan estratégico de alto nivel.
3.  **Descomposición (`task_decomposer.py`):** Toma cada fase del plan y la descompone en tareas tácticas, atómicas y ejecutables.
4.  **Enrutamiento (`captain_router.py`):** Asigna cada tarea táctica a un Capitán especializado.
5.  **Supervisión (`memory.py`):** Mantiene un registro en tiempo real del estado de cada tarea.
6.  **Consolidación y Reporte:** Consolida los resultados en un informe y lo eleva al General Sarita.

## 4. Componentes Internos

-   **`coronel.py`**: El orquestador principal.
-   **`policies.py`**: Define las reglas de negocio y normativas del dominio.
-   **`memory.py`**: Gestiona el estado y el progreso de las órdenes.
-   **`planner.py`**: El cerebro estratégico.
-   **`task_decomposer.py`**: El traductor de estrategia a táctica.
-   **`captain_router.py`**: El centro logístico para la asignación de tareas.
