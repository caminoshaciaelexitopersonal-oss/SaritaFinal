# Informe de Auditoría del Sistema "Sarita"

## 1. Resumen Ejecutivo

Este documento presenta un análisis exhaustivo del sistema "Sarita", una plataforma de turismo de "triple vía" que conecta entidades de gobernanza, prestadores de servicios turísticos y turistas. La auditoría se ha realizado sin modificar el código fuente y se centra en la estructura, funcionalidades implementadas y la identificación de problemas clave en el backend (Django) y el frontend (Next.js).

El sistema demuestra una arquitectura robusta y bien estructurada, con una clara separación de responsabilidades. El backend está organizado en módulos de Django que se corresponden con las diferentes áreas de negocio, y el frontend refleja esta estructura modular en su sistema de rutas y componentes.

Se ha verificado la implementación de los módulos de gestión empresarial para la "segunda vía" (el prestador), confirmando la existencia de funcionalidades para la gestión operativa, comercial, financiera y contable. El módulo de gestión archivística no está implementado y funciona como un placeholder.

El principal problema identificado es un error crítico en la interfaz de usuario del frontend que provoca que el menú de navegación se quede en un estado de carga infinita al fallar la autenticación (ej. con un token inválido), bloqueando el acceso a las secciones autenticadas. La causa raíz ha sido diagnosticada con precisión.

## 2. Metodología

La auditoría se realizó en las siguientes fases:

1.  **Análisis Estructural del Proyecto:** Se realizó un inventario completo de los archivos y directorios para obtener una visión general de la organización del monorepo.
2.  **Auditoría del Backend (Django):** Se analizaron archivos de configuración, rutas, modelos y aplicaciones para entender la arquitectura y lógica de negocio.
3.  **Auditoría del Frontend (Next.js):** Se analizaron dependencias, configuración, estructura de rutas, componentes y el flujo de autenticación para entender la arquitectura de la interfaz de usuario y diagnosticar problemas.

## 3. Análisis del Backend (Django)

El backend es un proyecto Django robusto y modular.

### 3.1. Configuración del Proyecto

*   **Archivo Clave:** `backend/puerto_gaitan_turismo/settings.py`
*   **Aplicaciones Instaladas (`INSTALLED_APPS`):** La configuración revela una arquitectura modular bien definida:
    *   **Apps Principales:** `api`, `apps.prestadores`.
    *   **Módulos "Mi Negocio":**
        *   `apps.prestadores.mi_negocio.gestion_comercial`
        *   `apps.prestadores.mi_negocio.gestion_financiera`
        *   `apps.prestadores.mi_negocio.gestion_contable` (desglosada en 7 submódulos como `activos_fijos`, `compras`, `contabilidad`, etc.).
    *   **Módulos Faltantes:** `gestion_archivistica` no está en `INSTALLED_APPS`, confirmando que no está implementado.
*   **Autenticación:** Se utiliza `django-allauth` y `dj-rest-auth` con un modelo de usuario personalizado (`api.CustomUser`), configurado para un registro y acceso centrado en el email.
*   **Base de Datos:** Configurada para usar SQLite en desarrollo.

### 3.2. Mapa de Endpoints de la API

El enrutamiento de la API es centralizado y claro.

*   **Archivo Raíz de URLs:** `backend/puerto_gaitan_turismo/urls.py`
*   **Estructura de Rutas:**
    *   `/api/auth/`: Maneja la autenticación y el registro a través de `dj_rest_auth`.
    *   `/api/`: Endpoints generales, de administración y contenido público, gestionados por la app `api`.
    *   `/api/v1/mi-negocio/`: Endpoints específicos para el panel del prestador de servicios, gestionados de forma modular. Cada módulo (`operativa`, `comercial`, `financiera`, etc.) tiene su propio archivo de URLs anidado, lo que resulta en una API muy organizada.

### 3.3. Módulos de Gestión Empresarial ("Segunda Vía")

Se verificó la existencia y el estado de implementación de los módulos de gestión para el prestador de servicios, ubicados en `backend/apps/prestadores/mi_negocio/`.

*   **Gestión Operativa:** Implementada y muy completa. Contiene submódulos genéricos para `perfil`, `clientes`, `productos_servicios`, `reservas`, etc.
*   **Gestión Comercial:** Implementada. Contiene `models.py`, `views.py` y `serializers.py`.
*   **Gestión Financiera:** Implementada. Contiene `models.py`, `views.py` y `serializers.py`.
*   **Gestión Contable:** Implementada como una agrupación de múltiples submódulos (`activos_fijos`, `compras`, `contabilidad`, `inventario`, `nomina`, `proyectos`, `presupuesto`), cada uno con su propia estructura.
*   **Gestión Archivística:** **No implementada**. El directorio solo contiene un `urls.py` que apunta a una vista `PlaceholderView`.

### 3.4. Modelo de Datos

*   **`api/models.py`:**
    *   **`CustomUser`:** Define los roles del sistema (`ADMIN`, `PRESTADOR`, `TURISTA`, etc.), que son la base de la arquitectura de "triple vía".
    *   **Modelos de Contenido:** Define los modelos para la "vía de gobernanza" y la "vía del turista", como `AtractivoTuristico`, `RutaTuristica`, `Publicacion`, etc.
    *   **Dependencia Circular:** Se encontró un `ForeignKey` comentado en el modelo `PlantillaVerificacion` que apunta a `prestadores.CategoriaPrestador`. La nota "Parche temporal... CircularDependencyError" es un hallazgo técnico crucial que evidencia un problema conocido de acoplamiento entre las apps `api` y `prestadores`.
*   **`backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/perfil/models.py`:**
    *   **`Perfil`:** Este es el modelo central del prestador de servicios ("segunda vía"). Contiene campos comerciales, de contacto y un sistema de puntuación para la clasificación.
    *   **`CategoriaPrestador`:** La presencia de este modelo aquí confirma la causa de la dependencia circular mencionada anteriormente.

## 4. Análisis del Frontend (Next.js)

El frontend es una aplicación moderna de Next.js que consume la API de Django.

### 4.1. Configuración y Dependencias

*   **Archivos Clave:** `frontend/package.json`, `frontend/next.config.ts`.
*   **Tecnologías:**
    *   **Framework:** Next.js 14 (v15.5.4 en el `package.json`).
    *   **Estilos:** Tailwind CSS.
    *   **UI:** Componentes de Radix UI e iconos de Lucide React.
    *   **Peticiones API:** `axios`.
    *   **Formularios:** `react-hook-form`.
    *   **Internacionalización:** `next-intl`.
*   **Configuración:** Se utilizan alias de ruta (`@/`) y la configuración de `next-intl` es correcta. Se permite explícitamente el acceso a imágenes servidas por el backend.

### 4.2. Estructura de Rutas y Componentes

*   **Archivo Clave:** El directorio `frontend/src/app/`.
*   **Rutas Públicas (Vía Turista):** `/descubre`, `/directorio`, `/mi-viaje`.
*   **Rutas de Autenticación:** `/dashboard/login`, `/dashboard/registro`.
*   **Rutas Protegidas:**
    *   `/dashboard/admin/`: Panel de administración (Vía Gobernanza).
    *   `/dashboard/prestador/mi-negocio/`: Panel del empresario (Vía Prestador), que a su vez contiene sub-rutas que reflejan la estructura modular del backend (`/gestion-operativa`, `/gestion-comercial`, etc.).

### 4.3. Flujo de Autenticación

*   **Archivo Clave:** `frontend/src/contexts/AuthContext.tsx`.
*   **Lógica Centralizada:** Un `AuthContext` gestiona de forma centralizada toda la lógica de autenticación: estado del token, datos del usuario, funciones de `login`, `logout`, `register`, etc.
*   **Persistencia de Sesión:** El token de autenticación se almacena en el `localStorage` para mantener la sesión del usuario activa entre recargas.
*   **Proceso de Carga:** Al iniciar la aplicación, el contexto intenta leer el token del `localStorage` y, si existe, realiza una petición a `/api/auth/user/` para obtener los datos del usuario.

### 4.4. Diagnóstico del Problema del Menú

*   **Componente Afectado:** `frontend/src/components/Sidebar.tsx`.
*   **Causa Raíz:** El problema del menú de carga infinita se debe a una gestión incorrecta del estado de carga.
    1.  El componente `Sidebar` muestra un esqueleto de carga (`SidebarSkeleton`) basado en la condición `if (!user)`.
    2.  Cuando un usuario con una sesión inválida (ej. token expirado) visita la página, el `AuthContext` intenta obtener los datos del usuario, pero la petición a la API falla (ej. con un error 401).
    3.  El `AuthContext` maneja el error llamando a `logout()`, lo que asegura que el estado `user` permanezca como `null`.
    4.  El `Sidebar` se vuelve a renderizar, pero como `user` sigue siendo `null`, la condición `if (!user)` sigue siendo verdadera.
    5.  **Conclusión:** El componente nunca deja de mostrar el esqueleto porque no tiene en cuenta el estado de `isLoading` del `AuthContext`. Permanece en un estado visual de "cargando" indefinidamente, aunque el proceso de autenticación ya ha concluido con un fallo.

## 5. Análisis de las Tres Vías

La arquitectura del sistema soporta claramente el modelo de negocio de "triple vía".

*   **1ª Vía (Gobernanza):**
    *   **Backend:** Soportado por los modelos de contenido (`AtractivoTuristico`, `Publicacion`, `PaginaInstitucional`) y los endpoints de administración en `api/urls.py`.
    *   **Frontend:** Implementado a través del panel en `/dashboard/admin/`.
*   **2ª Vía (Prestador/Empresario):**
    *   **Backend:** Soportado por el completo ecosistema de módulos de "Mi Negocio" (`gestion_operativa`, `gestion_comercial`, etc.) bajo la app `prestadores`, con el modelo `Perfil` como eje central.
    *   **Frontend:** Implementado a través del panel en `/dashboard/prestador/mi-negocio/`, cuya estructura de rutas y componentes se alinea directamente con la API.
*   **3ª Vía (Turista):**
    *   **Backend:** Soportado por los endpoints públicos en `api/urls.py` que exponen los atractivos, publicaciones, artesanos, etc.
    *   **Frontend:** Implementado a través de las rutas públicas como `/descubre`, `/directorio` y la funcionalidad de `/mi-viaje` para guardar elementos favoritos.

## 6. Conclusiones y Próximos Pasos

El sistema "Sarita" está construido sobre una base arquitectónica sólida y bien pensada. La modularidad del backend y la estructura reactiva del frontend están bien alineadas.

**Problemas Identificados:**

1.  **Crítico:** El bug del menú de carga infinita en el frontend impide el uso de la aplicación para usuarios cuya sesión es inválida, presentando una mala experiencia de usuario.
2.  **Mayor:** Existe una dependencia circular a nivel de modelos entre las aplicaciones `api` y `prestadores` en el backend, actualmente mitigada con un parche temporal (código comentado). Esto representa una deuda técnica que debería abordarse.
3.  **Menor:** El módulo de `gestion_archivistica` no está implementado, lo cual es consistente con las instrucciones del proyecto.

**Recomendación:**

La prioridad debe ser corregir el bug del menú en el frontend para estabilizar la experiencia de usuario. Posteriormente, se debería planificar la refactorización necesaria en el backend para resolver la dependencia circular.
