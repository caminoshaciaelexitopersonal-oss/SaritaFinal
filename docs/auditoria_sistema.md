# Auditoría Exhaustiva del Sistema "Sarita"

Este documento detalla la estructura, funcionalidad y estado actual del sistema Sarita, abarcando tanto el backend (Django) como el frontend (Next.js).

## 1. Análisis del Backend (Django)

El backend está construido con Django y Django REST Framework, siguiendo una arquitectura modular robusta. Su función principal es servir como una API RESTful para el frontend, gestionar la lógica de negocio y la persistencia de datos.

### 1.1. Estructura de Directorios Principal (`backend/`)

-   **`apps/`**: Directorio principal que contiene las aplicaciones de negocio reutilizables del proyecto.
    -   **`prestadores/`**: Aplicación central que maneja la lógica de los "Prestadores de Servicios Turísticos". Contiene el módulo paraguas "Mi Negocio".
        -   **`mi_negocio/`**: Módulo clave que implementa el ERP para los prestadores. Se subdivide en gestiones:
            -   **`gestion_comercial/`**: Maneja la lógica de clientes, ventas y facturación.
            -   **`gestion_contable/`**: Un paquete que agrupa múltiples sub-módulos para la contabilidad (activos fijos, compras, inventario, etc.).
            -   **`gestion_financiera/`**: Gestiona cuentas bancarias y transacciones.
            -   **`gestion_operativa/`**: Contiene la lógica operativa genérica (perfil, productos) y especializada (hoteles, restaurantes).
-   **`api/`**: Aplicación Django que contiene la lógica central de la API, incluyendo el modelo de usuario personalizado (`CustomUser`), serializers de autenticación y vistas genéricas.
-   **`puerto_gaitan_turismo/`**: Paquete de configuración del proyecto Django.
    -   `settings.py`: Archivo de configuración principal (analizado previamente). Define las `INSTALLED_APPS`, `MIDDLEWARE`, base de datos y configuraciones de terceros.
    -   `urls.py`: Archivo de enrutamiento principal. Define los puntos de entrada de la API (`/api/auth/`, `/api/v1/mi-negocio/`).
    -   `wsgi.py`: Punto de entrada para servidores web compatibles con WSGI.
-   **`manage.py`**: El script de utilidad de línea de comandos de Django para tareas administrativas (ejecutar el servidor, migraciones, etc.).
-   **`requirements.txt`**: Archivo que lista todas las dependencias de Python del proyecto.

### 1.2. Flujo de Datos y Lógica Clave

-   **Autenticación:** Gestionada por `dj-rest-auth` y `django-allauth`, pero personalizada a través de serializers en `api/serializers.py`. El `CustomTokenSerializer` es crucial, ya que está diseñado para devolver tanto el token como el objeto de usuario en el inicio de sesión, un punto clave para el funcionamiento del frontend.
-   **API "Mi Negocio":** El punto de entrada `/api/v1/mi-negocio/` dirige a `apps.prestadores.mi_negocio.urls`. Este archivo a su vez incluye los `urls.py` de cada módulo de gestión (`comercial`, `financiera`, `contable`, etc.), creando una API RESTful bien estructurada y anidada para el consumo del frontend. Cada módulo de gestión expone sus modelos a través de `ViewSets` de Django REST Framework, proveyendo endpoints CRUD.

## 2. Análisis del Frontend (Next.js)

El frontend está construido con Next.js 14 utilizando el **App Router**. Es responsable de toda la interfaz de usuario, la interacción con el cliente y la comunicación con el backend.

### 2.1. Estructura de Directorios Principal (`frontend/src/`)

-   **`app/`**: El directorio principal del App Router. La estructura de carpetas aquí define directamente las rutas de la URL.
    -   **`dashboard/`**: Contiene todas las rutas y vistas para los usuarios autenticados.
        -   **`login/`**: Página de inicio de sesión.
        -   **`registro/`**: Página de registro de usuarios.
        -   **`prestador/mi-negocio/`**: Corazón de la "segunda vía" (empresario). La estructura de carpetas aquí refleja fielmente la API del backend, con subdirectorios para `gestion-operativa`, `gestion-comercial`, `gestion-contable`, etc. Cada una de estas carpetas contiene una `page.tsx` que es el punto de entrada para esa sección del panel.
    -   **`descubre/`**, **`directorio/`**: Secciones públicas del sitio para la "tercera vía" (el turista), mostrando atractivos, rutas, prestadores, etc.
    -   `layout.tsx`: El layout raíz de la aplicación, que define la estructura HTML principal.
-   **`components/`**: Contiene componentes de React reutilizables.
    -   **`ui/`**: Componentes de UI genéricos y de bajo nivel (Botones, Inputs, Tarjetas, etc.).
    -   `Sidebar.tsx`: El componente de menú de navegación principal para el dashboard, clave en el problema actual.
    -   Otros componentes específicos para diferentes funcionalidades (formularios, perfiles, etc.).
-   **`contexts/`**: Para la gestión de estado global utilizando el Context API de React.
    -   `AuthContext.tsx`: El contexto más crítico. Maneja el estado de autenticación (usuario, token), las funciones de `login`, `logout` y `register`, y provee esta información al resto de la aplicación.
-   **`hooks/`**: Contiene hooks personalizados de React para encapsular lógica reutilizable, especialmente para la comunicación con la API (ej. `useMiNegocioApi.ts`).
-   **`services/`**: Módulos para interactuar con servicios externos, principalmente la API del backend.
    -   `api.ts`: Configuración central de la instancia de `axios`. Define la URL base de la API (`http://1227.0.0.1:8000/api`) y los interceptores. Todas las llamadas a la API en la aplicación deberían usar esta instancia.
-   **`messages/`**: Archivos de internacionalización (`en.json`, `es.json`) para soportar múltiples idiomas en la UI.

### 2.2. Flujo de Datos y Lógica Clave

-   **Gestión de Estado de Autenticación:** El componente `AuthProvider` (de `AuthContext.tsx`) envuelve la aplicación. Al iniciar sesión, llama a la API, espera recibir el `user` y el `token`, y los almacena. Componentes como `Sidebar.tsx` consumen este contexto con el hook `useAuth()` para mostrarse condicionalmente. **Una falla en la obtención del objeto `user` deja a la UI en un estado de carga indefinido.**
-   **Enrutamiento:** Controlado por la estructura de carpetas en `src/app/`. Next.js se encarga del enrutamiento del lado del cliente y del servidor.
-   **Comunicación con la API:** Se centraliza a través del servicio en `services/api.ts`. Los componentes y hooks usan esta instancia de `axios` para realizar peticiones a los endpoints del backend definidos en el análisis anterior.

## 3. Diagnóstico de Problemas en Ejecución

Se realizaron pruebas para instalar dependencias y ejecutar ambos entornos. A continuación se resumen los hallazgos.

### 3.1. Diagnóstico del Backend

-   **Estado:** **NO EJECUTABLE.**
-   **Error Crítico:** `django.db.migrations.exceptions.CircularDependencyError: api.0001_initial, prestadores.0001_initial`.
-   **Análisis:** El sistema no puede arrancar porque existe una dependencia circular irresoluble en las migraciones iniciales de las aplicaciones `api` y `prestadores`. Esto significa que el Modelo A en `api` requiere del Modelo B en `prestadores`, y viceversa, desde su creación. Django no puede determinar cuál crear primero. Este error bloquea cualquier operación de base de datos, incluyendo la ejecución del servidor.

### 3.2. Diagnóstico del Frontend

-   **Estado:** **NO COMPILABLE.**
-   **Error Crítico:** `Module not found` en múltiples archivos.
-   **Análisis:** La compilación de Next.js falla porque no puede encontrar varios componentes y hooks importados. Las causas probables son:
    -   Inconsistencias en las rutas de importación (uso de rutas relativas `../` en lugar de alias `@/`).
    -   Errores de capitalización en los nombres de archivo (ej. importar `card` en lugar de `Card`).
    -   Archivos de componentes que simplemente no existen en la base del código.
    -   El resultado es que no se puede generar una versión de producción del frontend, y el modo de desarrollo probablemente también fallaría.

### 3.3. Causa del Problema del Menú (Círculo de Carga)

El análisis estático confirma que el componente `Sidebar.tsx` muestra un esqueleto de carga (`SidebarSkeleton`) si no recibe un objeto de usuario (`user`) del `AuthContext`. Los problemas en el backend (no arranca) y en el frontend (no compila) hacen imposible que el flujo de inicio de sesión se complete exitosamente. Por lo tanto, el `AuthContext` nunca obtiene los datos del usuario, y el `Sidebar` se queda permanentemente en su estado de carga, explicando el comportamiento reportado.

## 4. Estado de Implementación de las "Tres Vías"

-   **1ª Vía (Gubernamental):** La estructura del backend (roles de administrador/funcionario en `CustomUser`) y del frontend (rutas en `/dashboard/admin`) sugiere que la base para esta vía está presente, pero su funcionalidad completa no se puede verificar debido a los errores de ejecución.
-   **2ª Vía (Empresarial):** Es la más desarrollada. Tanto el backend (`mi_negocio` con todos sus módulos) como el frontend (`/dashboard/prestador/mi-negocio/`) tienen una estructura muy completa y detallada. Se puede afirmar que la arquitectura está **implementada estructuralmente**, pero **no es funcional** debido a los errores de compilación y ejecución.
-   **3ª Vía (Turista):** Las rutas públicas como `/descubre` y `/directorio` en el frontend, y los modelos como `AtractivoTuristico` y `RutaTuristica` en el backend, indican que esta vía también tiene una base sólida. Sin embargo, al igual que las otras, no se puede verificar su funcionamiento.

## 5. Resumen de Estabilización del Frontend (Fase Actual)

-   **Errores Corregidos:**
    -   Se eliminó la funcionalidad de validación con `zod` y `@hookform/resolvers` en los archivos `FacturaCompraForm.tsx` y `ProveedorForm.tsx` para eliminar la necesidad de dependencias externas no autorizadas.
    -   Se corrigieron múltiples errores de importación causados por rutas relativas incorrectas (ej. `../hooks/`) y por capitalización incorrecta de nombres de componentes (ej. `card` en lugar de `Card`).
-   **Estado Actual:** **NO COMPILABLE.**
-   **Bloqueadores:** La compilación sigue fallando debido a que el código importa componentes de UI que no existen en el repositorio. Los archivos faltantes son:
    -   `@/components/ui/Tabs`
    -   `@/components/ui/Form`
    -   `@/components/ui/Textarea`
-   **Conclusión:** De acuerdo a la instrucción de no crear componentes ficticios y al no existir sustitutos claros en el código, el proceso de estabilización del frontend no puede continuar. El siguiente paso requiere una decisión del líder técnico sobre cómo proceder con estos componentes faltantes.
