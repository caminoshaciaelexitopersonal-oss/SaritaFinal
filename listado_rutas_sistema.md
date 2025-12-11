# Listado A — Todas las rutas del sistema (Final)

| Tipo | Método | Ruta | Archivo | Estado | Uso detectado | Observaciones |
|---|---|---|---|---|---|---|
| Frontend | Navegación | `/dashboard/prestador/mi-negocio/comercial/facturas-venta` | `facturas-venta/page.tsx` | Activa | - | Módulo "Mi Negocio". |
| Frontend | API Call | `GET /v1/mi-negocio/comercial/facturas-venta/` | `useComercialApi.ts` | **Corregida** | - | Se añadió `/v1/` para interoperabilidad. |
| Backend | GET, POST | `/api/v1/mi-negocio/comercial/facturas-venta/` | `gestion_comercial/urls.py` | Activa | `useComercialApi.ts` | Interoperabilidad corregida. |
| Backend | GET, PUT, PATCH, DELETE | `/api/v1/mi-negocio/comercial/facturas-venta/{id}/` | `gestion_comercial/urls.py` | **Activa (No Usada)** | - | Generada por `DefaultRouter`, pero sin llamadas detectadas desde los `hooks`. |
| Backend | Múltiples | `/api/prestadores/categorias/` | `api/urls.py` | Activa | `registro/page.tsx` | **Fuera de Mi Negocio.** Usada en el flujo de registro y formularios. |
| Backend | Múltiples | `/api/admin/users/` | `api/urls.py` | Activa | `api.ts` | **Fuera de Mi Negocio.** Endpoint para administración. |
| Backend | Múltiples | `/api/v1/mi-negocio/operativa/transportes/` | `modulos_genericos/urls.py` | **Duplicada Parcial** | - | Candidata a eliminación. Ver Listado B. |
| Backend | Múltiples | `/api/v1/mi-negocio/operativa/transporte/` | `modulos_genericos/urls.py` | **Duplicada Parcial** | - | Candidata a eliminación. Ver Listado B. |
| Backend | Múltiples | `/api/v1/mi-negocio/operativa/agencias-viajes/` | `modulos_genericos/urls.py` | **Inactiva** | - | Comentada. Candidata a eliminación. Ver Listado B. |
