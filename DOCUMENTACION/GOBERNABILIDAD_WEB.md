# Modelo de Gobernabilidad del Contenido Web

Este documento describe la arquitectura de backend que permite al Administrador de la Plataforma tener control total sobre el contenido del sitio web público, incluyendo el embudo de ventas.

## Principio Arquitectónico

**El contenido web no está hardcodeado.** Todo lo que ve el usuario público es servido dinámicamente a través de APIs y es gestionado desde el panel de `admin_plataforma`.

## Componentes del Modelo

### 1. `WebPage` (apps.web_funnel.models)
-   **Propósito:** Representa una página individual (ej. "Inicio", "Precios", "/downloads").
-   **Atributos Clave:**
    -   `title`: El título principal de la página.
    -   `slug`: El identificador único usado en la URL (ej. `http://sarita.com/inicio`).
    -   `is_published`: Un booleano que permite al admin poner la página "en línea" o mantenerla como borrador.

### 2. `Section` (apps.web_funnel.models)
-   **Propósito:** Divide una `WebPage` en secciones horizontales ordenables (ej. "Hero", "Beneficios", "Testimonios").
-   **Atributos Clave:**
    -   `web_page`: `ForeignKey` que la asocia a una `WebPage`.
    -   `title`: Título de la sección (ej. "Nuestros Planes").
    -   `order`: Un entero para definir el orden vertical de las secciones.

### 3. `ContentBlock` (apps.web_funnel.models)
-   **Propósito:** Es la unidad de contenido más pequeña, dentro de una `Section`.
-   **Atributos Clave:**
    -   `section`: `ForeignKey` que lo asocia a una `Section`.
    -   `content_type`: Define el tipo de bloque (`text`, `image`, `video`, `button`).
    -   `content`: El contenido real (el texto, la URL de una imagen, etc.).
    -   `link`: Un campo opcional para URLs (ej. el destino de un botón).
    -   `order`: Un entero para definir el orden de los bloques dentro de una sección.

### 4. `MediaAsset` (apps.web_funnel.models)
-   **Propósito:** Una librería central de medios. Permite subir un archivo una vez y reutilizarlo.
-   **Flujo:** El admin sube un archivo para crear un `MediaAsset`. Luego, en un `ContentBlock` de tipo `image`, copia la URL de este activo en el campo `content`.

### 5. `DownloadLink` (apps.downloads.models)
-   **Propósito:** Gestiona específicamente los enlaces de descarga de aplicaciones.
-   **Atributos Clave:**
    -   `plataforma`: (Google Play, Windows, etc.).
    -   `url`: El enlace directo al archivo o tienda.
    -   `is_active`: Permite activar o desactivar un enlace sin borrarlo.

## Flujo de Trabajo del Administrador

1.  **Crear Página:** El admin crea una nueva `WebPage` (ej. "Página de Consideración", slug `consideracion`).
2.  **Añadir Secciones:** A esta página, añade `Sections` ordenadas (ej. "Testimonios", "Casos de Éxito").
3.  **Poblar Contenido:** Dentro de cada sección, añade `ContentBlocks` (texto, imágenes, botones de CTA).
4.  **Publicar:** Marca `is_published` como `True`.
5.  **Visualización:** El frontend dinámico lee la API pública (`/api/web/public/pages/consideracion/`) y renderiza la página con sus secciones y bloques en el orden especificado.

Este modelo proporciona un control total y granular sobre el contenido web sin requerir conocimientos de código, cumpliendo con los principios arquitectónicos de la Fase B.
