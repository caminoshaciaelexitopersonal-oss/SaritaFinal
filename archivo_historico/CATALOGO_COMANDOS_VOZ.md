# Catálogo de Comandos de Voz para SADI

Este documento define el alcance inicial de los comandos de voz que el sistema SADI es capaz de interpretar y ejecutar. Cada comando está clasificado por su nivel de criticidad para determinar si requiere confirmación explícita del usuario antes de la ejecución.

## Niveles de Criticidad

*   **Lectura (Bajo):** Comandos que solo consultan información y no modifican el estado del sistema. No requieren confirmación.
*   **Escritura (Medio):** Comandos que crean o modifican datos de una manera no destructiva. Requieren confirmación por defecto.
*   **Crítico (Alto):** Comandos que realizan acciones destructivas o difíciles de revertir (ej. eliminaciones, desactivaciones permanentes). Siempre requieren confirmación.

---

## Módulo: Gestión de Planes y Suscripciones

| Comando de Voz (Ejemplo) | Intención | Parámetros | Criticidad | Servicio Ejecutor |
| :--- | :--- | :--- | :--- | :--- |
| "Crea un nuevo plan" | `CREAR_PLAN` | `nombre`, `precio`, `frecuencia` | Escritura | `gestion_plataforma_service` |
| "Desactiva el plan 'Básico'" | `DESACTIVAR_PLAN` | `id_plan` | Crítico | `gestion_plataforma_service` |
| "Cambia el precio del plan 'Premium' a 35.50" | `CAMBIAR_PRECIO_PLAN` | `id_plan`, `nuevo_precio` | Escritura | `gestion_plataforma_service` |
| "Muéstrame los planes activos" | `LISTAR_PLANES_ACTIVOS` | - | Lectura | `gestion_plataforma_service` |

## Módulo: Gestión de Contenidos (Páginas Institucionales)

| Comando de Voz (Ejemplo) | Intención | Parámetros | Criticidad | Servicio Ejecutor |
| :--- | :--- | :--- | :--- | :--- |
| "Publica la página 'Quiénes Somos'" | `PUBLICAR_PAGINA` | `slug_pagina` | Escritura | `gestion_contenidos_service` |
| "Oculta la página 'Contacto'" | `OCULTAR_PAGINA` | `slug_pagina` | Escritura | `gestion_contenidos_service` |
| "Actualiza el título de la página '...' a '...'" | `ACTUALIZAR_TITULO_PAGINA` | `slug_pagina`, `nuevo_titulo` | Escritura | `gestion_contenidos_service` |
| "¿Cuál es el estado de la página 'Blog'?" | `CONSULTAR_ESTADO_PAGINA` | `slug_pagina` | Lectura | `gestion_contenidos_service` |

## Módulo: Gestión de Publicaciones (Blog, Noticias)

| Comando de Voz (Ejemplo) | Intención | Parámetros | Criticidad | Servicio Ejecutor |
| :--- | :--- | :--- | :--- | :--- |
| "Aprobar la publicación con ID 123" | `APROBAR_PUBLICACION` | `id_publicacion` | Escritura | `api_services` |
| "Rechazar la publicación '...'" | `RECHAZAR_PUBLICACION` | `id_publicacion` | Escritura | `api_services` |
| "Enviar a aprobación la publicación '...'" | `ENVIAR_A_APROBACION` | `id_publicacion` | Escritura | `api_services` |
| "Listar publicaciones pendientes de revisión" | `LISTAR_PUBLICACIONES_PENDIENTES` | - | Lectura | `api_services` |

## Módulo: Configuración del Sitio

| Comando de Voz (Ejemplo) | Intención | Parámetros | Criticidad | Servicio Ejecutor |
| :--- | :--- | :--- | :--- | :--- |
| "Activar la sección de atractivos en la home" | `ACTIVAR_SECCION_HOME` | `nombre_seccion` | Escritura | `configuracion_service` |
| "Cambiar el teléfono de contacto a '...'" | `CAMBIAR_TELEFONO_CONTACTO` | `nuevo_telefono` | Escritura | `configuracion_service` |

---
*Este catálogo es un documento vivo y se expandirá a medida que se incorporen nuevas capacidades de voz al sistema.*
