# Módulo "Mi Negocio" - Frontend

Esta carpeta contiene toda la implementación de React (Next.js) para el panel de administración "Mi Negocio", exclusivo para usuarios con el rol de "prestador".

## Estructura de Carpetas

-   **/gestion-operativa**: Contiene los módulos para la gestión del día a día del negocio.
    -   **/genericos**: Módulos aplicables a cualquier tipo de prestador (Perfil, Clientes, Productos, etc.).
    -   **/especializados**: Módulos específicos para ciertos tipos de negocio (ej. `hoteles/Habitaciones`, `restaurantes/Menu`).
-   **/gestion-comercial**: (Placeholder) Futuros módulos de marketing y ventas.
-   **/gestion-contable**: (Placeholder) Futuros módulos de contabilidad.
-   **/gestion-financiera**: (Placeholder) Futuros módulos de finanzas.
-   **/gestion-archivistica**: (Placeholder) Futuros módulos de gestión documental.
-   **/componentes**: Componentes reutilizables específicos para el panel "Mi Negocio".
-   **/hooks**: Hooks de React para manejar la lógica y el estado, como las llamadas a la API.

## Lógica de Datos

La interacción con el backend se centraliza a través del hook `useMiNegocioApi.ts`, que utiliza una instancia de Axios configurada para comunicarse con el API de Django en `/api/v1/prestadores/mi_negocio/`.
