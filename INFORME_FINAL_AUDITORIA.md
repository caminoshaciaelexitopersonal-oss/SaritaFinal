# INFORME FINAL DE AUDITORÍA INTEGRAL DEL SISTEMA “SARITA”

**Fecha de Emisión:** 2024-10-27
**Auditor a Cargo:** Jules
**Directriz de Referencia:** AUDITORÍA TOTAL, VERIFICACIÓN Y ESTABILIZACIÓN DEL SISTEMA “SARITA”

---

### **📘 1. Inventario Total del Sistema**

El repositorio está organizado en tres componentes principales:

1.  **`backend/`**: Un proyecto Django que contiene toda la lógica de negocio, las APIs, y los sistemas de agentes.
2.  **`frontend/`**: Una aplicación Next.js (puerto 3000) que sirve como la aplicación principal, incluyendo los dashboards para todos los roles de usuario (Vía 1 y Vía 2).
3.  **`web-ventas-frontend/`**: Una segunda aplicación Next.js (puerto 3001), separada de la principal, destinada a ser la página de ventas y el embudo (Vía 3).

La configuración y la arquitectura están definidas en múltiples documentos `.md` en la raíz, siendo `ARQUITECTURA_CANONICA.md` y los reportes de fase (`FASE_U`, `FASE_VW`, `FASE_Z`) los más importantes para entender el diseño del sistema.

---

### **📙 2. Informe Técnico**

#### **Backend**

*   **Framework:** Django 5.2.6, con Django REST Framework para las APIs.
*   **Arquitectura:** Es una arquitectura robusta, multi-tenant (diseñada para servir a múltiples "prestadores" de forma aislada) y orientada a servicios.
*   **Bases de Datos:** PostgreSQL en producción, SQLite para desarrollo.
*   **Asincronía:** Utiliza Celery con Redis para la ejecución de tareas en segundo plano, fundamental para el sistema de agentes.
*   **Capa de Inteligencia de Voz (`apps/sadi_agent/` - Partes Activas):**
    *   **`VoiceOrchestrator`:** Orquesta el flujo de voz de principio a fin. Es funcional.
    *   **`VoiceSecurity`:** Implementa un sistema de permisos RBAC robusto. Es funcional.
    *   **`SemanticEngine`:** **DEUDA TÉCNICA CRÍTICA.** Es un prototipo que utiliza `regex` y coincidencia de palabras clave, no un verdadero motor semántico. No utiliza las capacidades de búsqueda por vectores (`sqlite-vec`) que están incluidas en las dependencias.
*   **Funcionalidad Inesperada:** Existe una integración con la blockchain de **Polygon** para "notarizar" documentos, gestionada a través de una tarea de Celery.

#### **Frontend (Dashboard Principal - `frontend/`)**

*   **Stack:** Next.js 15, React 19, TypeScript, Tailwind CSS. Es un stack moderno y profesional.
*   **Gestión de Estado:** Utiliza **React Query** para la gestión de datos del servidor (API calls), lo cual es una práctica excelente que mejora el rendimiento y la experiencia de usuario.
*   **Autenticación:** El `AuthContext` es el núcleo de la seguridad. Es muy robusto y maneja el login, registro para múltiples roles, persistencia de sesión y redirección basada en roles.
*   **Estado:** El proyecto es **estable en su base**, pero funcionalmente incompleto.

#### **Frontend (Web de Ventas - `web-ventas-frontend/`)**

*   **Stack:** Idéntico al del dashboard principal.
*   **Estado:** **ROTO E INOPERABLE.** El proyecto es una copia incompleta del dashboard. Faltan archivos críticos, como los contextos de autenticación (`AuthContext`), por lo que **no puede ser compilado ni ejecutado**.

---

### **📗 3. Informe Funcional (Cara al Cliente)**

#### **Vía 1 – Corporaciones / Gobierno**

*   **Estado:** **Parcialmente Implementado (Solo UI).**
*   **Análisis:** El `Sidebar` del dashboard renderiza correctamente los menús y secciones para los roles `ADMIN` y `FUNCIONARIO_DIRECTIVO`. La interfaz de usuario existe a nivel de navegación, pero no se ha auditado la funcionalidad página por página. Se presume que, al igual que la Vía 2, muchas de estas páginas son solo marcadores de posición.

#### **Vía 2 – Empresarios (Prestadores)**

*   **Estado:** **MAYORMENTE NO IMPLEMENTADO.**
*   **Análisis de los 5 Módulos ERP:**
    *   Gestión Comercial: ❌ **No Implementado.** El enlace del menú está roto y apunta a una página que no existe.
    *   Gestión Contable: ❌ **No Implementado.** La página principal es un marcador de posición ("en desarrollo").
    *   Gestión Archivística: ✅ **Funcional.** Es el único módulo completo. Permite listar y subir documentos, comunicándose correctamente con el backend.
    *   Gestión Financiera: ❌ **No Implementado.** El enlace del menú está roto.
    *   Gestión Operativa: ✅ **Parcialmente Funcional.** El submódulo "Mi Perfil" funciona correctamente. El estado de los demás (Productos, Clientes, etc.) es incierto pero la base existe.

#### **Vía 3 – Turista (Cara al Cliente Final)**

*   **Estado:** **Parcialmente Funcional (Base Sólida).**
*   **Análisis:**
    *   El flujo de registro y login para el rol `TURISTA` es funcional.
    *   El `AuthContext` contiene lógica específica para que los turistas guarden elementos en "Mi Viaje".
    *   La estructura de archivos en `frontend/src/app/` (`descubre/`, `directorio/`) indica que las páginas públicas existen, pero su funcionalidad y consumo de APIs no fueron auditados en profundidad.
    *   La web de ventas (`web-ventas-frontend`), que sería el principal embudo, está completamente rota.

---

### **🗺️ 4. Mapa de Flujos Reales**

*   **Registro y Autenticación de Usuarios (Todos los Roles):** ✅ **Funciona.**
*   **Protección de Rutas y Redirección por Rol en Frontend:** ✅ **Funciona.**
*   **Flujo de Agentes SARITA (Backend - Onboarding):** ✅ **Funciona.** La invocación por API y la ejecución asíncrona son robustas.
*   **Flujo de Voz (Backend - Onboarding):** ✅ **Funciona.** El flujo completo desde la voz hasta la ejecución de la misión está implementado, aunque con un motor semántico débil.
*   **Módulos ERP del Prestador:**
    *   Gestión Archivística: ✅ **Funciona.**
    *   Gestión Operativa (Perfil): ✅ **Funciona.**
    *   El resto de los módulos ERP: ❌ **No Funcionan.** Son enlaces rotos o páginas de marcador de posición.
*   **Web de Ventas:** ❌ **No Funciona.** El proyecto está roto y no se puede ejecutar.

---

### **🔬 5. Diagnóstico de Estabilidad**

*   **Backend:** **ALTA.** La arquitectura es sólida, pero presenta **riesgos** por deuda técnica (el `SemanticEngine`) y confusión a futuro (código muerto y dos arquitecturas de agentes paralelas).
*   **Frontend (Dashboard):** **MODERADA.** La base es estable, pero la masiva cantidad de funcionalidad incompleta y enlaces rotos lo degrada. El **bloqueo** principal es el bug del "spinner infinito" en el menú, cuya causa raíz ha sido identificada en el `AuthContext`.
*   **Frontend (Web de Ventas):** **NULA.** Es inoperable. **Bloqueo total.**

---

### **🏛️ 6. Informe FASE 7 — Verificación del Sistema de Agentes Inteligentes (SARITA)**

**Objetivo:** Determinar el estado real, alcance funcional y nivel de integración del sistema de agentes.

**Conclusión General:** El proyecto no tiene uno, sino **dos sistemas de agentes distintos** con arquitecturas y estados de madurez completamente diferentes.

#### **Sistema de Agentes #1: Motor de Orquestación "SARITA" (El Caballo de Batalla)**

*   **Ubicación:** `backend/apps/sarita_agents/`
*   **Estado:** ✅ **Activo, Funcional y Robusto.**
*   **Arquitectura:** Es un motor de **orquestación asíncrona**. Su trabajo es seguir planes pre-definidos en el código de manera muy estructurada.
*   **Jerarquía Real:**
    *   **General (`SaritaOrchestrator`):** Es el punto de entrada. Recibe directivas y las delega al Coronel correcto. **Funcional.**
    *   **Coroneles (`CoronelTemplate`, `PrestadoresCoronel`):** Actúan como enrutadores que seleccionan al Capitán adecuado para una misión. **Funcional.**
    *   **Capitanes (`CapitanTemplate`, `CapitanOnboardingPrestador`):** Definen el plan de acción (los pasos a seguir) y orquestan a los Tenientes usando `Celery chord` para ejecución paralela y asíncrona. **Funcional y muy bien implementado.**
    *   **Tenientes (`TenienteTemplate`, `TenienteValidacionPrestador`, etc.):** Son los ejecutores de tareas atómicas. Realizan el trabajo real (validar datos, escribir en la BD). **Funcional.**
*   **Flujo Real de Ejecución:** El flujo `API -> Tarea Celery -> General -> Coronel -> Capitán -> Chord(Tenientes) -> Tarea Callback -> Fin` está completamente implementado y es robusto.
*   **Persistencia y Auditoría:** Cada paso de una misión (Misión, Plan Táctico, Tarea Delegada, Registro de Ejecución) se guarda en la base de datos, haciendo el sistema **totalmente auditable**.
*   **Alcance Funcional:** Actualmente, solo el "corte vertical" para la misión `ONBOARDING_PRESTADOR` en el dominio `prestadores` está implementado.
*   **Código Muerto Asociado:** El directorio `backend/agents/` es un prototipo abandonado de este sistema y debe ser ignorado.

#### **Sistema de Agentes #2: Agente Autónomo "SADI" (El Experimento)**

*   **Ubicación:** `backend/apps/sadi_agent/` (archivos `agent.py`, `planner.py`, `executor.py`, `tool.py`, etc.).
*   **Estado:** ❌ **Inactivo y No Integrado.**
*   **Arquitectura:** Es un **agente autónomo** basado en un LLM (OpenAI). A diferencia de SARITA, no sigue un plan fijo, sino que genera su propio plan en tiempo real (`Planner`) para luego ejecutarlo (`Executor`) usando un conjunto de herramientas (`Tool`). Esta arquitectura es mucho más avanzada y dinámica.
*   **Jerarquía:** No sigue la jerarquía militar. Es una arquitectura de agente único (`Agent`) que razona y actúa.
*   **Integración:** Este sistema **NO** está conectado con el `VoiceOrchestrator` ni con el resto del flujo de la aplicación. Parece ser un experimento o una pieza de una futura implementación que nunca se integró.
*   **Nivel de Madurez:** El código base de la arquitectura existe, pero al no estar integrado, su funcionalidad real no se puede verificar. Es una **isla de código avanzado pero aislado.**

---

### **🕵️ 7. Informe FASE 8 — Diagnóstico del Super Admin y Gobernanza**

**Objetivo:** Determinar si el Super Admin actúa como gobierno real del sistema o es un rol superficial.

**Conclusión General:** El rol de Super Admin (`ADMIN`) tiene las **bases técnicas implementadas** para gobernar el sistema, pero la **funcionalidad a nivel de interfaz de usuario es parcial y está incompleta.**

#### **Capacidades en el Backend (Potencial Real)**

*   **Autenticación y Roles:** El `CustomUser` model en el backend tiene un sistema de roles claro. El rol `ADMIN` es la designación de más alto nivel.
*   **APIs de Administración:** Existe una aplicación Django dedicada, `apps/admin_plataforma/`, destinada a contener las APIs exclusivas para la gobernanza. Esto es una excelente práctica de diseño que aísla la lógica de administración.
*   **Seguridad por Voz:** El sistema `VoiceSecurity` está basado en el modelo `VoicePermission`, que permite definir explícitamente qué acciones puede realizar cada rol. Un Super Admin podría, a través de este sistema, tener acceso a todos los comandos de voz.

#### **Capacidades en el Frontend (Funcionalidad Real)**

*   **Acceso y Vistas:** Un usuario con rol `ADMIN` es correctamente redirigido al `/dashboard` y el `Sidebar` le muestra las secciones de "Plataforma Sarita", "Gestión de Contenido" y "Administración".
*   **Análisis de Funcionalidad de los Menús del Admin:**
    *   `Planes` (`/dashboard/admin_plataforma/planes`): **Probablemente un marcador de posición.**
    *   `Gestión Web` (`/dashboard/admin_plataforma/web-content`): **Probablemente un marcador de posición.**
    *   `Gestión de Contenido` (Publicaciones, Atractivos, Rutas): **Parcialmente funcional.**
    *   `Administración` (Usuarios, Config. del Sitio, Formularios, Verificaciones): **Parcialmente funcional.**
*   **Diferencia UI vs. Backend:** El backend está **preparado** para un gobierno total. El frontend solo ha **implementado algunas de las vistas** necesarias para ejercer ese gobierno.

#### **Conclusión Final de Gobernanza**

El Super Admin **NO es un rol superficial**, tiene un poder real definido en el backend. Sin embargo, su capacidad para gobernar el sistema está **limitada por una interfaz de usuario incompleta.** El rol está en un estado **parcial**. El trabajo restante es de **desarrollo de frontend**.

---

### **🚀 8. Plan Estratégico Post-Auditoría**

1.  **Fase 1: Estabilización y Limpieza (Prioridad Inmediata)**
    *   **1.1:** Reparar el build de `web-ventas-frontend`.
    *   **1.2:** Eliminar el directorio obsoleto `backend/agents/`.
    *   **1.3:** Comentar los enlaces rotos en el `Sidebar`.
    *   **1.4:** Corregir el bug del spinner infinito en el `AuthContext`.

2.  **Fase 2: Unificación y Mejora de la Base Técnica**
    *   **2.1:** Unificar el código duplicado (especialmente `AuthContext`) entre los dos frontends.
    *   **2.2:** Reimplementar el `SemanticEngine` con búsqueda por vectores.
    *   **2.3:** Tomar una decisión estratégica sobre el agente SADI (LangGraph): integrar o eliminar.

3.  **Fase 3: Implementación Incremental de la Vía 2 (Prestadores)**
    *   **3.1:** Implementar el frontend para el Módulo de Gestión Comercial.
    *   **3.2:** Implementar el frontend para el Módulo de Gestión Contable.
    *   **3.3:** Implementar el frontend para el Módulo de Análisis Financiero.
    *   **3.4:** Completar los submódulos de la Gestión Operativa.
