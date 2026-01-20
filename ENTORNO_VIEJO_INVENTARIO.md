
# Inventario Funcional del Entorno Viejo (Admin Panel)

**Fecha:** 2024-07-27
**Autor:** Jules, Ingeniero de Software IA

## 1. Propósito

Este documento realiza un inventario de alto nivel del antiguo panel de administración (`backend/apps/admin_panel/` y `frontend/src/app/dashboard/admin/`) para guiar la migración controlada de funcionalidades al nuevo entorno (`admin_plataforma`).

El objetivo no es un análisis exhaustivo, sino una clasificación arquitectónica para justificar la estrategia de "reescritura" sobre la de "reutilización".

## 2. Análisis Arquitectónico del Backend (`apps/admin_panel/`)

El análisis de la estructura de archivos revela varios problemas fundamentales:

1.  **Inconsistencia Estructural:** No hay un patrón de diseño coherente. `supervision_comercial` utiliza una capa de `presentation`, mientras que `supervision_financiera` mezcla vistas y serializadores de "admin" en el mismo nivel. Esta inconsistencia hace que el mantenimiento y la extensibilidad sean extremadamente difíciles.
2.  **Acoplamiento Fuerte:** Los módulos internos (`activos_fijos`, `nomina`, etc.) fueron claramente copiados de `mi_negocio` y adaptados, heredando el alto acoplamiento. La lógica de negocio está dispersa entre vistas, modelos y, a veces, servicios.
3.  **Estado de Refactorización a Medias:** Los nombres de las carpetas (`supervision_*`) y los archivos de prueba (`_obsoleto_test_*.py`) indican que hubo intentos de refactorización que no se completaron, dejando el código en un estado inestable y poco confiable.
4.  **Suposición Arquitectónica Rota:** El núcleo del problema, como se identificó en la auditoría inicial, es que toda la estructura asume que "Admin" es solo una variante de "Prestador", reutilizando modelos y flujos que no aplican a la gestión de una plataforma.

## 3. Clasificación General de Componentes

Dada la inconsistencia y el acoplamiento, se aplica una clasificación general en lugar de un análisis pieza por pieza:

-   **Endpoints y Vistas:** 🔴 **Obsoletos / Peligrosos**.
    *   **Justificación:** Están fuertemente acoplados a modelos y permisos incorrectos. Intentar reutilizarlos introduciría los mismos errores estructurales en el nuevo sistema. Deben ser reescritos desde cero.

-   **Serializers:** 🔴 **Obsoletos / Peligrosos**.
    *   **Justificación:** Al igual que las vistas, están diseñados para los modelos del prestador y no para el nuevo contexto del administrador de la plataforma. El contrato de la API debe ser rediseñado, no copiado.

-   **Modelos:** 🔴 **Obsoletos**.
    *   **Justificación:** El antiguo panel de admin no tiene modelos propios; abusa de los modelos del prestador. Los nuevos modelos (`Plan`, `Suscripcion`, etc.) ya han comenzado a crearse correctamente en la app `admin_plataforma`.

-   **Lógica de Negocio (en `services` u otros):** 🟡 **Reescribible**.
    *   **Justificación:** Esta es la única área donde puede haber valor rescatable. La lógica de negocio pura (ej. cálculos, validaciones) puede ser extraída cuidadosamente, auditada y re-implementada dentro de los nuevos servicios desacoplados, como `GestionPlataformaService`. **Nunca se debe copiar el archivo completo.**

## 4. Análisis del Frontend (`/dashboard/admin/`)

El frontend del antiguo panel de administración sufre del mismo problema fundamental: es una copia directa del panel del prestador.

-   **Componentes y Páginas:** 🔴 **Obsoletos / Peligrosos**.
    *   **Justificación:** Todos los componentes, hooks y páginas están diseñados para el flujo de un `Prestador`. Reutilizarlos es inviable y peligroso, ya que apuntan a APIs incorrectas y manejan un estado que no corresponde al del administrador.

## 5. Conclusión y Estrategia de Migración

El "entorno viejo" del panel de administración no es una base fiable para la migración. Su estructura es inconsistente, está a medio refactorizar y se basa en una suposición arquitectónica fundamentalmente incorrecta.

**Estrategia Confirmada:**

1.  **NO se reutilizará ningún componente de capa de presentación** (vistas, serializers, componentes de UI) del entorno viejo.
2.  La **lógica de negocio pura** se identificará y se **reescribirá** dentro de los nuevos servicios aislados (`GestionPlataformaService` y futuros).
3.  Todo el desarrollo se centrará en el nuevo entorno (`admin_plataforma`), tratando el entorno viejo únicamente como una **fuente de consulta de SOLO LECTURA** para entender los requisitos funcionales que deben ser implementados correctamente.
