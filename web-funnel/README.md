# Funnel de Ventas de Sarita

## Estado Actual: Congelado (Fase A.3)

Este directorio contiene la maqueta estática para el funnel de ventas del sistema Sarita.

### Propósito

El propósito de este funnel es servir como el principal canal de adquisición de clientes para los productos de Sarita, dirigido tanto a **Empresarios Turísticos** como a **Entidades Gubernamentales**.

### Estado Técnico Actual

*   **Frontend:** El contenido de la carpeta `frontend/` es una **maqueta de HTML estático**. No está conectado a ninguna API y sus datos (como precios de planes) están escritos directamente en el código.
*   **Backend:** La aplicación de Django asociada (`backend/apps/web_funnel/`) es un CMS básico para gestionar el *contenido* de estas páginas, pero actualmente **no expone ninguna API** y no está conectada a la lógica de negocio principal (Planes y Suscripciones).

### Decisión Estratégica

En la **Fase A de Estabilización Estructural**, se ha tomado la decisión de **congelar conscientemente** el desarrollo de este componente.

*   **NO es deuda técnica activa:** No requiere mantenimiento ni corrección en la fase actual.
*   **ES un backlog estructurado:** Su funcionalidad se ha movido al backlog para ser abordada en una fase futura (`Fase B - Plataforma Comercial`).

### Futuro del Componente (Fase B)

El plan futuro para este funnel es reconstruirlo por completo:

1.  **Backend:** Desarrollar una API que exponga los planes de `admin_plataforma` y gestione un flujo de compra/suscripción.
2.  **Frontend:** Convertir las páginas estáticas en una aplicación dinámica (React/Next.js) que consuma la nueva API.

**No se debe realizar ninguna modificación sobre este componente hasta que comience la Fase B.**
