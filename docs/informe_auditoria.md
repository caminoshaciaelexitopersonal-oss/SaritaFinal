# Informe de Auditoría del Sistema "Sarita"

**Fecha:** 2025-11-08
**Autor:** Jules

## 1. Resumen Ejecutivo

Este informe detalla los hallazgos de una auditoría exhaustiva del sistema "Sarita", un proyecto monorepo que comprende un backend en Django y un frontend en Next.js. El objetivo de la auditoría fue analizar la estructura, verificar las funcionalidades implementadas y evaluar el estado actual del sistema sin realizar modificaciones en el código.

**Conclusión Principal:** El sistema "Sarita" es una plataforma robusta, con una arquitectura bien definida y altamente modular que soporta la visión de "triple vía" (Gobernanza, Empresarios/Prestadores, Turistas). La implementación de los módulos de gestión empresarial ("Mi Negocio") está estructuralmente completa tanto en el backend como en el frontend. Se identificó un bug crítico pero solucionable en la interfaz de usuario, y un riesgo técnico latente en el backend relacionado con una dependencia circular. Sorprendentemente, ambos servidores (backend y frontend) pudieron iniciarse con éxito, lo que indica que el sistema está en un estado funcional para comenzar las pruebas y correcciones.

## 2. Análisis del Backend (Django)

### 2.1. Arquitectura y Estructura

*   **Pila Tecnológica:** Django, Django REST Framework, `dj-rest-auth`, `django-allauth`.
*   **Base de Datos:** Configurada para PostgreSQL (producción) y SQLite (desarrollo).
*   **Arquitectura Modular:** El backend presenta una arquitectura "micro-aplicaciones" muy granular. La lógica de negocio principal se encuentra en `backend/apps/prestadores/mi_negocio/`, la cual se subdivide en los 5 módulos de gestión:
    *   `gestion_operativa`
    *   `gestion_comercial`
    *   `gestion_contable`
    *   `gestion_financiera`
    *   `gestion_archivistica`
*   **Modelo de Datos:** El modelo `CustomUser` (`api/models.py`) define claramente los roles que sustentan la arquitectura de "triple vía":
    *   **Vía 1 (Gobernanza):** Roles como `ADMIN_ENTIDAD`, `FUNCIONARIO_DIRECTIVO`.
    *   **Vía 2 (Empresarios):** Roles `PRESTADOR` y `ARTESANO`. El modelo principal `Perfil` del prestador se encuentra en una sub-aplicación dedicada en `.../gestion_operativa/modulos_genericos/perfil/models.py`.
    *   **Vía 3 (Turista):** Rol `TURISTA`.

### 2.2. Estado de Implementación de "Mi Negocio"

*   **Estructuralmente Completo:** Se confirma que la estructura de carpetas y aplicaciones para los 5 módulos de gestión está presente y registrada en `settings.py`.
*   **`gestion_operativa`:** Es el módulo base, conteniendo modelos genéricos como `Perfil`, `Clientes`, `Productos`, etc.
*   **`gestion_contable`:** Muestra una implementación muy detallada, con submódulos para `compras`, `inventario`, `nomina`, `activos_fijos`, etc.
*   **Funcionalidades Clave:** El sistema incluye modelos para funcionalidades avanzadas como un sistema de puntuación, formularios dinámicos, y un módulo de verificación de cumplimiento.

### 2.3. Riesgos y Observaciones

*   **Riesgo de Dependencia Circular (Crítico Latente):** Se encontró evidencia en el código (`api/models.py`, modelo `PlantillaVerificacion`) de una `CircularDependencyError` entre las aplicaciones `api` y `prestadores`. Aunque las migraciones se aplicaron con éxito durante la prueba de ejecución, este problema arquitectónico subyacente es un riesgo significativo que puede resurgir y causar problemas de estabilidad en el futuro, especialmente al añadir o modificar modelos.
*   **Advertencias de Configuración:** Al ejecutar `manage.py`, aparecen advertencias relacionadas con `ACCOUNT_LOGIN_METHODS` y una ruta de `STATICFILES_DIRS` inexistente. Son de baja prioridad pero deben ser corregidas.

## 3. Análisis del Frontend (Next.js)

### 3.1. Arquitectura y Estructura

*   **Pila Tecnológica:** Next.js 14 (App Router), TypeScript, TailwindCSS.
*   **Gestión de Datos:** `axios` para llamadas a la API y `react-hook-form` para formularios.
*   **Internacionalización:** Preparado para ser multilingüe con `next-intl`.
*   **Estructura de Rutas:** La estructura de carpetas en `frontend/src/app/` se corresponde directamente con la arquitectura del sistema, incluyendo rutas detalladas para cada módulo de "Mi Negocio" en `frontend/src/app/dashboard/prestador/mi-negocio/`.

### 3.2. Flujo de Autenticación y Experiencia de Usuario

*   **Autenticación Centralizada:** El `AuthContext.tsx` maneja toda la lógica de login, registro y gestión de sesión. Está correctamente configurado para trabajar con los endpoints personalizados del backend.
*   **Navegación del Dashboard:** El componente `Sidebar.tsx` contiene una estructura de navegación codificada estáticamente que refleja con precisión todos los módulos de "Mi Negocio" y los paneles de administración, confirmando que la UI está lista para estas funcionalidades.

### 3.3. Bugs Identificados

*   **Bug del Menú con Carga Infinita (Crítico, Causa Identificada):**
    *   **Síntoma:** El menú del dashboard a veces se queda en un estado de carga (esqueleto) infinito.
    *   **Causa Raíz:** La auditoría del código reveló que el componente `Sidebar.tsx` solo verifica la existencia del objeto `user` (`if (!user)`) para mostrar el esqueleto de carga. No tiene en cuenta el estado `isLoading` del `AuthContext`.
    *   **Escenario del Bug:** Cuando la autenticación finaliza (`isLoading` es `false`) pero el usuario no es válido (`user` es `null`), la condición `!user` sigue siendo verdadera, y el esqueleto de carga nunca se elimina.

## 4. Resultados de la Verificación de Ejecución

*   **Dependencias:** Las dependencias de `pip` y `npm` se instalaron correctamente.
*   **Base de Datos:** El comando `python backend/manage.py migrate` **se ejecutó con éxito**, inicializando la base de datos SQLite sin la `CircularDependencyError` esperada.
*   **Servidor Backend:** El servidor de desarrollo de Django **se inició correctamente** y está en ejecución.
*   **Servidor Frontend:** El servidor de desarrollo de Next.js **se inició correctamente** y está en ejecución.

**Conclusión:** El sistema es ejecutable en su estado actual.

## 5. Propuesta de Plan de Acción por Fases

Para llevar el sistema "Sarita" a un estado 100% funcional, limpio y documentado, se propone el siguiente plan de acción:

### Fase 1: Corrección de Bugs Críticos y Estabilización

1.  **Corregir el Bug del Menú:**
    *   **Tarea:** Modificar `frontend/src/components/Sidebar.tsx`.
    *   **Detalle:** Obtener el estado `isLoading` del `useAuth()` hook y cambiar la condición de renderizado del esqueleto de `if (!user)` a `if (isLoading)`. Esto asegurará que el esqueleto solo se muestre mientras los datos de autenticación se están cargando activamente.
2.  **Solucionar la Dependencia Circular del Backend:**
    *   **Tarea:** Refactorizar el modelo `PlantillaVerificacion` en `backend/api/models.py`.
    *   **Detalle:** Descomentar la relación `ForeignKey` a `prestadores.CategoriaPrestador`. Para resolver el error, cambiar la referencia de `ForeignKey('prestadores.CategoriaPrestador', ...)` a una "lazy relation" usando el formato de string `'prestadores.CategoriaPrestador'`. Esto aplaza la resolución de la dependencia hasta que sea estrictamente necesario, rompiendo el ciclo de importación durante la inicialización. Después de esto, se deberán generar y aplicar nuevas migraciones.

### Fase 2: Verificación Funcional del Flujo de Usuarios

1.  **Crear Usuarios de Prueba:**
    *   **Tarea:** Escribir y ejecutar scripts de `manage.py` o usar el shell de Django.
    *   **Detalle:** Crear al menos un usuario para cada uno de los roles principales (Admin Entidad, Prestador, Turista).
2.  **Probar el Flujo de Login y Registro:**
    *   **Tarea:** Realizar pruebas manuales o con Playwright.
    *   **Detalle:** Verificar que el registro funciona para cada rol y que el login redirige correctamente al dashboard correspondiente. Confirmar que la sesión de usuario persiste.
3.  **Probar la Funcionalidad del Dashboard:**
    *   **Tarea:** Navegar por todas las secciones del `Sidebar` para cada rol.
    *   **Detalle:** Asegurarse de que cada página se carga sin errores y que los componentes de la UI se renderizan correctamente. El objetivo no es probar la lógica de negocio completa, sino asegurar que la navegación y la estructura de la página son funcionales.

### Fase 3: Limpieza y Documentación

1.  **Resolver Advertencias del Backend:**
    *   **Tarea:** Actualizar `settings.py`.
    *   **Detalle:** Corregir las advertencias sobre `ACCOUNT_LOGIN_METHODS` y `STATICFILES_DIRS`.
2.  **Limpiar Dependencias del Frontend:**
    *   **Tarea:** Ejecutar `npm audit` y actualizar paquetes.
    *   **Detalle:** Atender las vulnerabilidades y advertencias de paquetes obsoletos para mejorar la seguridad y el mantenimiento del proyecto.
3.  **Añadir Documentación al Código:**
    *   **Tarea:** Revisar los archivos clave (modelos, contextos, servicios).
    *   **Detalle:** Añadir docstrings y comentarios donde la lógica sea compleja para facilitar el mantenimiento futuro.
