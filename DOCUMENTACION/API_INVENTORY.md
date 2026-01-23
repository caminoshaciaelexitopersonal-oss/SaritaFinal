# Inventario de APIs - Mi Negocio

Este documento detalla el estado funcional de las APIs para cada módulo del panel "Mi Negocio" del Prestador, a fecha de cierre de la Fase C.

| Módulo | Endpoint Principal | Estado | Notas |
| :--- | :--- | :--- | :--- |
| **Gestión Operativa** | `/api/v1/mi-negocio/operativa/` | `ACTIVO` | API funcional para la gestión de perfil, productos, clientes, etc. Es la base de otros módulos. |
| **Gestión Comercial** | `/api/v1/mi-negocio/comercial/` | `ACTIVO` | API funcional para operaciones comerciales y facturas de venta. |
| **Gestión Financiera**| `/api/v1/mi-negocio/financiera/` | `ACTIVO` | API funcional para la gestión de cuentas y transacciones. |
| **Gestión Archivística**| `/api/v1/mi-negocio/archivistica/`| `ACTIVO` | API funcional para la gestión documental. |
| **Gestión Contable** | `/api/v1/mi-negocio/contable/` | `PARCIAL` | La API se está construyendo de forma fragmentada. Sub-módulos como `activos-fijos` y `compras` están activos, pero no existe una API cohesiva para el módulo completo. Muchas de sus funcionalidades están **INEXISTENTES**. |
| **Proyectos** | N/A | `INEXISTENTE` | El endpoint está explícitamente comentado en el código del backend (`mi_negocio/urls.py`). No hay funcionalidad. |
| **Presupuesto** | N/A | `INEXISTENTE` | El endpoint está explícitamente comentado en el código del backend (`mi_negocio/urls.py`). No hay funcionalidad. |

## Conclusión de Sincronización

- **Frontend Sincronizado:** Durante la Fase A, las páginas del frontend correspondientes a los módulos en estado `PARCIAL` (`gestion-contable`) e `INEXISTENTE` (`proyectos`) fueron reemplazadas por un componente de "En Construcción".
- **Navegación Limpia:** Los enlaces a módulos `INEXISTENTES` fueron eliminados del `Sidebar`.

El estado actual del frontend es **honesto** y refleja con precisión el estado funcional del backend, cumpliendo con el objetivo de la Fase C1.
