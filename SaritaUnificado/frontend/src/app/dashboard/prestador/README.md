# Arquitectura del Panel del Prestador

Esta sección de la aplicación contiene toda la interfaz de usuario para el panel de administración del rol "Prestador de Servicios Turísticos".

## Estructura "Mi Negocio"

Siguiendo el principio de **Arquitectura Limpia y Centrada en el Dominio**, toda la funcionalidad del panel se ha agrupado bajo la ruta `/dashboard/prestador/mi-negocio`.

Esta carpeta está organizada de la siguiente manera:

*   `/gestion-operativa/`: Contiene las páginas para la gestión diaria del negocio.
    *   `/genericos/`: Módulos comunes a todos los prestadores (Perfil, Productos, Clientes, etc.). Cada módulo tiene su propia subcarpeta.
    *   `/especializados/`: Módulos específicos por categoría de prestador. La lógica para mostrar estos módulos se encuentra en el `Sidebar.tsx`, que lee la categoría del perfil del usuario.
*   `/gestion-comercial/`: (Placeholder) Páginas futuras para marketing y ventas.
*   `/gestion-contable/`: (Placeholder) Páginas futuras para facturación y finanzas.

### Hooks de API

*   `src/hooks/useMiNegocioApi.ts`: (Placeholder) Este hook está destinado a centralizar toda la lógica de obtención y envío de datos para el panel "Mi Negocio", simplificando el manejo de estado, caché y sincronización en el futuro.