# INVENTARIO DE AGENTES DE IA – BACKEND SARITA

## 1️⃣ Resumen General

Se ha realizado un análisis exhaustivo del directorio `backend/agents`, identificando la estructura, finalidad y estado actual del ecosistema de agentes de IA.

- **Número Total de Agentes Encontrados:** 96 archivos `.py` que definen agentes.
- **Distribución por Jerarquía:**
  - **Agentes Generales:** 1 (implícito, "Sarita")
  - **Agentes Coroneles:** 4 (implícitos, representados por directorios)
  - **Agentes Capitanes:** 91 (definidos en archivos `.py`)
- **Observaciones Críticas Iniciales:**
  - La arquitectura se adhiere a una estricta jerarquía militar (General > Coronel > Capitán).
  - **El 100% de los agentes analizados son esqueletos (`placeholders`) sin funcionalidad real implementada.** Se basan en una plantilla común que simula el flujo de recibir, planificar, delegar y reportar.
  - Se ha detectado una **anomalía estructural grave** en el dominio del Coronel `prestadores` que impide la funcionalidad de toda su rama (más de 80 agentes) debido a la duplicación masiva de código y errores de importación.

---

## 2️⃣ Detalle por Agente (Muestra Representativa)

A continuación, se detalla un agente Capitán de cada rama de Coronel para ilustrar el patrón de diseño y el estado de implementación.

### 🔹 **Coronel: Administrador General**

- **Identificación:**
  - **Nombre del archivo:** `capitan_gobernanza_agentes.py`
  - **Nombre de la clase:** `CapitanGobernanzaAgentes`
  - **Ruta exacta:** `backend/agents/general/sarita/coroneles/administrador_general/capitanes/capitan_gobernanza_agentes.py`
- **Jerarquía:** 🟨 Capitán
- **Finalidad:** Gestionar el ciclo de vida, versionado y rendimiento de los propios agentes de IA (un agente "meta").
- **Funcionalidad Actual:** Es un esqueleto. No se integra con ninguna herramienta de CI/CD o MLOps. Simula un plan de despliegue.
- **Mando y Dependencia:** Reactivo, responde a su Coronel. Su plan prevé la delegación a un "teniente de ci_cd" (inexistente).
- **Nivel de Implementación:** 🔴 Esqueleto / Placeholder
- **Alineación con SADI:** Muy Alta. Es fundamental para la operación de SADI, permitiendo comandos por voz para gestionar otros agentes.

### 🔹 **Coronel: Clientes Turistas**

- **Identificación:**
  - **Nombre del archivo:** `capitan_experiencia_turista.py`
  - **Nombre de la clase:** `CapitanExperienciaTurista`
  - **Ruta exacta:** `backend/agents/general/sarita/coroneles/clientes_turistas/capitanes/capitan_experiencia_turista.py`
- **Jerarquía:** 🟨 Capitán (con rol de orquestador)
- **Finalidad:** Actuar como punto de entrada y coordinador principal para todas las solicitudes de un turista.
- **Funcionalidad Actual:** Es un esqueleto. Su plan define la orquestación de otros capitanes especialistas (Búsqueda, Contexto, Perfil), pero no hay código de ejecución para ello.
- **Mando y Dependencia:** Reactivo, responde a su Coronel. Está diseñado para coordinar a otros Capitanes, lo cual es una excepción a la regla de delegación a Tenientes.
- **Nivel de Implementación:** 🔴 Esqueleto / Placeholder
- **Alineación con SADI:** Muy Alta. Es el interlocutor principal para los comandos de voz del turista.

### 🔹 **Coronel: Gubernamental**

- **Identificación:**
  - **Nombre del archivo:** `capitan_control_prestadores.py`
  - **Nombre de la clase:** `CapitanControlPrestadores`
  - **Ruta exacta:** `backend/agents/general/sarita/coroneles/gubernamental/municipal/capitanes/capitan_control_prestadores.py`
- **Jerarquía:** 🟨 Capitán
- **Finalidad:** Supervisar y fiscalizar a los prestadores de servicios turísticos a nivel municipal.
- **Funcionalidad Actual:** Es un esqueleto. No se integra con ninguna base de datos de prestadores ni gestiona un flujo de inspección. El resultado es simulado.
- **Mando y Dependencia:** Reactivo, responde a su Coronel (Municipal). Su plan prevé la delegación a "tenientes inspectores" (inexistentes).
- **Nivel de Implementación:** 🔴 Esqueleto / Placeholder
- **Alineación con SADI:** Alta. Permite comandos de fiscalización por voz.

### 🔹 **Coronel: Prestadores**

- **Identificación:**
  - **Nombre del archivo:** `capitan_busqueda_documental.py`
  - **Nombre de la clase:** `CapitanBusquedaDocumental`
  - **Ruta exacta:** `backend/agents/general/sarita/coroneles/prestadores/capitanes/gestion_archivistica/capitan_busqueda_documental.py`
- **Jerarquía:** 🟨 Capitán
- **Finalidad:** Ejecutar búsquedas complejas en el archivo digital de un prestador.
- **Funcionalidad Actual:** Es un esqueleto. No se integra con ningún sistema de gestión documental. Notablemente, no hereda de la clase base, a diferencia de otros agentes de su módulo.
- **Mando y Dependencia:** Reactivo, responde a su Coronel. Su plan prevé la delegación a un "teniente de sistemas" (inexistente).
- **Nivel de Implementación:** 🔴 Esqueleto / Placeholder
- **Alineación con SADI:** Alta. Permite comandos de búsqueda por voz para la gestión documental del prestador.

---

## 3️⃣ Mapa de Jerarquía (Estructura de Directorios)

```
(General: Sarita)
└── coroneles/
    ├── administrador_general/
    │   └── capitanes/ (5 agentes)
    ├── clientes_turistas/
    │   └── capitanes/ (6 agentes)
    ├── gubernamental/
    │   ├── departamental/
    │   │   └── capitanes/ (3 agentes)
    │   ├── municipal/
    │   │   └── capitanes/ (3 agentes)
    │   └── nacional/
    │       └── capitanes/ (3 agentes)
    └── prestadores/
        └── capitanes/
            ├── gestion_archivistica/ (8 agentes)
            ├── gestion_comercial/ (12 agentes)
            ├── gestion_contable/ (27 agentes)
            │   ├── activos_fijos/ (11 agentes)
            │   └── nomina/ (17 agentes)
            ├── gestion_financiera/ (9 agentes)
            └── gestion_operativa/ (18 agentes)
                └── sg_sst/ (16 agentes)
```

---

## 4️⃣ Hallazgos Críticos

1.  **Implementación Nula:** El hallazgo más importante es que **ningún agente tiene funcionalidad real implementada**. Todo el ecosistema es una arquitectura de esqueletos. La lógica de negocio reside actualmente en los "servicios" de Django, no en los agentes.

2.  **Violación de DRY y Error Estructural en `prestadores`:**
    - Se encontraron **8 archivos `capitan_base.py` duplicados** en cada subdirectorio del Coronel `prestadores`.
    - Todos estos archivos base contienen una **importación relativa rota** (`from ..capitan_base import CapitanBase`) que apunta a un archivo inexistente.
    - **Consecuencia:** Toda la jerarquía de herencia del Coronel más grande y complejo (con más de 80 capitanes) está rota. Ninguno de estos agentes es instanciable en su estado actual. Esto indica un refactor incompleto o un error de diseño fundamental.

3.  **Jerarquía Anidada Inesperada:**
    - El Coronel `gubernamental` presenta una sub-jerarquía (`departamental`, `municipal`, `nacional`) que no se ajusta al modelo plano de los otros coroneles. Esto podría ser intencional, pero añade complejidad y debe ser validado.
    - El `CapitanExperienciaTurista` está diseñado para orquestar a otros Capitanes, una excepción a la regla de "Capitán delega a Teniente" que debe ser documentada como un patrón de diseño válido (orquestador de dominio).

4.  **Ausencia de Tenientes:** La arquitectura prevé un nivel de "Tenientes" para la ejecución técnica, pero no se encontró ninguna implementación o plantilla para ellos. Esto significa que la capa de ejecución está completamente ausente.

5.  **Anomalía: `captain_template.py`:** Existe un archivo de plantilla en la raíz de `backend/agents`. Aunque no es un agente activo, su presencia debe ser gestionada para evitar que se incluya accidentalmente en el sistema de producción.
