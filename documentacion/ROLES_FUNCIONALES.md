# Cierre Funcional por Rol

Este documento define las capacidades reales de los roles principales del sistema Sarita al cierre de la Fase C.

---

### 1. Administrador de la Plataforma (`ADMIN`)

Este rol gestiona la plataforma Sarita como un producto SaaS, no supervisa a los empresarios.

**Funciones Operativas (CRUD Completo):**
-   **Gestión de Planes:** Crear, leer, actualizar y eliminar planes de suscripción para todos los tipos de clientes (`/dashboard/admin_plataforma/planes`).
-   **Gestión de Contenido Web:** Crear, leer, actualizar y eliminar páginas, secciones y bloques de contenido para el sitio web público (APIs en `/api/web/admin/` implementadas, frontend en desarrollo).
-   **Gestión de Descargas:** Controlar los enlaces de descarga de aplicaciones (APIs en `/api/downloads/admin/` implementadas, frontend en desarrollo).

**Funciones de Solo Lectura (Actual):**
-   N/A

**Funciones No Implementadas (Pero Planeadas):**
-   Dashboard de métricas de ventas y suscripciones.
-   Gestión directa de suscripciones de clientes.
-   Interfaz de usuario completa para la gestión de contenido web y descargas.

---

### 2. Prestador / Empresario (`PRESTADOR`)

Este rol utiliza el sistema de gestión "Mi Negocio".

**Módulos Activos:**
-   **Gestión Operativa:** Funcionalidades básicas como gestión de perfil, productos/servicios y clientes.
-   **Gestión Comercial:** Acceso a facturación de ventas y compras.
-   **Gestión Financiera:** Gestión de cuentas y transacciones.
-   **Gestión Archivística:** Sistema de gestión documental.

**Módulos Congelados (No Funcionales):**
-   **Gestión Contable:** El módulo está incompleto en el backend. La interfaz de usuario muestra un aviso de "En Construcción".
-   **Proyectos y Presupuesto:** Estos módulos están deshabilitados en el backend y no son accesibles desde la interfaz de usuario.

---

### 3. Turista (Usuario Público/Anónimo)

Este rol consume la información pública del portal.

**Funciones Activas:**
-   **Exploración:** Navegar y ver contenido dinámico en la página de inicio, página de descargas y página de planes.
-   **Comercio (Flujo Inicial):**
    -   Añadir planes a un carro de compras (requiere inicio de sesión).
    -   Ver el contenido del carro de compras.
    -   Simular el inicio de un proceso de pago.

**Funciones No Implementadas:**
-   Proceso de pago completo.
-   Creación y gestión de un perfil de "viajero" para guardar favoritos.
-   El resto de las páginas públicas (directorio, guías, etc.) aún no son dinámicas.
