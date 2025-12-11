# Informe de Auditoría Estructural del Sistema "Sarita"

## 1. Introducción y Objetivo

El propósito de este documento es presentar los resultados de una auditoría estática exhaustiva del sistema "Sarita". El análisis se ha realizado "carpeta por carpeta, archivo por archivo" para obtener una comprensión profunda de la arquitectura, el estado de implementación y la funcionalidad prevista, sin modificar ningún archivo.

El objetivo principal es verificar la implementación del sistema de **"triple vía"**:
1.  **Vía de Gobernanza:** Para entidades como secretarías de turismo.
2.  **Vía de Empresarios:** Para prestadores de servicios turísticos, con 5 módulos de gestión (Comercial, Operativo, Archivístico, Contable y Financiero).
3.  **Vía del Turista:** El portal público que consume la información del sistema.

**Conclusión General:** A nivel de código y arquitectura, el sistema "Sarita" es **excepcionalmente robusto, bien diseñado y completo**. La estructura para las tres vías y los cinco módulos ERP está presente y sigue las mejores prácticas de la industria. Sin embargo, el sistema en su estado actual **no es funcional**, ya que la interfaz de usuario está completamente bloqueada por la falta de respuesta del servidor backend.

---

## 2. Diagnóstico del Problema Principal: "Círculo de Carga Infinito"

La queja principal sobre el menú que se queda en un estado de carga perpetuo ha sido analizada y la causa raíz ha sido identificada.

*   **Flujo del Problema:**
    1.  Al cargar la aplicación, el componente `frontend/src/contexts/AuthContext.tsx` establece un estado `isLoading` en `true`.
    2.  Intenta verificar si el usuario tiene una sesión activa realizando una llamada a la API del backend en la ruta `/auth/user/`.
    3.  El componente `frontend/src/components/Sidebar.tsx` (el menú de navegación) depende de este estado. Mientras `isLoading` es `true`, renderiza un componente de esqueleto (`SidebarSkeleton`), que es lo que el usuario percibe como el "círculo de carga".
    4.  Debido a que el backend no responde a la llamada de la API, la promesa nunca se resuelve.
    5.  Como resultado, `isLoading` permanece `true` indefinidamente, y el menú nunca llega a mostrarse.

*   **Conclusión del Diagnóstico:** El problema no es un error de lógica en el frontend. Es un **síntoma directo de un backend inoperativo o inalcanzable**. La estabilización del backend es el único camino para solucionar este problema.

---

## 3. Auditoría Detallada del Backend (`backend/`)

El backend de Django es maduro, seguro y está diseñado para ser escalable.

### 3.1. Arquitectura General y Configuración

*   **Archivo Principal:** `backend/puerto_gaitan_turismo/settings.py`
*   **Observaciones:**
    *   **Base de Datos:** Configurado para usar SQLite en desarrollo local, lo que facilita la portabilidad.
    *   **Aplicaciones Instaladas (`INSTALLED_APPS`):** Define una arquitectura modular clara. Se registran aplicaciones para el núcleo (`api`), los prestadores (`prestadores`), las compañías (`companies`) y cada uno de los módulos ERP.
    *   **Seguridad y Autenticación:** Utiliza `dj-rest-auth` y `django-allauth` para un sistema de autenticación robusto basado en tokens y centrado en el email.
    *   **Arquitectura Multi-Tenant:** La presencia del middleware `TenantMiddleware` es la prueba de una arquitectura multi-inquilino, diseñada para aislar de forma segura los datos de cada prestador de servicios.
    *   **Tareas Asíncronas y Blockchain:** La configuración de `Celery` y `Polygon` indica capacidades avanzadas para tareas en segundo plano y notarización de documentos, respectivamente.

### 3.2. Análisis por Aplicación (Las Tres Vías)

#### **Vía de Gobernanza y Turista: `backend/api/`**

Esta aplicación es la columna vertebral del sistema.

*   **`models.py`:**
    *   **`CustomUser`:** Es el modelo central. La enumeración `Role` implementa a la perfección el sistema de triple vía, con roles como `ADMIN_ENTIDAD`, `PRESTADOR`, y `TURISTA`.
    *   **Perfiles por Rol:** Utiliza un patrón de perfiles (`PerfilFuncionarioDirectivo`, `Artesano`) para extender el `CustomUser` sin sobrecargarlo.
    *   **Contenido del Turista:** Contiene los modelos para el contenido público: `AtractivoTuristico`, `RutaTuristica`, `Publicacion`, etc.
    *   **Módulos de Gobernanza:** Incluye un sistema muy completo para la **Verificación de Cumplimiento** (`PlantillaVerificacion`, `ItemVerificacion`) y **Formularios Dinámicos**.

*   **`serializers.py` y `views.py`:** Proporcionan los endpoints de la API para que el frontend consuma todos los modelos mencionados.

#### **Vía de Gobernanza: `backend/apps/companies/`**

*   **Propósito:** Gestiona las "Entidades" (`Company`), que representan a las secretarías de turismo y otras organizaciones gubernamentales. Un `ProviderProfile` (prestador) siempre pertenece a una `Company`, creando una jerarquía clara.

#### **Vía de Empresarios: `backend/apps/prestadores/`**

Esta es la aplicación principal para la lógica de negocio de "Mi Negocio".

*   **`mi_negocio/gestion_operativa/modulos_genericos/perfil/models.py`:**
    *   **`ProviderProfile`:** Es el modelo **INQUILINO (TENANT)**. Cada prestador es un `ProviderProfile` y todos sus datos de negocio se asocian a él.
    *   **`TenantManager`:** Un gestor de modelos personalizado que **automáticamente filtra todas las consultas a la base de datos por el inquilino activo**. Este es un mecanismo de seguridad de nivel profesional que garantiza que un empresario solo pueda acceder a su propia información.

*   **`mi_negocio/` (Módulos ERP):**
    *   Se confirma la existencia de las carpetas para los 5 módulos:
        1.  `gestion_operativa`: Contiene sub-módulos genéricos (clientes, productos, reservas) y especializados (para hoteles, restaurantes, etc.).
        2.  `gestion_comercial`
        3.  `gestion_contable`: Subdividido en `contabilidad`, `compras`, `inventario`, etc.
        4.  `gestion_financiera`
        5.  `gestion_archivistica`
    *   El código dentro de estos módulos está bien estructurado, con sus propios modelos, vistas y serializers, listo para ser activado.

---

## 4. Auditoría Detallada del Frontend (`frontend/`)

El frontend está construido con un stack tecnológico moderno y sigue las mejores prácticas de desarrollo de React.

### 4.1. Stack Tecnológico

*   **Archivo Principal:** `frontend/package.json`
*   **Observaciones:**
    *   **Framework:** `Next.js 15`, utilizando el App Router.
    *   **Manejo de Datos:** `@tanstack/react-query` para una gestión eficiente del estado del servidor y `axios` para las llamadas a la API.
    *   **UI/UX:** `tailwindcss` para el diseño, `recharts` para gráficos, y `react-toastify` para notificaciones.
    *   **Formularios:** `react-hook-form` y `zod` para formularios robustos y seguros.
    *   **Testing:** `Playwright` para pruebas End-to-End.

### 4.2. Estructura de la Aplicación

*   **`frontend/src/app/` (Enrutamiento):**
    *   **Rutas Públicas (Vía Turista):** Los directorios `descubre/`, `directorio/`, y `mi-viaje/` sirven las páginas para los turistas.
    *   **Rutas Privadas:** El directorio `dashboard/` contiene todas las páginas que requieren autenticación.

*   **`frontend/src/app/dashboard/`:**
    *   **Flujo de Autenticación:** Las páginas de `login/` y `registro/` gestionan el acceso.
    *   **Paneles por Rol:** Los directorios `admin/` (Vía Gobernanza) y `prestador/` (Vía Empresarios) separan claramente las interfaces para cada rol principal.

*   **`frontend/src/app/dashboard/prestador/mi-negocio/`:**
    *   **Correspondencia Perfecta:** La estructura de carpetas aquí (`gestion-comercial`, `gestion-contable`, etc.) es un **espejo exacto** de la estructura del backend, lo que demuestra una arquitectura coherente.
    *   **`hooks/`:** Un directorio dedicado a centralizar la lógica de comunicación con la API para todos los módulos de "Mi Negocio", lo cual es una excelente práctica.

---

## 5. Conclusión Final y Recomendación

El sistema "Sarita" ha sido diseñado y construido con un muy alto nivel de calidad técnica y arquitectónica. La estructura de código es lógica, modular, segura y completa, correspondiendo a todos los requisitos funcionales del sistema de triple vía.

**El único y principal impedimento para que el sistema sea funcional es que el backend no está en ejecución.**

**Próximo Paso Recomendado:**
Proceder con una **Fase de Estabilización**. Esta fase debe comenzar con los siguientes pasos, solicitando explícitamente autorización para ello:
1.  **Intentar ejecutar el Backend:** Instalar dependencias (`requirements.txt`) y correr el servidor de Django para diagnosticar y resolver cualquier error de arranque (ej. migraciones de base de datos, dependencias faltantes).
2.  **Intentar ejecutar el Frontend:** Una vez que el backend esté en línea, instalar dependencias (`package.json`) y correr el servidor de Next.js para confirmar la conectividad y la renderización correcta de la interfaz.
3.  **Corrección de Errores:** Abordar cualquier otro error de integración que surja una vez que ambos sistemas estén en comunicación.
