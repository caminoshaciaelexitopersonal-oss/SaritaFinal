# Voice-Ready Functionality Map (SADI)

Este documento identifica los flujos de negocio del sistema Sarita que están preparados para ser operados por un sistema de voz como SADI, gracias a su arquitectura de servicios desacoplada.

## Principio Arquitectónico para SADI

Una función está "lista para voz" (`voice-ready`) si su lógica de negocio principal está encapsulada en un **método de servicio** que:
1.  **No depende del objeto `request` de Django/DRF.** Acepta parámetros simples y primitivos (IDs, strings, números).
2.  **Es semántico.** Su nombre describe claramente la acción de negocio (ej. `add_item_to_cart`).
3.  **Es autocontenido.** Contiene toda la lógica y validaciones de negocio, sin depender de la capa de la vista (API).

Esta arquitectura permite que un controlador de voz (como SADI) y un controlador de API (un `ViewSet` de DRF) sean simplemente dos "clientes" diferentes que consumen el mismo servicio de negocio.

## Mapa de Funcionalidades "Voice-Ready"

### Módulo: Carro de Compras (`apps.cart.services.CartService`)
-   **`get_or_create_cart(user)`**
    -   **Comando SADI (Ejemplo):** "Muéstrame mi carro de compras."
    -   **Estado:** `LISTO`.
-   **`add_item_to_cart(user, plan_id, quantity)`**
    -   **Comando SADI (Ejemplo):** "Añade el plan 'premium' a mi carro."
    -   **Estado:** `LISTO`.
-   **`remove_item_from_cart(user, item_id)`**
    -   **Comando SADI (Ejemplo):** "Elimina el último ítem de mi carro."
    -   **Estado:** `LISTO`.

### Módulo: Pagos (`apps.payments.services.PaymentService`)
-   **`initiate_payment(cart, provider)`**
    -   **Comando SADI (Ejemplo):** "Inicia el pago de mi carro con Wompi."
    -   **Estado:** `LISTO`.
-   **`confirm_payment(transaction_id, status)`**
    -   **Comando SADI (Ejemplo):** "Confirma el pago 'xyz' como pagado."
    -   **Estado:** `LISTO`.
-   **`get_payment_status(payment_id)`**
    -   **Comando SADI (Ejemplo):** "Cuál es el estado del pago 123?"
    -   **Estado:** `LISTO`.

### Módulo: Gestión de Planes (CRUD vía API)
-   **Acciones:** Crear, editar, activar/desactivar planes.
-   **Flujo SADI:** Un comando de voz como "Crea un nuevo plan mensual para prestadores a 99 dólares" se traduciría en una llamada `POST` a la API `/api/admin/plataforma/planes/`.
-   **Estado:** `LISTO`. La lógica CRUD simple dentro de los `ModelViewSet` es suficientemente atómica para ser considerada "voice-ready". No se requiere un servicio separado para estas operaciones básicas.

### Módulo: Gobernabilidad Web (CRUD vía API)
-   **Acciones:** Crear/publicar página, añadir sección, etc.
-   **Flujo SADI:** "Publica la página con slug 'inicio'." se traduciría en una llamada `PATCH` a `/api/web/admin/pages/inicio/` con `{ "is_published": true }`.
-   **Estado:** `LISTO`. Similar a la gestión de planes, la naturaleza CRUD de la gobernabilidad web es directamente compatible con una operación por voz que invoque a la API.

## Conclusión

La arquitectura basada en servicios que se ha implementado en la Fase B asegura que los flujos de negocio más críticos y complejos ya están desacoplados de la interfaz web. Esto proporciona una base sólida para la futura integración de SADI, que podrá invocar estos servicios directamente sin necesidad de refactorizar la lógica de negocio existente.
