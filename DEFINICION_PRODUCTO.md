# DEFINICIÓN DE PRODUCTO - "Sarita"

Este documento congela la definición del sistema "Sarita" como un producto, estableciendo su propósito, audiencia y alcance funcional para la versión actual.

## 1. ¿Qué problema resuelve?

"Sarita" resuelve la desarticulación y la falta de digitalización en el sector turístico de un destino. Centraliza la información para los turistas, proporciona herramientas de gestión modernas a los empresarios y ofrece a las entidades de gobernanza una plataforma para administrar y verificar el ecosistema turístico local.

## 2. ¿Para quién?

El producto está diseñado para tres audiencias principales (la "triple vía"):

1.  **Entidades de Gobernanza Turística:** Secretarías, direcciones o institutos de turismo a nivel municipal o departamental.
2.  **Empresarios y Prestadores de Servicios Turísticos:** Hoteles, restaurantes, agencias de viajes, guías, artesanos y otros actores comerciales del sector.
3.  **Turistas:** Visitantes nacionales o extranjeros que buscan descubrir, planificar y experimentar el destino turístico.

## 3. ¿Qué hace y qué NO hace?

**¿Qué hace?**

*   **Para la Gobernanza:** Permite gestionar contenido público (atractivos, rutas, eventos), administrar un directorio de prestadores y artesanos, y realizar verificaciones de cumplimiento a través de plantillas.
*   **Para los Empresarios:** Ofrece un ERP básico ("Mi Negocio") con módulos para gestionar operaciones, ventas (facturación), contabilidad (partida doble), inventario y finanzas.
*   **Para los Turistas:** Proporciona un portal web para explorar el destino, ver el directorio de servicios, encontrar eventos y guardar favoritos para planificar un viaje.
*   **Trazabilidad:** Registra eventos de negocio clave (como la creación de una factura) en un log de auditoría.

**¿Qué NO hace?**

*   **No procesa pagos reales:** El sistema registra órdenes de pago, pero no se integra con pasarelas de pago.
*   **No emite facturas electrónicas reales:** La integración con la DIAN es una simulación y está desactivada. El sistema genera una representación interna de la factura, no un documento fiscal válido.
*   **No realiza contabilidad fiscal avanzada:** El módulo contable es para gestión interna (contabilidad administrativa), no para la declaración de impuestos.
*   **No gestiona reservas en tiempo real de forma completa:** Permite registrar reservas, pero no gestiona inventario complejo de disponibilidad (ej. channel manager de hotel) ni bloqueos en tiempo real.
*   **No es un sistema de gestión de redes sociales:** No publica contenido automáticamente en plataformas externas.

## 4. ¿Qué módulos están oficialmente activos?

Para la versión actual, los siguientes módulos se declaran **activos y soportados**:

*   **Portal Público (Turista):**
    *   Descubre (Atractivos, Rutas, Eventos)
    *   Directorio (Prestadores, Artesanos)
    *   Mi Viaje (Elementos Guardados)
*   **Panel de Gobernanza (Admin):**
    *   Gestión de Contenido
    *   Gestión de Usuarios
    *   Verificación de Cumplimiento
*   **Panel de Empresario ("Mi Negocio"):**
    *   Gestión Operativa
    *   Gestión Comercial
    *   Gestión Contable
    *   Gestión Archivística
    *   Gestión Financiera
