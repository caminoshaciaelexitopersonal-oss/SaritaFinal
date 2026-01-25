# Análisis de la Arquitectura de Agentes SARITA

## 1. Resumen Ejecutivo

Este documento detalla la arquitectura jerárquica del sistema de agentes SARITA, basada en el análisis del código fuente encontrado en `backend/agents/`. La arquitectura sigue un modelo militar estricto de mando y control, diseñado para la delegación, ejecución y reporte de tareas de forma organizada y auditable.

La misión de la Fase T es replicar esta estructura exacta en el backend de Django, respetando la jerarquía y el flujo de operaciones aquí descritos.

## 2. Jerarquía de Mando y Roster de Agentes

La estructura de agentes es jerárquica y consta de cuatro (4) niveles bien definidos.

### Nivel 1: General (Comandante Supremo)
- **Agente:** `sarita`
- **Ubicación:** `backend/agents/general/sarita/`
- **Misión:** Actúa como el cerebro central y el único punto de entrada para las directivas del sistema. Es responsable de interpretar la intención estratégica, delegarla al Coronel apropiado y supervisar el resultado final. No ejecuta tareas directamente.

### Nivel 2: Coroneles (Comandantes de Dominio)
- **Agentes:**
    - `administrador_general`: Gestiona operaciones de la plataforma interna.
    - `clientes_turistas`: Gestiona interacciones y datos del usuario final (turista).
    - `gubernamental`: Gestiona procesos y datos relacionados con entidades gubernamentales.
    - `prestadores`: Gestiona la lógica de negocio de los proveedores de servicios (hoteles, tours, etc.).
- **Ubicación:** `backend/agents/general/sarita/coroneles/`
- **Misión:** Cada Coronel es un experto en su dominio de negocio. Recibe directivas estratégicas del General, las traduce en misiones tácticas y se las asigna al Capitán más adecuado dentro de su división. Supervisa el progreso de las misiones.

### Nivel 3: Capitanes (Agentes Tácticos Especializados)
- **Agente Base:** `captain_template.py`
- **Ubicación:** (Por implementar, dentro de cada directorio de Coronel)
- **Misión:** Son los agentes de campo. Reciben una misión específica de su Coronel (ej: "gestionar una reserva"). Su responsabilidad es crear un plan detallado (una secuencia de pasos) para cumplir esa misión. No ejecutan los pasos directamente, sino que los delegan.

### Nivel 4: Tenientes (Ejecutores Atómicos)
- **Agente Base:** (Implícito en el `captain_template.py`, por implementar)
- **Ubicación:** (Por implementar)
- **Misión:** Son los "soldados". Reciben una tarea atómica y bien definida de un Capitán (ej: "escribir en la base de datos", "llamar a una API externa"). Son la única capa que interactúa directamente con los servicios del sistema para mutar el estado.

## 3. Flujo de Mando y Operación (Ciclo Canónico)

El flujo de una directiva a través del sistema es unidireccional y sigue un ciclo de delegación y reporte. El `captain_template.py` define el núcleo de este ciclo a nivel táctico.

1.  **Directiva -> General (`sarita`):** Un usuario o sistema emite una orden de alto nivel (ej: "Inscribir nuevo hotel").
2.  **Delegación Estratégica -> Coronel:** El General `sarita` determina que esta es una tarea para el dominio de `prestadores` y delega la misión al `Coronel de Prestadores`.
3.  **Orden Táctica -> Capitán (`handle_order`):** El Coronel traduce la misión en una orden táctica y la envía al Capitán apropiado (ej: `Capitán de Onboarding de Hoteles`).
4.  **Planificación (`plan`):** El Capitán recibe la orden y crea un plan paso a paso (ej: 1. Validar datos, 2. Crear perfil de proveedor, 3. Configurar habitaciones, 4. Notificar al usuario).
5.  **Delegación de Tareas (`delegate`):** El Capitán delega cada paso del plan a los Tenientes correspondientes (ej: `Teniente de Base de Datos`, `Teniente de Notificaciones`).
6.  **Ejecución:** Los Tenientes ejecutan las tareas atómicas.
7.  **Reporte (`report`):** Los resultados de cada tarea se reportan hacia arriba. Los Tenientes informan al Capitán, quien consolida los resultados en un informe final para el Coronel. El Coronel, a su vez, reporta el estado final de la misión al General.

Este flujo garantiza una clara separación de responsabilidades, auditabilidad y control en toda la cadena de mando.
