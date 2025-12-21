# Auditoría del Backend - Análisis de Modelos

## Resumen General de la Estructura de Datos

1.  **Arquitectura Multi-Tenant:** La base de datos está claramente diseñada para ser multi-tenant. El modelo `Perfil` (`apps.prestadores.mi_negocio...perfil.models`) actúa como el ancla principal para casi todos los datos relacionados con un prestador de servicios. Cada modelo de gestión (`Cliente`, `FacturaVenta`, `Producto`, etc.) tiene una `ForeignKey` directa a `Perfil`, asegurando que cada prestador solo pueda ver y gestionar su propia información.
2.  **Sistema de Tres Vías:**
    *   **Gobernanza/Turista (App `api`):** Contiene los modelos públicos como `AtractivoTuristico`, `RutaTuristica`, `Artesano` y modelos de gestión de la plataforma como `CustomUser`, `Entity` y `Publicacion`.
    *   **Prestador de Servicios (App `prestadores` y sus submódulos):** Contiene un completo sistema ERP modular para la gestión del negocio (`Mi Negocio`), abarcando áreas comercial, financiera y contable.
3.  **Modularidad Fuerte:** El código del ERP está altamente organizado en submódulos lógicos (`gestion_comercial`, `gestion_financiera`, `gestion_contable`), y a su vez, `gestion_contable` se divide en sub-submódulos (`compras`, `activos`, `nomina`, etc.). Esto refleja una arquitectura bien estructurada y escalable.
4.  **Funcionalidades Placeholder:** Varios archivos `models.py` están vacíos. Esto indica que la estructura de la aplicación está diseñada para ser expandida con funcionalidades futuras, pero que actualmente no están implementadas a nivel de base de datos (por ejemplo, reservas, gestión de documentos, módulos especializados por tipo de prestador).

## `api` App

*   **Modelos Principales:** `CustomUser`, `Profile`, `Artesano`, `AtractivoTuristico`, `RutaTuristica`, `Publicacion`.
*   **Relaciones Clave:**
    *   `CustomUser` es el modelo central de usuario, con `OneToOne` a `Profile` y `Artesano`.
    *   `RutaTuristica` agrupa `AtractivoTuristico`s.
*   **Observaciones:** Contiene los modelos base para el sistema de turismo (vías de turista y gobernanza) y modelos de soporte como formularios dinámicos, sistema de puntuación, notificaciones y verificación de documentos.

## `apps/prestadores/mi_negocio` App (Módulos ERP)

### Módulo `gestion_operativa` (Genéricos)

*   `perfil.models.py`:
    *   **Modelos:** `CategoriaPrestador`, `Perfil`.
    *   **Observaciones:** `Perfil` es el **modelo central y más importante** para el prestador de servicios.
*   `productos_servicios.models.py`:
    *   **Modelos:** `ProductoServicio`.
    *   **Relaciones:** `ForeignKey` a `Perfil`.
*   `clientes.models.py`:
    *   **Modelos:** `Cliente`.
    *   **Relaciones:** `ForeignKey` a `Perfil`.
*   `costos.models.py`:
    *   **Modelos:** `Costo`.
    *   **Relaciones:** `ForeignKey` a `Perfil`.
*   `inventario.models.py`:
    *   **Modelos:** `Inventario`.
    *   **Relaciones:** `ForeignKey` a `Perfil`.
*   **Archivos Vacíos:** `reservas`, `documentos`, `valoraciones`, `estadisticas`, `galeria`.

### Módulo `gestion_operativa` (Especializados)

*   **Archivos Vacíos:** `restaurantes`, `transporte`, `guias`, `agencias`, `hoteles`.

### Módulo `gestion_comercial`

*   `models.py`:
    *   **Modelos:** `FacturaVenta`, `ItemFactura`, `ReciboCaja`.
    *   **Relaciones:** `ForeignKey` a `Perfil`, `Cliente`, `Producto`, `CuentaBancaria`.

### Módulo `gestion_financiera`

*   `models.py`:
    *   **Modelos:** `CuentaBancaria`, `TransaccionBancaria`.
    *   **Relaciones:** `ForeignKey` a `Perfil`.

### Módulo `gestion_contable`

*   `compras/models.py`:
    *   **Modelos:** `Proveedor`, `FacturaCompra`.
    *   **Relaciones:** `ForeignKey` a `Perfil`.
*   `activos/models.py`:
    *   **Modelos:** `CategoriaActivo`, `ActivoFijo`, `Depreciacion`.
    *   **Relaciones:** `ForeignKey` a `Perfil`.
*   `contabilidad/models.py`:
    *   **Modelos:** `CostCenter`, `Currency`, `ExchangeRate`, `ChartOfAccount`, `JournalEntry`, `Transaction`.
    *   **Relaciones:** `ForeignKey` a `Perfil`.
*   `inventario/models.py`:
    *   **Modelos:** `CategoriaProducto`, `Almacen`, `Producto`, `MovimientoInventario`.
    *   **Relaciones:** `ForeignKey` a `Perfil`.
*   `nomina/models.py`:
    *   **Modelos:** `Empleado`, `Contrato`, `ConceptoNomina`, `Planilla`, `NovedadNomina`.
    *   **Relaciones:** `ForeignKey` a `Perfil`.
*   `proyectos/models.py`:
    *   **Modelos:** `Proyecto`, `IngresoProyecto`, `CostoProyecto`.
    *   **Relaciones:** `ForeignKey` a `Perfil`, `FacturaVenta`, `FacturaCompra`.
*   **Archivos Vacíos:** `empresa`.

## Análisis de Endpoints y Serializers

1.  **Arquitectura RESTful:** La API sigue los principios RESTful, utilizando `viewsets` y `routers` para proporcionar endpoints CRUD estándar para la mayoría de los recursos.
2.  **Estructura de Rutas Jerárquica:** Las rutas están organizadas de forma lógica y jerárquica, con un punto de entrada principal en `/api/`. La autenticación se encuentra en `/api/auth/`, la API principal en `/api/`, y el panel "Mi Negocio" en `/api/v1/mi-negocio/`.
3.  **Modularidad:** Las rutas del panel "Mi Negocio" están modularizadas por función (comercial, financiera, contable), lo que refleja la estructura de la aplicación.
4.  **Serializers Ricos en Lógica:** Los serializers no solo definen la representación de los datos, sino que también contienen una lógica de validación y creación significativa, incluyendo la creación anidada de objetos relacionados y la asignación automática de datos (como el perfil del usuario).
5.  **Separación de Lectura/Escritura:** El uso de serializers separados para las operaciones de lectura y escritura permite un control más granular sobre la API.
6.  **Integración entre Módulos:** Los serializers demuestran la integración entre los diferentes módulos de la aplicación, reutilizando componentes como el `ClienteSerializer` en el `FacturaVentaSerializer`.

## 🧩 Endpoints y Serializers
| Endpoint | View/ViewSet | Métodos | Modelo | Serializer | Permisos | Frontend (archivo o ruta) |
| --- | --- | --- | --- | --- | --- | --- |
| /api/v1/mi-negocio/comercial/facturas-venta/ | FacturaVentaViewSet | GET, POST, PUT, PATCH, DELETE | FacturaVenta | FacturaVentaSerializer | IsPrestadorOwner | gestion-comercial/ventas.tsx |
| /api/v1/mi-negocio/comercial/recibos-caja/ | ReciboCajaViewSet | GET, POST, PUT, PATCH, DELETE | ReciboCaja | ReciboCajaSerializer | IsPrestadorOwner | gestion-comercial/ventas.tsx |
| /api/v1/mi-negocio/financiera/cuentas-bancarias/ | CuentaBancariaViewSet | GET, POST, PUT, PATCH, DELETE | CuentaBancaria | CuentaBancariaSerializer | IsPrestadorOwner | gestion-financiera/cuentas.tsx |
| /api/v1/mi-negocio/financiera/transacciones/ | TransaccionBancariaViewSet | GET, POST, PUT, PATCH, DELETE | TransaccionBancaria | TransaccionBancariaSerializer | IsPrestadorOwner | gestion-financiera/cuentas.tsx |
| /api/v1/mi-negocio/financiera/reporte-ingresos-gastos/ | ReporteIngresosGastosView | GET | N/A | N/A | IsAuthenticated | gestion-financiera/reportes.tsx |
| /api/v1/mi-negocio/contable/activos/categorias/ | CategoriaActivoViewSet | GET, POST, PUT, PATCH, DELETE | CategoriaActivo | CategoriaActivoSerializer | IsPrestadorOwner | gestion-contable/activos.tsx |
| /api/v1/mi-negocio/contable/activos/activos-fijos/ | ActivoFijoViewSet | GET, POST, PUT, PATCH, DELETE | ActivoFijo | ActivoFijoSerializer | IsPrestadorOwner | gestion-contable/activos.tsx |
| /api/v1/mi-negocio/contable/activos/depreciaciones/ | DepreciacionViewSet | GET, POST, PUT, PATCH, DELETE | Depreciacion | DepreciacionSerializer | IsPrestadorOwner | gestion-contable/activos.tsx |
| /api/v1/mi-negocio/contable/compras/proveedores/ | ProveedorViewSet | GET, POST, PUT, PATCH, DELETE | Proveedor | ProveedorSerializer | IsPrestadorOwner | gestion-contable/compras.tsx |
| /api/v1/mi-negocio/contable/compras/facturas/ | FacturaCompraViewSet | GET, POST, PUT, PATCH, DELETE | FacturaCompra | FacturaCompraSerializer | IsPrestadorOwner | gestion-contable/compras.tsx |
| /api/v1/mi-negocio/contable/compras/generar-pago-masivo/ | GenerarPagoMasivoProveedoresView | POST | N/A | N/A | IsAuthenticated | gestion-contable/compras.tsx |
| /api/v1/mi-negocio/contable/contabilidad/cost-centers/ | CostCenterViewSet | GET, POST, PUT, PATCH, DELETE | CostCenter | CostCenterSerializer | IsPrestadorOwner | gestion-contable/contabilidad.tsx |
| /api/v1/mi-negocio/contable/contabilidad/chart-of-accounts/ | ChartOfAccountViewSet | GET | ChartOfAccount | ChartOfAccountSerializer | IsAuthenticated | gestion-contable/contabilidad.tsx |
| /api/v1/mi-negocio/contable/contabilidad/journal-entries/ | JournalEntryViewSet | GET, POST, PUT, PATCH, DELETE | JournalEntry | JournalEntrySerializer | IsPrestadorOwner | gestion-contable/contabilidad.tsx |
| /api/v1/mi-negocio/contable/inventario/categorias/ | CategoriaProductoViewSet | GET, POST, PUT, PATCH, DELETE | CategoriaProducto | CategoriaProductoSerializer | IsPrestadorOwner | gestion-contable/inventario.tsx |
| /api/v1/mi-negocio/contable/inventario/almacenes/ | AlmacenViewSet | GET, POST, PUT, PATCH, DELETE | Almacen | AlmacenSerializer | IsPrestadorOwner | gestion-contable/inventario.tsx |
| /api/v1/mi-negocio/contable/inventario/productos/ | ProductoViewSet | GET, POST, PUT, PATCH, DELETE | Producto | ProductoSerializer | IsPrestadorOwner | gestion-contable/inventario.tsx |
| /api/v1/mi-negocio/contable/inventario/movimientos/ | MovimientoInventarioViewSet | GET, POST, PUT, PATCH, DELETE | MovimientoInventario | MovimientoInventarioSerializer | IsPrestadorOwner | gestion-contable/inventario.tsx |
| /api/v1/mi-negocio/contable/nomina/empleados/ | EmpleadoViewSet | GET, POST, PUT, PATCH, DELETE | Empleado | EmpleadoSerializer | IsPrestadorOwner | gestion-contable/nomina.tsx |
| /api/v1/mi-negocio/contable/nomina/contratos/ | ContratoViewSet | GET, POST, PUT, PATCH, DELETE | Contrato | ContratoSerializer | IsPrestadorOwner | gestion-contable/nomina.tsx |
| /api/v1/mi-negocio/contable/nomina/planillas/ | PlanillaViewSet | GET, POST, PUT, PATCH, DELETE | Planilla | PlanillaSerializer | IsPrestadorOwner | gestion-contable/nomina.tsx |
| /api/v1/mi-negocio/contable/nomina/conceptos/ | ConceptoNominaViewSet | GET | ConceptoNomina | ConceptoNominaSerializer | IsAuthenticated | gestion-contable/nomina.tsx |
| /api/v1/mi-negocio/contable/proyectos/proyectos/ | ProyectoViewSet | GET, POST, PUT, PATCH, DELETE | Proyecto | ProyectoSerializer | IsPrestadorOwner | gestion-contable/proyectos.tsx |
| /api/v1/mi-negocio/contable/proyectos/ingresos/ | IngresoProyectoViewSet | GET, POST, PUT, PATCH, DELETE | IngresoProyecto | IngresoProyectoSerializer | IsPrestadorOwner | gestion-contable/proyectos.tsx |
| /api/v1/mi-negocio/contable/proyectos/costos/ | CostoProyectoViewSet | GET, POST, PUT, PATCH, DELETE | CostoProyecto | CostoProyectoSerializer | IsPrestadorOwner | gestion-contable/proyectos.tsx |
| /api/v1/mi-negocio/operativa/clientes/ | ClienteViewSet | GET, POST, PUT, PATCH, DELETE | Cliente | ClienteSerializer | IsPrestadorOwner | gestion-operativa/clientes.tsx |
| /api/v1/mi-negocio/operativa/productos-servicios/ | ProductoServicioViewSet | GET, POST, PUT, PATCH, DELETE | ProductoServicio | ProductoServicioSerializer | IsPrestadorOwner | gestion-operativa/productos.tsx |
| /api/v1/mi-negocio/operativa/inventario/ | InventarioViewSet | GET, POST, PUT, PATCH, DELETE | Inventario | InventarioSerializer | IsPrestadorOwner | gestion-operativa/inventario.tsx |
| /api/v1/mi-negocio/operativa/costos/ | CostoViewSet | GET, POST, PUT, PATCH, DELETE | Costo | CostoSerializer | IsPrestadorOwner | gestion-operativa/costos.tsx |
| /api/v1/mi-negocio/operativa/perfil/me/ | PerfilViewSet | GET | Perfil | PerfilSerializer | IsAuthenticated | gestion-operativa/perfil.tsx |
| /api/v1/mi-negocio/operativa/perfil/update-me/ | PerfilViewSet | PUT, PATCH | Perfil | PerfilSerializer | IsAuthenticated | gestion-operativa/perfil.tsx |

## Inconsistencias entre Backend y Frontend
*   El hook `useMiNegocioApi` intenta acceder a `/api/v1/mi-negocio/financiera/bank-accounts/`, pero el endpoint real es `/api/v1/mi-negocio/financiera/cuentas-bancarias/`.
*   El hook `useMiNegocioApi` intenta acceder a `/api/v1/mi-negocio/financiera/cash-transactions/`, pero el endpoint real es `/api/v1/mi-negocio/financiera/transacciones/`.
*   El hook `useMiNegocioApi` intenta acceder a los endpoints raíz de `/api/v1/mi-negocio/contable/nomina/` y `/api/v1/mi-negocio/contable/proyectos/`, pero estos no existen. El backend solo expone endpoints más específicos.
*   El hook `useMiNegocioApi` no tiene funciones para interactuar con los módulos de `activos`, `inventario` y `costos`.

## Resumen Cuantitativo

*   **Endpoints documentados:** 32
*   **Serializers únicos:** 45 (aproximadamente)
*   **Endpoints con permisos de acceso definidos:** 32
*   **Endpoints actualmente consumidos en el frontend:** 13
