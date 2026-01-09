# MAPA JERÁRQUICO DE AGENTES A.I. - SISTEMA SARITA

Este documento define la estructura de mando formal para el sistema de agentes A.I. y audita el estado actual de los agentes existentes, identificando los vacíos jerárququicos y las acciones necesarias para establecer una cadena de mando clara.

## 1. Definición de la Jerarquía Formal

El sistema se organiza bajo una estricta jerarquía militar de 4 niveles. No hay comunicación lateral ni saltos de nivel.

### 🔴 NIVEL 1 — GENERAL (Interfaz Única)
- **Rol:** Recibe la orden en lenguaje natural del usuario (texto/voz) a través del chat, clasifica la intención estratégica y la delega al Coronel del dominio apropiado.
- **Prohibido:** Ejecutar tareas, dar órdenes a Capitanes o unidades inferiores.
- **Debe existir UN solo General.**

### 🟠 NIVEL 2 — CORONELES (Coordinadores Estratégicos de Dominio)
- **Rol:** Cada Coronel representa un macro-dominio del sistema (Comercial, Operativo, Contable, Financiero, Archivístico). Recibe la orden estratégica del General, la traduce a un plan táctico y la delega a sus Capitanes especialistas.
- **Prohibido:** Ejecutar tareas, dar órdenes a unidades inferiores a Capitán.

### 🟡 NIVEL 3 — CAPITANES (Orquestadores Tácticos)
- **Rol:** Cada Capitán es un especialista dentro de un dominio (ej. Capitán de Facturación, Capitán de Inventario). Recibe la orden táctica del Coronel, la convierte en una secuencia de tareas concretas y las delega a las Unidades de Ejecución (Tenientes).
- **Prohibido:** Ejecutar tareas directamente.

### 🟢 NIVEL 4 — UNIDADES DE EJECUCIÓN (Ejecutores)
- **Rol:** Este es el único nivel que ejecuta acciones.
    - **Tenientes:** Coordinan un pequeño grupo de Sargentos para una función específica.
    - **Sargentos:** Supervisan y validan las tareas de los Soldados.
    - **Soldados:** Son los ejecutores finales (scripts, llamadas a API, workers) que realizan el trabajo.

---

## 2. Auditoría del Estado Actual

La siguiente tabla clasifica los agentes encontrados en `backend/agents/corps/` según la jerarquía definida.

| Nombre del Agente | Nivel Jerárquico Detectado | Dominio Funcional | ¿Ejecuta o Coordina? | Clasificación |
| :--- | :--- | :--- | :--- | :--- |
| **sarita_nacion_general.py** | **Nivel 1 - GENERAL** | Mando Estratégico Nacional | Coordina | ✅ **Correcto.** Este es el único punto de entrada válido. |
| **sarita_departamento_general.py** | Nivel 1.5 - Sub-General | Mando Estratégico Departamental | Coordina | ❌ **Mal Ubicado.** Introduce una capa burocrática innecesaria. Debe ser eliminado. |
| **turismo_coronel.py** | **Nivel 2 - CORONEL** | "Turismo" (Todo) | Coordina | ⚠️ **Sin Superior Definido.** Es un "Coronel de todo", viola el principio de especialización por dominio. |
| **admin_captain.py** | **Nivel 3 - CAPITÁN** | Administración | Coordina | 🕳️ **Hueco Jerárquico.** Comanda tenientes de múltiples dominios (Prestadores, Artesanos) que no le corresponden. |
| **artesanos_captain.py** | **Nivel 3 - CAPITÁN** | Artesanos (Operativo) | Coordina | 🕳️ **Hueco Jerárquico.** No reporta a un `Coronel Operativo`. |
| **atractivos_captain.py** | **Nivel 3 - CAPITÁN** | Atractivos (Operativo) | Coordina | 🕳️ **Hueco Jerárquico.** No reporta a un `Coronel Operativo`. |
| **funcionario_captain.py** | **Nivel 3 - CAPITÁN** | Funcionario (Admin) | Coordina | 🕳️ **Hueco Jerárquico.** No reporta a un `Coronel de Administración` (inexistente). |
| **oferta_captain.py** | **Nivel 3 - CAPITÁN** | Oferta Comercial | Coordina | 🕳️ **Hueco Jerárquico.** No reporta a un `Coronel Comercial`. |
| **prestadores_captain.py** | **Nivel 3 - CAPITÁN** | Prestadores (Operativo) | Coordina | 🕳️ **Hueco Jerárquico.** No reporta a un `Coronel Operativo`. |
| **publicaciones_captain.py** | **Nivel 3 - CAPITÁN** | Publicaciones (Operativo) | Coordina | 🕳️ **Hueco Jerárquico.** No reporta a un `Coronel Operativo`. |
| **turista_captain.py** | **Nivel 3 - CAPITÁN** | Turista (Operativo) | Coordina | 🕳️ **Hueco Jerárquico.** No reporta a un `Coronel Operativo`. |
| **videos_captain.py** | **Nivel 3 - CAPITÁN** | Videos (Comercial) | Coordina | 🕳️ **Hueco Jerárquico.** No reporta a un `Coronel Comercial`. |
| *agentes_teniente.py (varios)* | **Nivel 4 - TENIENTE** | Varios | Coordinan Sargentos | 🕳️ **Hueco Jerárquico.** Reciben órdenes de capitanes de dominios incorrectos. |
| *agentes_sargento.py (varios)* | **Nivel 4 - SARGENTO** | Varios | Ejecutan/Supervisan | 🕳️ **Hueco Jerárquico.** Estructura de mando superior es incorrecta. |

### Conclusión de la Auditoría

El sistema actual es un **enjambre caótico con una jerarquía rota**.
- Hay un exceso de Generales.
- Falta la capa de Coroneles especializados por dominio.
- Un único "super-coronel" (`TurismoCoronel`) comanda a capitanes de todos los dominios, rompiendo la cadena de mando.
- Los Capitanes y sus unidades inferiores están funcionalmente correctos, pero reportan a la estructura de mando equivocada.

---

## 3. Plan de Reestructuración y Creación de Agentes

Para establecer la cadena de mando correcta, se ejecutarán las siguientes acciones:

### A. Acciones de Eliminación y Re-nombramiento

1.  **ELIMINAR:** `sarita_departamento_general.py`. Es una capa redundante.
2.  **RENOMBRAR:** `sarita_nacion_general.py` a `general.py` para reflejar que es el único General del sistema.
3.  **ELIMINAR:** `turismo_coronel.py`. Será reemplazado por Coroneles especializados.

### B. Creación de Agentes Faltantes (Nivel Coronel)

Se crearán los siguientes archivos de placeholder para los Coroneles de dominio faltantes en `backend/agents/corps/`:

- `coronel_comercial.py`
- `coronel_operativo.py`
- `coronel_archivistico.py`
- `coronel_contable.py`
- `coronel_financiero.py`

### C. Re-asignación de Subordinados

- El `general.py` será modificado para dar órdenes a los 5 nuevos Coroneles.
- Cada nuevo Coronel será configurado (en su momento) para comandar únicamente a los Capitanes de su dominio correspondiente. (ej. `coronel_operativo` comandará a `artesanos_captain`, `prestadores_captain`, etc.).
