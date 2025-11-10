# Informe de Auditoría del Sistema "Sarita"

## 1. Visión General de la Arquitectura

El sistema "Sarita" está diseñado como una plataforma de "triple vía" que sirve a tres audiencias distintas:

1.  **Vía Gubernamental:** Para entidades como corporaciones y secretarías de turismo, encargadas de la gestión de destinos, rutas, inventarios y la verificación de prestadores de servicios.
2.  **Vía Empresarial (Mi Negocio):** Un panel de gestión tipo ERP para empresarios y prestadores de servicios turísticos. Este panel está dividido en 5 módulos principales: Gestión Operativa, Comercial, Archivística, Contable y Financiera.
3.  **Vía Turista:** Un portal público que permite a los turistas acceder a información sobre destinos, prestadores, artesanos, atractivos y eventos.

La arquitectura técnica consiste en un monorepo con un **backend desarrollado en Django** y un **frontend en Next.js 14** (con App Router).

## 2. Análisis del Backend (Django)

La estructura del backend es robusta, modular y está bien organizada.

### 2.1. Inventario de Archivos y Estructura

El backend reside en la carpeta `backend/`. El listado completo de archivos revela una estructura de proyecto Django estándar con una clara separación de responsabilidades. Las aplicaciones principales se encuentran en `backend/apps/`. El módulo "Mi Negocio" está correctamente ubicado en `backend/apps/prestadores/mi_negocio/`, tal como se indicó.

### 2.2. Configuración del Proyecto (`settings.py`)

El análisis del archivo `backend/puerto_gaitan_turismo/settings.py` revela:

*   **Aplicaciones Instaladas (`INSTALLED_APPS`):** Se confirma que las aplicaciones clave (`api`, `prestadores`) y los módulos de "Mi Negocio" están correctamente registrados:
    *   `gestion_comercial`
    *   `gestion_financiera`
    *   `gestion_archivistica`
    *   El conjunto completo de `gestion_contable` (activos_fijos, compras, contabilidad, etc.).
*   **Modelo de Usuario:** Se utiliza un modelo `CustomUser` (`api.CustomUser`), lo cual es esencial para la gestión de los múltiples roles del sistema.
*   **Autenticación:** Se emplea `dj-rest-auth` y `django-allauth`, configurados para un inicio de sesión basado en correo electrónico.
*   **Módulo `gestion_operativa`:** No está registrado como una app independiente, confirmando que su lógica está integrada dentro de la app `prestadores`.

### 2.3. Modelos y Roles (`api/models.py`)

El modelo `CustomUser` define una enumeración de roles (`Role`) que se alinea perfectamente con la arquitectura de triple vía:

*   **Roles Gubernamentales:** `ADMIN_ENTIDAD`, `FUNCIONARIO_DIRECTIVO`, `FUNCIONARIO_PROFESIONAL`.
*   **Roles Empresariales:** `PRESTADOR`, `ARTESANO`.
*   **Rol Público:** `TURISTA`.

El sistema utiliza perfiles adicionales vinculados al `CustomUser` para almacenar datos específicos de cada rol, como `ProviderProfile` para los prestadores, lo cual es una práctica de diseño sólida.

### 2.4. Estructura de la API (`mi_negocio/urls.py`)

El archivo de rutas `backend/apps/prestadores/mi_negocio/urls.py` confirma que la API para los 5 módulos de gestión está completamente estructurada y es coherente con la arquitectura descrita. Cada módulo expone sus propios endpoints, lo que demuestra que el backend está, a nivel estructural, completamente implementado.

## 3. Análisis del Frontend (Next.js)

El frontend está bien estructurado y sigue las convenciones modernas de Next.js.

### 3.1. Inventario de Archivos y Estructura

El frontend se encuentra en la carpeta `frontend/`. La estructura de directorios bajo `src/app/` refleja la lógica del negocio:

*   **Rutas Públicas (Turista):** `src/app/descubre/` y `src/app/directorio/`.
*   **Rutas de Autenticación:** `src/app/dashboard/login/` y `src/app/dashboard/registro/`.
*   **Panel "Mi Negocio":** Las carpetas bajo `src/app/dashboard/prestador/mi-negocio/` (ej. `gestion-comercial`, `gestion-contable`) se corresponden directamente con los módulos del backend.

### 3.2. Componentes Clave

*   **`Sidebar.tsx` (Menú de Navegación):**
    *   **Diagnóstico:** Este componente depende directamente del `AuthContext` para obtener la información del usuario y su estado de carga (`isLoading`). Muestra un esqueleto de carga mientras `isLoading` es `true`.
    *   **Causa del Problema:** El problema visual del "círculo de carga infinito" no reside en el `Sidebar` en sí, sino en el hecho de que el `AuthContext` nunca finaliza su estado de carga.
    *   **Contenido:** Los enlaces del menú están definidos de forma estática (hardcoded) y se muestran condicionalmente según el rol del usuario, lo cual es correcto.

*   **`AuthContext.tsx` (Flujo de Autenticación):**
    *   **Diagnóstico:** Este es el componente central que gestiona el estado de autenticación de toda la aplicación.
    *   **Flujo Crítico:** Al iniciarse, intenta obtener un token de `localStorage`. Si lo encuentra, realiza una llamada a la API del backend en el endpoint `GET /auth/user/` para obtener los datos del usuario. El estado `isLoading` permanece en `true` hasta que esta llamada se completa.
    *   **Causa del Problema:** El fallo en el inicio de sesión y el menú de carga infinito se deben a que la llamada a `GET /auth/user/` está fallando, impidiendo que el contexto se cargue por completo.

*   **`services/api.ts` (Configuración de API):**
    *   **URL Base:** El frontend está configurado para comunicarse con el backend en `http://127.0.0.1:8000/api`.
    *   **Manejo de Errores:** Incluye interceptores para añadir el token de autenticación a las peticiones y para gestionar errores 401 (No Autorizado), redirigiendo al usuario al login si un token es inválido.

## 4. Informe de Funcionalidad (Cara al Cliente)

### 4.1. Estado Actual del Sistema

**El sistema, en su estado actual, no es funcional.**

*   **Backend:** No se puede iniciar. Falla con un error `ModuleNotFoundError`, indicando que sus dependencias (incluyendo Django) no están instaladas.
*   **Frontend:** El servidor de desarrollo se inicia correctamente. Sin embargo, como no puede comunicarse con el backend, ninguna funcionalidad que dependa de la API (inicio de sesión, registro, visualización de datos) funciona.

### 4.2. Flujo de Registro e Inicio de Sesión

*   **Análisis Estático:** El código para el registro y el inicio de sesión, tanto en el frontend como en el backend, parece estar completamente implementado y bien estructurado. La lógica para manejar diferentes roles y redirigir a los usuarios a sus respectivos paneles está presente.
*   **Análisis Dinámico:** En la práctica, este flujo es **inoperable**. Cualquier intento de iniciar sesión o registrarse desde el frontend resulta en un fallo de red, ya que el servidor del backend no está en ejecución para recibir las peticiones.

### 4.3. Paneles de Administración y Páginas Públicas

*   **Estructura:** Las páginas y componentes para todos los paneles (Administrador, Prestador, etc.) y las vistas de turista existen en el código fuente del frontend.
*   **Funcionalidad:** Ninguna de estas páginas puede mostrar datos reales. Al navegar a una página protegida, el `AuthContext` no puede verificar la autenticación, lo que probablemente resulte en una redirección a la página de inicio de sesión o en un estado de carga infinito, como se observa con el menú.

## 5. Diagnóstico y Observaciones Finales

La auditoría revela un sistema que, a nivel de código y estructura, es robusto, completo y está bien diseñado. La arquitectura de "triple vía" y los 5 módulos ERP de "Mi Negocio" están implementados de manera coherente en el frontend y el backend.

**El problema principal no es un error de lógica en el código, sino un problema de configuración del entorno de ejecución.**

La causa raíz de todos los problemas de funcionalidad observados (menú de carga, fallo de inicio de sesión) es la misma: **el backend no puede ejecutarse porque le faltan sus dependencias de Python.** Sin un backend en funcionamiento, el frontend no puede autenticar usuarios ni obtener datos, lo que deja a la aplicación en un estado de parálisis funcional.

El sistema parece estar "listo para funcionar", pero necesita que su entorno sea configurado correctamente para poder hacerlo.
