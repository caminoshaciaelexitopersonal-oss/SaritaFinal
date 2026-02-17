# Modelo de Datos Comercial

Este documento describe la arquitectura de backend para el flujo de comercio electrónico del sistema Sarita, desde la selección del producto hasta el pago.

## Principios

-   **Modularidad:** Cada concepto (Planes, Carro, Pagos) reside en su propia app de Django.
-   **Trazabilidad:** Cada paso del proceso de compra genera un registro en la base de datos.
-   **Agnosticismo del Proveedor:** El sistema de pagos está diseñado para no depender de una única pasarela.

## Entidades Principales y Flujo de Datos

El flujo comercial sigue una secuencia lógica a través de varios modelos:

### 1. `Plan` (`apps.admin_plataforma.models`)
-   **Definición:** Es el **Producto** que se vende. Representa una suscripción al software de Sarita.
-   **Atributos Clave:** `nombre`, `precio`, `frecuencia`, `tipo_usuario_objetivo`.
-   **Gobernabilidad:** Es gestionado completamente por el Administrador de la Plataforma a través de la API `/api/admin/plataforma/planes/`.

### 2. `Cart` y `CartItem` (`apps.cart.models`)
-   **Definición:** Representan la **Orden** en estado de preparación. Es el espacio temporal donde un usuario reúne los planes que desea comprar.
-   **Flujo:**
    1.  Un usuario (autenticado) ve los `Planes` en una página pública (ej. `/decision`).
    2.  Al hacer clic en "Añadir al Carro", el frontend llama a la API `/api/cart/add-item/`.
    3.  El `CartService` del backend crea (o actualiza) un `CartItem` que asocia el `Plan` seleccionado con el `Cart` del usuario.

### 3. `Payment` (`apps.payments.models`)
-   **Definición:** Representa la **Transacción de Pago**. Es el registro auditable de cada intento de compra.
-   **Flujo:**
    1.  El usuario revisa su carro en la página `/checkout`.
    2.  Al hacer clic en "Proceder al Pago", el frontend llama a la API `/api/payments/init/`.
    3.  El `PaymentService` del backend:
        a.  Calcula el monto total del `Cart`.
        b.  Crea una instancia de `Payment` con estado `INIT` y la asocia al `Cart`.
        c.  (Futuro, Fase D) Se comunica con la pasarela de pago externa y actualiza el estado a `PENDING`.

### 4. `Suscripcion` (`apps.admin_plataforma.models`)
-   **Definición:** Es el resultado final de una compra exitosa. Otorga al usuario acceso a las funcionalidades del `Plan` que compró.
-   **Flujo (Futuro, Fase D):**
    1.  La pasarela de pago notifica al backend (vía webhook en `/api/webhooks/confirm/`) que el pago fue exitoso.
    2.  El `PaymentService` actualiza el `Payment` a estado `PAID`.
    3.  **Se crea una instancia de `Suscripcion`**, asociando al `Usuario` con el `Plan` comprado, con una fecha de inicio y fin.
    4.  El `Cart` del usuario se vacía.

## Diagrama Conceptual del Flujo
```
[Página de Planes (Funnel)]
       |
       v (Usuario añade un Plan)
[Carro de Compras (Cart)]
       |
       v (Usuario procede al pago)
[Registro de Pago (Payment)]
       |
       v (Confirmación de pago exitoso)
[Suscripción Activa (Suscripcion)]
```

Esta arquitectura modular y secuencial asegura que el proceso comercial sea robusto, escalable y fácil de auditar, sentando una base sólida para la implementación de las pasarelas de pago en la Fase D.
