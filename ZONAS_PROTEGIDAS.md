
# Zonas Protegidas del Sistema Sarita

**Última actualización:** 2024-07-27

## 1. Propósito

Este documento define las áreas del código fuente que se consideran **críticas y estables**, y que están **estrictamente prohibidas de modificar, renombrar o eliminar** sin un proceso de revisión y aprobación excepcional.

El objetivo es proteger los activos visuales, la configuración de marketing y la lógica de negocio del backend que actualmente está en producción y funcionando correctamente para los roles de `Prestador` y `Turista`.

## 2. Regla Operativa General

**Todas las carpetas y archivos listados a continuación son de SOLO LECTURA.**

Cualquier nuevo desarrollo que necesite interactuar con estos activos debe consumirlos tal como están, sin alterarlos.

## 3. Zonas Protegidas en el Frontend

### 3.1. Activos Visuales y Multimedia

Estas carpetas contienen el branding, los logos, las imágenes de marketing, los íconos y otros elementos visuales que son fundamentales para la identidad del sistema.

-   `frontend/public/**`
-   `frontend/assets/**`
-   `frontend/media/**`

### 3.2. Carpetas de Módulos de Cara al Público

Las siguientes carpetas contienen la lógica y presentación de las secciones públicas del sitio. Su alteración podría impactar directamente la experiencia del turista.

-   `frontend/src/app/descubre/**`
-   `frontend/src/app/directorio/**`
-   `frontend/src/app/mi-viaje/**`

## 4. Zonas Protegidas en el Backend

### 4.1. Lógica de Negocio Existente

El backend actual que da servicio a los prestadores, turistas y al sitio público no debe ser modificado. Esto incluye:

-   **Modelos:** No se deben alterar los esquemas de la base de datos existentes.
-   **Migraciones:** No se deben generar migraciones que modifiquen o eliminen tablas o columnas existentes.
-   **APIs Productivas:** No se deben cambiar los endpoints, serializers o vistas que están actualmente en uso por el frontend. Las rutas afectadas incluyen, pero no se limitan a:
    -   `/api/auth/`
    -   `/api/v1/mi-negocio/`
    -   `/api/public/` (si aplica)

## 5. Justificación

Estas zonas se protegen para:

-   **Prevenir Regresiones:** Evitar que nuevos desarrollos rompan funcionalidades existentes y probadas.
-   **Mantener la Integridad Visual:** Asegurar que la identidad de marca y los materiales de marketing permanezcan consistentes.
-   **Permitir el Desarrollo en Paralelo:** Facilitar la construcción del nuevo panel de administración sin interferir con el sistema en producción.

Cualquier necesidad de modificar estas zonas debe ser tratada como un cambio arquitectónico mayor y seguir un proceso de aprobación riguroso.
