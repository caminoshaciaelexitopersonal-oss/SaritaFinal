# Arquitectura de la API de SaritaUnificado

Esta aplicación (`api`) funciona como el núcleo central del backend de SaritaUnificado.

## Decisión de Diseño #01 — Refactorización Lógica del Backend

Para mejorar la mantenibilidad y escalabilidad, se ha adoptado un enfoque de **refactorización lógica** en lugar de una refactorización física completa.

**Justificación:**

*   **Estabilidad:** Se mantienen las aplicaciones Django existentes (`api`, `empresa`, `turismo`, `restaurante`) para evitar romper dependencias y migraciones de base de datos complejas.
*   **Claridad:** La lógica de negocio se organiza dentro de cada aplicación mediante comentarios y secciones en los archivos `views.py` y `serializers.py`.
*   **Escalabilidad:** Se ha creado un punto de entrada unificado para toda la API del panel del prestador bajo la ruta `/api/v1/prestadores/`.

### Estructura de Rutas del Panel "Mi Negocio"

Toda la funcionalidad del panel del prestador se agrupa bajo `/api/v1/prestadores/mi-negocio/`, gestionado por el archivo `api/urls_prestador.py`. La estructura es la siguiente:

*   `/operativa/`: Contiene los endpoints para la gestión diaria del negocio.
    *   `/genericos/*`: Rutas para módulos comunes a todos los prestadores (Perfil, Productos, Clientes, etc.).
    *   `/especializados/*`: Rutas para módulos específicos por categoría (Hoteles, Restaurantes, etc.).
*   `/comercial/`: (Placeholder) Futuros endpoints para marketing y ventas.
*   `/contable/`: (Placeholder) Futuros endpoints para facturación y finanzas.