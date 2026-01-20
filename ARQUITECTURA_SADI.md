# Arquitectura de Preparación para SADI (Sistema de Acceso y Despliegue Inteligente)

## 1. Principio Rector

El sistema debe ser 100% operable a través de una capa de servicios desacoplada del frontend. Cada acción administrativa debe corresponder a una función `callable` en el backend. Esto asegura que cualquier interfaz, ya sea una UI web, una CLI o un agente de voz como SADI, pueda controlar el sistema de manera consistente.

## 2. Flujo de Datos para Operación por Voz

El flujo de ejecución para un comando de voz se conceptualiza de la siguiente manera:

1.  **Entrada de Voz**: El Administrador emite una orden (ej: "Sarita, publica la página de 'Quiénes Somos'").
2.  **SADI (Capa de Decisión)**:
    *   Interpreta la intención del lenguaje natural.
    *   Identifica el comando (`PUBLICAR_PAGINA`) y los parámetros (`slug='quienes-somos'`).
    *   Selecciona el endpoint de API apropiado para ejecutar la acción.
3.  **Llamada a la API de Sarita**: SADI realiza una petición `POST` al endpoint correspondiente (ej: `/api/admin/plataforma/paginas/quienes-somos/publicar/`).
4.  **Backend de Sarita (Capa de Ejecución)**:
    *   **Vista DRF**: Recibe la petición. Autentica al usuario y verifica los permisos (`IsAdminUser`).
    *   **Llamada al Servicio**: La vista, que es delgada, invoca a la función de servicio correspondiente (`gestion_contenidos_service.publicar_pagina(slug='quienes-somos', usuario=request.user)`).
    *   **Función de Servicio**: Contiene toda la lógica de negocio (cambiar el estado del modelo, validar, etc.). Es la única capa que modifica datos.
    *   **Respuesta**: El servicio devuelve un resultado, y la vista lo formatea como una respuesta HTTP.
5.  **Feedback a SADI**: SADI recibe la confirmación (`{ "status": "ok", "message": "Página 'Quiénes Somos' publicada con éxito." }`) y la comunica al Administrador.

## 3. Catálogo de Comandos Administrativos (Mapeo Voz -> Servicio)

Esta sección mapea los comandos de voz de alto nivel a las funciones de servicio que los ejecutarán.

### Gestión de Contenidos (Páginas Institucionales)

| Comando de Voz (Ejemplo) | Intención | Función de Servicio (Destino) | Estado Actual |
| :--- | :--- | :--- | :--- |
| "Publicar la página 'Quiénes Somos'" | PUBLICAR_PAGINA | `gestion_contenidos_service.publicar_pagina(slug, usuario)` | Pendiente de Crear |
| "Ocultar la página 'Contacto'" | OCULTAR_PAGINA | `gestion_contenidos_service.ocultar_pagina(slug, usuario)` | Pendiente de Crear |
| "Actualizar el título de la página '...' a '...'" | ACTUALIZAR_TITULO_PAGINA | `gestion_contenidos_service.actualizar_titulo(slug, nuevo_titulo, usuario)` | Pendiente de Crear |

### Gestión de Publicaciones (Blog, Noticias, Capacitaciones)

| Comando de Voz (Ejemplo) | Intención | Función de Servicio (Destino) | Estado Actual |
| :--- | :--- | :--- | :--- |
| "Aprobar la publicación '...'" | APROBAR_PUBLICACION | `api_services.aprobar_publicacion(publicacion_id, usuario)` | **Implementado** |
| "Rechazar la publicación '...'" | RECHAZAR_PUBLICACION | `api_services.rechazar_publicacion(publicacion_id, usuario)` | **Implementado** |
| "Enviar a aprobación la publicación '...'" | ENVIAR_A_APROBACION | `api_services.enviar_para_aprobacion(publicacion_id, usuario)` | **Implementado** |

### Gestión de Planes y Suscripciones

| Comando de Voz (Ejemplo) | Intención | Función de Servicio (Destino) | Estado Actual |
| :--- | :--- | :--- | :--- |
| "Crear un nuevo plan mensual llamado 'Premium' de 29.99" | CREAR_PLAN | `gestion_plataforma_service.crear_plan(...)` | Implementado (en ViewSet) |
| "Desactivar el plan 'Básico'" | DESACTIVAR_PLAN | `gestion_plataforma_service.desactivar_plan(plan_id, usuario)` | Pendiente de Crear |
| "Cambiar el precio del plan 'Premium' a 35.50" | CAMBIAR_PRECIO_PLAN | `gestion_plataforma_service.cambiar_precio_plan(plan_id, nuevo_precio, usuario)` | Pendiente de Crear |

### Configuración del Sitio

| Comando de Voz (Ejemplo) | Intención | Función de Servicio (Destino) | Estado Actual |
| :--- | :--- | :--- | :--- |
| "Activar la sección de atractivos en la página principal" | ACTIVAR_SECCION_HOME | `configuracion_service.set_seccion_activa('atractivos', True, usuario)` | Pendiente de Crear |
| "Cambiar el teléfono de contacto a '...'" | CAMBIAR_TELEFONO_CONTACTO | `configuracion_service.actualizar_configuracion({'telefono_movil': '...'}, usuario)` | Implementado (en View) |

---
*Este documento se actualizará a medida que se refactoricen las vistas y se creen los servicios correspondientes.*
