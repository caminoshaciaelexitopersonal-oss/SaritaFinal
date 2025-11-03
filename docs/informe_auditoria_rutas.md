# Auditoría Técnica de Rutas: Sistema Sarita

Este informe detalla el estado de las rutas del backend (API Django) y del frontend (Next.js), centrándose en su funcionalidad y configuración actual.

## 1. Backend (Django)

Análisis de las rutas registradas en `backend/apps/prestadores/mi_negocio` y sus correspondientes `urls.py`. El estado "Configurada" indica que la ruta está correctamente declarada en el código fuente. La funcionalidad real depende de la correcta implementación de las vistas y modelos asociados.

**Prefijo base para todas las rutas:** `/api/v1/mi-negocio/`

### Rutas de "Mi Negocio"

| Módulo | Ruta | Estado | Código HTTP | Descripción / Observación |
| :--- | :--- | :--- | :--- | :--- |
| **Operativa** | `operativa/clientes/` | Configurada | - | Endpoints CRUD para Clientes. |
| **Operativa** | `operativa/productos-servicios/` | Configurada | - | Endpoints CRUD para Productos/Servicios. |
| **Operativa** | `operativa/inventario/` | Configurada | - | Endpoints CRUD para Inventario. |
| **Operativa** | `operativa/costos/` | Configurada | - | Endpoints CRUD para Costos. |
| **Operativa** | `operativa/perfil/me/` | Configurada | GET | Obtiene el perfil del usuario autenticado. |
| **Operativa** | `operativa/perfil/update-me/` | Configurada | PUT, PATCH | Actualiza el perfil del usuario autenticado. |
| **Comercial** | `comercial/facturas-venta/` | Configurada | - | Endpoints CRUD para Facturas de Venta. |
| **Comercial** | `comercial/recibos-caja/` | Configurada | - | Endpoints CRUD para Recibos de Caja. |
| **Financiera**| `financiera/cuentas-bancarias/` | Configurada | - | Endpoints CRUD para Cuentas Bancarias. |
| **Financiera**| `financiera/transacciones/` | Configurada | - | Endpoints CRUD para Transacciones Bancarias. |
| **Financiera**| `financiera/reporte-ingresos-gastos/`| Configurada | GET | Vista para generar un reporte de ingresos y gastos. |
| **Contable** | `contable/activos/categorias/` | Configurada | - | Endpoints CRUD para Categorías de Activos. |
| **Contable** | `contable/activos/activos-fijos/` | Configurada | - | Endpoints CRUD para Activos Fijos. |
| **Contable** | `contable/activos/depreciaciones/` | Configurada | - | Endpoints CRUD para Depreciaciones. |
| **Contable** | `contable/compras/proveedores/` | Configurada | - | Endpoints CRUD para Proveedores. |
| **Contable** | `contable/compras/facturas/` | Configurada | - | Endpoints CRUD para Facturas de Compra. |
| **Contable** | `contable/compras/generar-pago-masivo/`| Configurada | POST | Vista para generar pagos masivos a proveedores. |
| **Contable** | `contable/contabilidad/cost-centers/` | Configurada | - | Endpoints CRUD para Centros de Costo. |
| **Contable** | `contable/contabilidad/chart-of-accounts/`| Configurada | - | Endpoints CRUD para Plan de Cuentas. |
| **Contable** | `contable/contabilidad/journal-entries/` | Configurada | - | Endpoints CRUD para Asientos Diarios. |
| **Contable** | `contable/inventario/categorias/` | Configurada | - | Endpoints CRUD para Categorías de Producto (Inventario). |
| **Contable** | `contable/inventario/almacenes/` | Configurada | - | Endpoints CRUD para Almacenes. |
| **Contable** | `contable/inventario/productos/` | Configurada | - | Endpoints CRUD para Productos (Inventario). |
| **Contable** | `contable/inventario/movimientos/` | Configurada | - | Endpoints CRUD para Movimientos de Inventario. |
| **Contable** | `contable/nomina/empleados/` | Configurada | - | Endpoints CRUD para Empleados. |
| **Contable** | `contable/nomina/contratos/` | Configurada | - | Endpoints CRUD para Contratos. |
| **Contable** | `contable/nomina/planillas/` | Configurada | - | Endpoints CRUD para Planillas de Nómina. |
| **Contable** | `contable/nomina/conceptos/` | Configurada | - | Endpoints CRUD para Conceptos de Nómina. |
| **Contable** | `contable/proyectos/proyectos/` | Configurada | - | Endpoints CRUD para Proyectos. |
| **Contable** | `contable/proyectos/ingresos/` | Configurada | - | Endpoints CRUD para Ingresos de Proyecto. |
| **Contable** | `contable/proyectos/costos/` | Configurada | - | Endpoints CRUD para Costos de Proyecto. |
| **Archivística**| `archivistica/` | Placeholder | GET | Vista de marcador de posición, no funcional. |

## 2. Frontend (Next.js)

Análisis de las rutas de página dentro de `frontend/src/app/dashboard/prestador/mi-negocio`.

**Resultado del Build:** El comando `npx next build` falló con un error fatal de Turbopack (`Invariant: Expected to inject all injections, found // INJECT:pages`). Esto significa que el proyecto de frontend no puede ser compilado y, por lo tanto, **ninguna página es funcional en el estado actual.**

### Páginas de "Mi Negocio"

| Ruta | Estado | Componente principal | Observaciones |
| :--- | :--- | :--- | :--- |
| `/gestion-archivistica` | Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-comercial` | Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-comercial/ventas` | Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-comercial/ventas/nueva` | Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-contable` | Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-contable/activos` | Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-contable/asientos` | Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-contable/compras` | Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-contable/contabilidad`| Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-contable/cuentas-bancarias`| Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-contable/informes/...`| Rota (Build Fallido) | `page.tsx` | 5 páginas de informes, no se pueden compilar. |
| `/gestion-contable/inventario` | Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-contable/plan-de-cuentas`| Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-contable/tesoreria` | Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-contable/transacciones`| Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-financiera` | Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-financiera/financiera` | Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-operativa/especializados/...`| Rota (Build Fallido) | `page.tsx` | 5 páginas especializadas, no se pueden compilar. |
| `/gestion-operativa/genericos` | Rota (Build Fallido) | `page.tsx` | Página de bienvenida estática, pero no se puede compilar. |
| `/gestion-operativa/genericos/certificaciones`| Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-operativa/genericos/clientes`| Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-operativa/genericos/clientes/editar/[id]`| Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-operativa/genericos/clientes/nuevo`| Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-operativa/genericos/costos`| Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-operativa/genericos/crm` | Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-operativa/genericos/documentos`| Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-operativa/genericos/estadisticas`| Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-operativa/genericos/galeria`| Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-operativa/genericos/inventario`| Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-operativa/genericos/perfil`| Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-operativa/genericos/productos-servicios`| Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-operativa/genericos/reservas`| Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-operativa/genericos/valoraciones`| Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-operativa/nomina` | Rota (Build Fallido) | `page.tsx` | No se puede compilar. |
| `/gestion-operativa/proyectos` | Rota (Build Fallido) | `page.tsx` | No se puede compilar. |

## 3. Resumen Global

| Métrica | Total |
| :--- | :--- |
| **Rutas de Backend Auditadas** | 33 |
| Rutas de Backend Configradas (Estático) | 33 |
| **Rutas de Frontend Auditadas** | 44 |
| Rutas de Frontend Funcionales | 0 |
| Rutas de Frontend Rotas | 44 (Build Fallido) |

## 4. Observaciones Finales

- **Bloqueador Crítico (Frontend):** El proyecto de frontend es **inoperable** debido a un error fatal en el proceso de build de Next.js (Turbopack). Este es el problema de mayor prioridad a resolver, ya que impide cualquier tipo de verificación visual o funcional de la interfaz de usuario.
- **Backend Robusto (Estructuralmente):** El backend presenta una estructura de API muy completa y bien organizada para "Mi Negocio". Todas las rutas para los módulos principales están definidas, lo que sugiere que la lógica de negocio subyacente puede estar en un estado avanzado de desarrollo.
- **Dependencia API:** El análisis de los componentes del frontend (como `ClientesPage`) revela una fuerte dependencia del hook `useMiNegocioApi`, lo que indica que el frontend está diseñado para ser un consumidor puro de la API REST del backend.
