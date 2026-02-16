# Informe de Auditoría Técnica de Rutas - Sistema Sarita

Este informe detalla el estado de las rutas del backend (Django) y frontend (Next.js), con un enfoque en el módulo "Mi Negocio". El análisis se realizó de forma estática, revisando el código fuente para determinar la funcionalidad potencial sin ejecutar los servidores.

## Backend (Django)

**Observación Crítica:** La configuración de enrutamiento principal en `backend/puerto_gaitan_turismo/urls.py` está **ROTA**. Intenta cargar las rutas desde `apps.mi_negocio`, pero la ubicación correcta del módulo es `apps.prestadores.mi_negocio`. Esta es la causa raíz por la que ninguna ruta de la API `api/v1/mi-negocio/` funcionaría sin una corrección.

### Tabla de Rutas de `mi_negocio`

| Módulo | Ruta | Estado | Código HTTP (potencial) | Descripción / Observación |
| :--- | :--- | :--- | :--- | :--- |
| `gestion_operativa` | `/operativa/clientes/` | **Funcional** | 200 OK | Conectado a una `ClienteViewSet` completa con lógica de negocio y seguridad (multi-tenancy). |
| `gestion_contable` | `/contabilidad/cost-centers/` | **Roto** | 500 Server Error | La `ViewSet` se importa desde la app `contabilidad`, la cual no existe. |
| `gestion_contable` | `/contabilidad/chart-of-accounts/` | **Roto** | 500 Server Error | La `ViewSet` se importa desde la app `contabilidad`, la cual no existe. |
| `gestion_contable` | `/contabilidad/journal-entries/` | **Roto** | 500 Server Error | La `ViewSet` se importa desde la app `contabilidad`, la cual no existe. |
| `gestion_comercial` | `/comercial/` | **Roto** | 500 Server Error | Incluye las URLs de la app `comercial`, la cual no existe. |
| `gestion_financiera`| `/contabilidad/tesoreria/` | **Roto** | 500 Server Error | Incluye las URLs de la app `financiera`, la cual no existe. |
| `gestion_archivistica`| `/archivistica/` | **En Construcción** | 200 OK | Apunta a una `PlaceholderView` genérica. No tiene funcionalidad real. |
| N/A | `/compras/` | **Roto** | 500 Server Error | Incluye las URLs de la app `compras`, la cual no existe. |
| N/A | `/inventario/` | **Roto** | 500 Server Error | Incluye las URLs de la app `inventario`, la cual no existe. |
| N/A | `/activos/` | **Roto** | 500 Server Error | Incluye las URLs de la app `activos`, la cual no existe. |
| N/A | `/nomina/` | **Roto** | 500 Server Error | Incluye las URLs de la app `nomina`, la cual no existe. |
| N/A | `/proyectos/` | **Roto** | 500 Server Error | Incluye las URLs de la app `proyectos`, la cual no existe. |

---

## Frontend (Next.js)

**Observación Crítica:** El hook central `useMiNegocioApi.ts` contiene múltiples llamadas a endpoints del backend que están rotos. Además, depende críticamente del `AuthContext` para obtener un token de autenticación. Un fallo en el login o en el token impediría que cualquier componente funcional renderice datos, resultando en un estado de "carga infinita".

### Tabla de Rutas de `mi-negocio`

| Ruta | Estado | Componente principal | Observaciones |
| :--- | :--- | :--- | :--- |
| `/gestion-operativa/genericos/clientes` | **Roto** | `ClientesPage` | La página está bien construida pero llama a un endpoint incorrecto (`.../genericos/clientes/` en vez de `.../clientes/`). Esto probablemente resultaría en una carga infinita o un error. |
| `/gestion-comercial` | **En Construcción** | `GestionComercialPage` | Renderiza correctamente una página estática que indica que el módulo está en desarrollo. No hay funcionalidad. |
| `/gestion-contable` | **En Construcción** | `GestionContablePage` | Renderiza correctamente una página estática que indica que el módulo está en desarrollo. No hay funcionalidad. |
| `/gestion-financiera` | **En Construcción** | `GestionFinancieraPage` | Renderiza correctamente una página estática que indica que el módulo está en desarrollo. No hay funcionalidad. |
| `/gestion-archivistica` | **En Construcción** | `GestionArchivisticaPage` | Renderiza correctamente una página estática que indica que el módulo está en desarrollo. No hay funcionalidad. |

---

## Resumen Global

- **Total de Rutas de Backend Auditadas:** 12
  - **Rutas Funcionales:** 1 (8.3%)
  - **Rutas Rotas:** 10 (83.3%)
  - **Rutas en Construcción:** 1 (8.3%)

- **Total de Rutas de Frontend Auditadas:** 5
  - **Rutas Funcionales:** 0 (0%)
  - **Rutas Rotas:** 1 (20%) - *Rota debido a un endpoint incorrecto.*
  - **Rutas en Construcción (Placeholders):** 4 (80%)

## Observaciones Finales y Dependencias

1.  **Desconexión Backend-Frontend:** Existe una desconexión fundamental. El backend tiene una estructura de aplicaciones (`apps/prestadores/mi_negocio`) que no coincide con las referencias en su propio enrutador (`apps.mi_negocio`) ni con las llamadas desde el frontend. La mayoría de las aplicaciones referenciadas (`contabilidad`, `comercial`, etc.) no existen.
2.  **El Módulo `gestion_operativa` es el Único Real:** El único módulo con una implementación funcional real es el de `clientes` dentro de `gestion_operativa`. Sin embargo, la página del frontend que debería consumirlo está rota debido a una URL incorrecta.
3.  **Dependencia Crítica del `AuthContext`:** Todo el panel de "Mi Negocio" depende de una autenticación exitosa para funcionar. Si el `AuthContext` no provee un token válido, ninguna de las llamadas a la API se realizará, dejando las páginas funcionales en un estado de carga perpetua. Esto es una causa muy probable del problema del "círculo de carga" que mencionaste.
4.  **Estado General del Proyecto:** El módulo "Mi Negocio" se encuentra en una fase muy temprana de desarrollo. La infraestructura de enrutamiento está presente pero en su mayoría rota o apuntando a código inexistente. El frontend consiste principalmente en placeholders, con una única página funcional que está mal conectada a su API.
