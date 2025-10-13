# Diagrama de Arquitectura de Módulos - SARITA

## 1. Visión General

SARITA (Sistema Autónomo en Red Inteligente Territorial Asistida) está diseñado como una plataforma web monolítica con una separación clara entre el frontend y el backend, y un sistema de agentes jerárquicos para la automatización de tareas y la interacción con el usuario.

```
+-------------------------------------------------+
|                                                 |
|                   Usuario (Navegador)           |
|                                                 |
+------------------------+------------------------+
                         |
                         | HTTPS (API Requests)
                         |
+------------------------v------------------------+
|                                                 |
|              Frontend (Next.js 15)              |
|                                                 |
|    +------------------+    +------------------+ |
|    |      Panel       |    |      Sitio       | |
|    |  Administración  |    |      Público     | |
|    +------------------+    +------------------+ |
|                                                 |
+------------------------+------------------------+
                         |
                         | API Gateway (Django REST Framework)
                         |
+------------------------v------------------------+
|                                                 |
|               Backend (Django 5)                |
|                                                 |
|  +-------------------------------------------+  |
|  |     Módulos Principales de la Aplicación    |  |
|  | +-----------+ +----------+ +------------+ |  |
|  | |    API    | |  Turismo | |    Core    | |  |
|  | | (Modelos, | |  (Vistas, | | (Settings, | |  |
|  | |  Vistas)  | |  Modelos) | |   Auth)    | |  |
|  | +-----------+ +----------+ +------------+ |  |
|  +-------------------------------------------+  |
|                                                 |
|  +-------------------------------------------+  |
|  |        Sistema de Agentes (LangGraph)       |  |
|  | +-------------+  +-------------+  +-------+ |  |
|  | | SaritaNacion|  | SaritaDepto |  | Coronel| |  |
|  | |  (General)  |  |  (General)  |  | (Turismo)| |  |
|  | +-------------+  +-------------+  +-------+ |  |
|  +-------------------------------------------+  |
|                                                 |
+------------------------+------------------------+
                         |
                         |
           +-------------+-------------+
           |                           |
+----------v----------+     +----------v----------+
|                     |     |                     |
|      Base de Datos  |     |   Modelos de Lenguaje |
|     (PostgreSQL)    |     |      (LLMs)         |
|                     |     |                     |
+---------------------+     +---------------------+

```

## 2. Componentes Clave

### 2.1. Frontend (Next.js 15)

-   **Panel de Administración:** Interfaz para la gestión de contenidos, usuarios, roles y configuraciones del sistema.
-   **Sitio Público:** El portal de turismo visible para los visitantes, con información sobre atractivos, prestadores de servicios, rutas, etc.
-   **Componentes:** Utiliza ShadCN/UI para los componentes de la interfaz de usuario y TailwindCSS para los estilos.

### 2.2. Backend (Django 5)

-   **API (Módulo Principal):** Contiene los modelos de datos unificados, los serializadores, las vistas (ViewSets) y la lógica de negocio principal. Gestiona usuarios, publicaciones, atractivos turísticos, y más.
-   **Turismo (Módulo Integrado):** Funcionalidades específicas del antiguo "TurismoAPP", ahora completamente integradas en el módulo `api`.
-   **Core:** Contiene la configuración central del proyecto Django (`settings.py`, `urls.py`), utilidades de autenticación (JWT), y otros componentes transversales.
-   **Sistema de Agentes (LangGraph):** Orquesta las interacciones entre los usuarios y los modelos de lenguaje (LLMs).
    -   **SaritaNacionGeneral:** El agente de más alto nivel, supervisa toda la red.
    -   **SaritaDepartamentoGeneral:** Agentes de nivel intermedio, uno por cada dependencia o departamento.
    -   **TurismoCoronel:** Agentes especializados en tareas específicas de turismo, subordinados a los agentes de departamento.

### 2.3. Infraestructura

-   **Base de Datos (PostgreSQL):** Almacena todos los datos de la aplicación de forma centralizada.
-   **Modelos de Lenguaje (LLMs):** Servicios externos (como los de OpenAI, Anthropic, etc.) que proporcionan las capacidades de inteligencia artificial a los agentes.

## 3. Flujo de Datos

1.  El **usuario** interactúa con el **Frontend** a través de su navegador.
2.  El **Frontend** realiza peticiones a la **API del Backend** para obtener o modificar datos.
3.  El **Backend** procesa las peticiones, interactuando con la **Base de Datos** para persistir la información.
4.  Para tareas complejas o interacciones en lenguaje natural, las vistas del backend invocan al **Sistema de Agentes**.
5.  El **Sistema de Agentes** procesa el comando, interactúa con los **LLMs**, y devuelve una respuesta estructurada.
6.  El **Backend** devuelve la respuesta al **Frontend**, que actualiza la interfaz de usuario.