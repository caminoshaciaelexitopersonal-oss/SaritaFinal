# Auditoría Técnica de Rutas - Sistema Sarita

Este informe complementario detalla el estado de las rutas del backend (API Django) y del frontend (Next.js), centrándose en la sección "Mi Negocio". El análisis se basa en una revisión estática del código fuente.

## Resumen Global

-   **Total de Rutas de Backend Auditadas (Mi Negocio):** 5
-   **Rutas de Backend Funcionales:** 1
-   **Rutas de Backend en Construcción (Placeholder):** 4
-   ---
-   **Total de Rutas de Frontend Auditadas (Mi Negocio):** 16
-   **Rutas de Frontend Funcionales (con API):** 2
-   **Rutas de Frontend en Construcción (Placeholder/Sin API):** 14

**Observación General:** Se confirma una fuerte coherencia entre la arquitectura del backend y la del frontend. La mayoría de las rutas del frontend, aunque existen, dependen de endpoints del backend que aún no han sido implementados, lo que las convierte en marcadores de posición funcionales. El sistema de autenticación (`AuthContext`) es una dependencia crítica para el acceso a todas las rutas del dashboard.

---

## Auditoría de Rutas del Backend (API)

Las siguientes rutas se encuentran bajo el prefijo `/api/v1/mi-negocio/`.

| Módulo | Ruta | Estado | Código HTTP Esperado | Descripción / Observación |
| :--- | :--- | :--- | :--- | :--- |
| **Operativa** | `operativa/clientes/` | **Funcional** | 200 OK | Endpoint CRUD completo para la gestión de clientes. Implementa lógica multi-tenancy. |
| **Comercial** | `comercial/` | **En Construcción** | 200 OK | Placeholder. Devuelve una respuesta genérica indicando "módulo en desarrollo". |
| **Contable** | `contable/` | **En Construcción** | 200 OK | Placeholder. Devuelve una respuesta genérica indicando "módulo en desarrollo". |
| **Financiera** | `financiera/` | **En Construcción** | 200 OK | Placeholder. Devuelve una respuesta genérica indicando "módulo en desarrollo". |
| **Archivística**| `archivistica/` | **En Construcción** | 200 OK | Placeholder. Devuelve una respuesta genérica indicando "módulo en desarrollo". |

---

## Auditoría de Rutas del Frontend

Las siguientes rutas se encuentran bajo el prefijo `/dashboard/prestador/mi-negocio/`.

| Ruta | Estado | Componente(s) Principal(es) | Observaciones |
| :--- | :--- | :--- | :--- |
| `gestion-operativa/genericos/perfil/` | **En Construcción** | `page.tsx` (genérico) | Renderiza, pero depende de un endpoint de API para el perfil que no está implementado en `mi_negocio/urls.py`. |
| `gestion-operativa/genericos/productos-servicios/` | **En Construcción** | `page.tsx` (genérico) | Renderiza, pero la API correspondiente no está implementada. |
| `gestion-operativa/genericos/clientes/` | **Funcional** | `page.tsx` | Renderiza correctamente y se conecta con el endpoint funcional de la API. |
| `gestion-operativa/genericos/clientes/nuevo/` | **Funcional** | `page.tsx` | Renderiza el formulario para crear un nuevo cliente, que utiliza el endpoint funcional. |
| `gestion-operativa/genericos/reservas/` | **En Construcción** | `page.tsx` (genérico) | Renderiza, pero la API correspondiente no está implementada. |
| `gestion-operativa/genericos/valoraciones/` | **En Construcción** | `page.tsx` (genérico) | Renderiza, pero la API correspondiente no está implementada. |
| `gestion-operativa/genericos/documentos/` | **En Construcción** | `page.tsx` (genérico) | Renderiza, pero la API correspondiente no está implementada. |
| `gestion-operativa/genericos/galeria/` | **En Construcción** | `page.tsx` (genérico) | Renderiza, pero la API correspondiente no está implementada. |
| `gestion-operativa/genericos/estadisticas/` | **En Construcción** | `page.tsx` (genérico) | Renderiza, pero la API correspondiente no está implementada. |
| `gestion-operativa/genericos/inventario/` | **En Construcción** | `Inventario.tsx` | Renderiza, pero la API correspondiente no está implementada. |
| `gestion-operativa/genericos/costos/` | **En Construcción** | `Costos.tsx` | Renderiza, pero la API correspondiente no está implementada. |
| `gestion-operativa/especializados/...` | **En Construcción** | Varios | Rutas para hoteles, restaurantes, etc. Renderizan, pero sus APIs no están implementadas. |
| `gestion-comercial/` | **En Construcción** | `page.tsx` | Renderiza una página explícita de "módulo en desarrollo". |
| `gestion-contable/` | **En Construcción** | `page.tsx` | Renderiza una página explícita de "módulo en desarrollo". |
| `gestion-financiera/` | **En Construcción** | `page.tsx` | Renderiza una página explícita de "módulo en desarrollo". |
| `gestion-archivistica/` | **En Construcción** | `page.tsx` | Renderiza una página explícita de "módulo en desarrollo". |
