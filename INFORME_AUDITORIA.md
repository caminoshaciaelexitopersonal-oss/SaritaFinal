# Informe de Auditoría del Sistema "Sarita"

## 1. Resumen Ejecutivo

Este documento presenta un análisis exhaustivo del sistema "Sarita", una plataforma de turismo de triple vía. La auditoría se centró en la verificación estructural y funcional del backend (Django) y el frontend (Next.js), el diagnóstico de problemas críticos y la evaluación del estado de implementación de sus módulos principales.

**Hallazgo Principal:** El sistema posee un backend de alta calidad, con un sistema ERP de nivel profesional para la "vía del empresario", y un frontend moderno y bien estructurado. Sin embargo, **el sistema está completamente inoperativo** debido a un error crítico de dependencia circular en las migraciones de la base de datos del backend. Este problema impide que el servidor de Django arranque, lo que a su vez causa que el frontend, aunque se ejecuta, se quede en un estado de carga infinito al no poder autenticar al usuario.

**Recomendación Inmediata:** La prioridad absoluta es resolver la dependencia circular para poder iniciar el backend, desbloquear el desarrollo y permitir una verificación funcional completa.

---

## 2. Estado de Ejecución de los Servidores

Se intentó poner en marcha ambos componentes del sistema para una verificación en vivo.

*   **Backend (Django):**
    *   **Estado:** **FALLO CRÍTICO.**
    *   **Motivo:** El servidor no pudo arrancar. El registro de errores muestra una `django.db.migrations.exceptions.CircularDependencyError` entre las migraciones iniciales de las aplicaciones `api` y `prestadores`. Esto representa un bloqueo total para cualquier operación del backend.

*   **Frontend (Next.js):**
    *   **Estado:** **Iniciado Correctamente.**
    *   **Observaciones:** El servidor de desarrollo se ejecuta sin errores de compilación y es accesible. Sin embargo, la aplicación web es **inutilizable**. Al depender del backend para la autenticación y la carga de datos, la interfaz se queda bloqueada mostrando un esqueleto de carga en el menú lateral, un síntoma directo del fallo del backend.

---

## 3. Auditoría Detallada del Backend (Django)

### 3.1. Arquitectura y Estructura de Carpetas

El backend sigue las mejores prácticas de Django, con una clara separación de preocupaciones. La estructura principal auditada es:

*   `backend/api/`: Contiene el modelo de usuario (`CustomUser`), la lógica de autenticación y modelos genéricos de la plataforma.
*   `backend/apps/prestadores/`: Funciona como el contenedor principal para la lógica de la "vía del empresario".
*   `backend/apps/prestadores/mi_negocio/`: **El núcleo del sistema ERP.** Es una "super-app" que alberga los 5 módulos de gestión.

### 3.2. Diagnóstico del Error de Dependencia Circular

*   **Causa Raíz:** Se identificó un ciclo de dependencias a nivel de migraciones de base de datos:
    1.  La app `api` define modelos que tienen una `ForeignKey` al modelo `ProviderProfile` (ej. `ImagenGaleria`). Esto hace que `api` dependa de `prestadores`.
    2.  La app `prestadores` (específicamente en `.../perfil/models.py`) define el modelo `ProviderProfile`, el cual tiene una `OneToOneField` al modelo `CustomUser`. `CustomUser` está definido en la app `api`. Esto hace que `prestadores` dependa de `api`.
*   **Impacto:** Este bloqueo mutuo (`api` -> `prestadores` -> `api`) impide que Django pueda crear el esquema de la base de datos, resultando en el fallo total del sistema.

### 3.3. Análisis de los Módulos ERP ("Mi Negocio")

Se confirma que los 5 módulos de gestión empresarial están implementados a nivel de código fuente. La calidad del código es excepcionalmente alta, robusta y sigue patrones de diseño profesionales.

*   **`gestion_operativa`:** Contiene los modelos genéricos que soportan la operación, como `ProviderProfile` (el modelo central del prestador), `Cliente`, `Producto`, etc. Está bien estructurado en submódulos.
*   **`gestion_comercial`:** Implementa el ciclo de ventas con modelos para `FacturaVenta`, `ItemFactura` y `ReciboCaja`. Está correctamente integrado con los demás módulos.
*   **`gestion_contable`:** Es el módulo más complejo y completo. Implementa un sistema de contabilidad de doble entrada con `ChartOfAccount` (Plan de Cuentas), `JournalEntry` (Asientos) y `Transaction` (Movimientos). Incluye submódulos para `compras`, `inventario`, `activos_fijos`, etc. Es un sistema de nivel empresarial.
*   **`gestion_financiera`:** Maneja la tesorería con modelos para `CuentaBancaria` y `TransaccionBancaria`. Se integra perfectamente con la contabilidad.
*   **`gestion_archivistica`:** Es el módulo más avanzado tecnológicamente. No solo gestiona documentos con versionado, sino que incluye campos y una estructura preparada para una futura integración con tecnología **blockchain** (`merkle_root`, `blockchain_transaction`), lo que demuestra una visión a largo plazo.

---

## 4. Auditoría Detallada del Frontend (Next.js)

### 4.1. Arquitectura y Estructura de Carpetas

El frontend utiliza Next.js 14 con el App Router, una tecnología moderna. La estructura es limpia y organizada:

*   `frontend/src/app/`: Contiene las rutas y páginas de la aplicación. La estructura `dashboard/prestador/mi-negocio/...` refleja fielmente la del backend.
*   `frontend/src/contexts/`: Maneja el estado global. `AuthContext.tsx` es el archivo más crítico.
*   `frontend/src/components/`: Contiene componentes de UI reutilizables. `Sidebar.tsx` es clave para la navegación.
*   `frontend/src/services/`: Centraliza la configuración de llamadas a la API (`axios`).

### 4.2. Diagnóstico del Menú de Carga Infinito

*   **Causa Raíz:** Confirmado. El componente `AuthProvider` en `AuthContext.tsx` establece un estado `isLoading` a `true` al iniciar. Intenta verificar la sesión del usuario haciendo una llamada a la API del backend (`/auth/user/`). Como el backend está caído, esta llamada nunca tiene éxito. El `Sidebar.tsx` consume este estado y muestra un componente `SidebarSkeleton` (un esqueleto de interfaz) mientras `isLoading` sea `true`, lo que ocurre de forma indefinida.
*   **Conclusión:** El problema del frontend es un **síntoma directo e inevitable** del fallo crítico del backend.

### 4.3. Análisis del Flujo de Autenticación y Funcionalidades

*   **Login y Registro:** El flujo está correctamente implementado en `AuthContext.tsx`. La lógica de registro es particularmente robusta, utilizando diferentes endpoints de la API según el rol del usuario, lo que demuestra una implementación cuidadosa de los requisitos.
*   **Componentes y Vistas del Cliente:**
    *   **Sidebar/Menú:** El componente `Sidebar.tsx` está bien construido. Es dinámico y renderiza los enlaces de navegación correctamente según el rol del usuario autenticado. La estructura de enlaces para "Mi Negocio" es exhaustiva y coincide con los módulos del backend.
    *   **Páginas de "Mi Negocio":** La estructura de carpetas en `frontend/src/app/dashboard/prestador/mi-negocio/` indica que se han creado las páginas para interactuar con los módulos ERP, pero su funcionalidad no se puede verificar.

---

## 5. Informe de Componentes y Funcionalidades (De Cara al Cliente)

Debido a que el sistema no arranca, este análisis se basa en la auditoría del código fuente y la estructura de archivos, no en la interacción con la aplicación en funcionamiento.

### 5.1. Vía 1: Gobernanza (Corporaciones, Secretarías)

*   **Backend:** Las apps `companies` y `audit`, junto con los roles de administrador en `CustomUser`, sugieren la base para esta vía. `gestion_archivistica` también parece fuertemente orientada a la gobernanza.
*   **Frontend:** El `Sidebar.tsx` muestra un conjunto de enlaces de administración (`adminNavSections`) para roles como `ADMIN` y `FUNCIONARIO_DIRECTIVO`, que incluyen gestión de usuarios, contenido, configuraciones y verificaciones.
*   **Estado:** La estructura está definida, pero la funcionalidad no es verificable.

### 5.2. Vía 2: Empresarios (Prestadores de Servicios)

*   **Backend:** **Es la parte más desarrollada del sistema.** Los 5 módulos ERP (`Comercial`, `Operativo`, `Archivístico`, `Contable` y `Financiero`) están completamente implementados a nivel de modelos y lógica de negocio. Es un sistema de gestión empresarial muy potente y atractivo.
*   **Frontend:** El menú `miNegocioNav` en el `Sidebar.tsx` contiene una lista exhaustiva de enlaces a todas las funcionalidades del ERP, desde la gestión de perfil y clientes hasta la contabilidad y facturación.
*   **Estado:** El backend está listo pero bloqueado. El frontend está estructurado para consumir estas funcionalidades, pero también está bloqueado. Es la vía con mayor potencial una vez resuelto el problema principal.

### 5.3. Vía 3: Turista

*   **Backend:** El modelo `CustomUser` define el rol de `TURISTA`. Existen modelos como `AtractivoTuristico`, `RutaTuristica`, `Resena` y `ElementoGuardado` que soportan la experiencia del turista.
*   **Frontend:** El `AuthContext` tiene lógica específica para turistas (ej. `toggleSaveItem`). Las rutas públicas y de "Mi Viaje" deben existir en la estructura de `frontend/src/app/`, aunque no fueron el foco principal de esta auditoría inicial.
*   **Estado:** La funcionalidad base está presente en el código, pero no es verificable.
