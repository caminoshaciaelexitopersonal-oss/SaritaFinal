# Informe Funcional Detallado del Sistema "Sarita"

Fecha de Análisis: 2025-11-09

## 1. Resumen Ejecutivo

Este informe detalla un análisis funcional exhaustivo, archivo por archivo, del backend y frontend del sistema "Sarita". El objetivo es mapear las funcionalidades existentes, identificar los componentes faltantes y evaluar el estado de implementación de cada módulo.

**Hallazgos Clave del Backend:**
*   **Arquitectura Robusta pero Incompleta:** El backend presenta una arquitectura multi-tenant muy sólida en los módulos de "Mi Negocio" (`gestion_comercial`, `gestion_financiera`, etc.). Sin embargo, la aplicación `api` principal está a medio refactorizar, con múltiples dependencias rotas o comentadas hacia el modelo de prestador de servicios.
*   **Módulos de Negocio Implementados:** Módulos como `gestion_comercial`, `gestion_contable` y `gestion_financiera` están implementados a un alto nivel, con lógica de negocio compleja y transacciones atómicas que conectan los tres sistemas.
*   **Funcionalidad Faltante Crítica (Backend):**
    *   **Módulo de Reservas:** El archivo `reservas/models.py` está vacío, lo que causa el `ImportError` que impide la ejecución de todo el sistema.
    *   **Módulo de Verificación:** Los modelos existen, pero las vistas y serializadores están comentados, por lo que la funcionalidad no está expuesta en la API.
    *   **Integración Incompleta:** Numerosos modelos en `api/models.py` tienen sus relaciones con el `ProviderProfile` comentadas.

**Hallazgos Clave del Frontend:**
*   **UI Moderna y Bien Estructurada:** El frontend utiliza una arquitectura moderna con Next.js y hooks de React para gestionar la lógica de la API de forma centralizada.
*   **Funcionalidad Parcialmente Implementada:** La UI para módulos como `gestion_comercial` existe y es funcional, pero con limitaciones.
*   **Funcionalidad Faltante Crítica (Frontend):**
    *   **Módulos Inexistentes:** No hay UI para `Gestión Archivística` ni `Verificación de Cumplimiento`.
    *   **Integración con API Incompleta:** Componentes cruciales, como el formulario de creación de facturas, dependen de datos de prueba (`mock data`) en lugar de conectarse a la API de inventario, lo que los hace inutilizables en la práctica.
    *   **Posible Bug Bloqueante:** Se ha detectado un patrón de construcción de URLs en el hook `useMiNegocioApi.ts` que probablemente duplica el prefijo `/api`, lo que podría estar causando que **todas las llamadas a la API de "Mi Negocio" fallen silenciosamente**. Este es el candidato más probable para el problema del "menú en círculo" reportado.

**Conclusión General:** El sistema tiene una base de código de alta calidad en sus módulos de negocio principales, pero sufre de una refactorización incompleta y una falta de integración entre el frontend y el backend que lo dejan inoperable.

---

## 2. Análisis Funcional del Backend

### 2.1. Aplicación `api`

#### `api/models.py`
*   **Componentes Existentes:**
    *   `CustomUser`: Modelo de usuario central, robusto y funcional.
    *   `Department`, `Municipality`: Modelos de localización, completos.
    *   `Artesano`: Modelo de perfil para artesanos, completo.
    *   `AtractivoTuristico`, `RutaTuristica`, `Publicacion`: Modelos de contenido público.
*   **Componentes Faltantes:**
    *   **Relaciones con Prestador:** Los modelos `ImagenGaleria`, `RutaTuristica`, `Verificacion`, `DocumentoVerificacion` tienen sus relaciones `ForeignKey` al prestador **comentadas**. La integración es inexistente.

#### `api/views.py`
*   **Componentes Existentes:**
    *   Vistas para contenido público (`AtractivoTuristicoViewSet`, etc.).
    *   Vistas de administración (`AdminPrestadorViewSet`, etc.).
    *   Sistema de reseñas y sugerencias.
*   **Componentes Faltantes:**
    *   **API de Verificación:** Las vistas y serializadores para `PlantillaVerificacion` y `Verificacion` están **comentados**. La funcionalidad no está expuesta.
    *   **Lógica de Negocio de "Mi Negocio":** Este archivo no contiene los endpoints para que el prestador gestione su negocio, confirmando la arquitectura modular.

### 2.2. Aplicación `prestadores/mi_negocio`

#### `gestion_operativa/modulos_genericos/perfil/models.py`
*   **Componentes Existentes:**
    *   `ProviderProfile`: **Modelo central del prestador de servicios (Tenant)**. Completo y funcional.
    *   `TenantAwareModel`: Modelo base para la arquitectura multi-tenant. Implementación robusta.

#### `gestion_operativa/modulos_genericos/perfil/views.py`
*   **Componentes Existentes:**
    *   `PerfilViewSet`: **Endpoint completo y seguro** para que un prestador gestione su propio perfil a través de las acciones `me` y `update-me`.

#### `gestion_operativa/modulos_genericos/reservas/models.py`
*   **Componentes Existentes:** Ninguno.
*   **Componentes Faltantes:**
    *   **Archivo Vacío:** Este archivo está completamente vacío.
    *   `CancellationPolicy`: El modelo `CancellationPolicy` es esperado por otros módulos (`productos_servicios`), pero no existe. **Este es el origen del error que bloquea todo el sistema.**

#### `gestion_comercial/models.py`
*   **Componentes Existentes:**
    *   `FacturaVenta`, `ItemFactura`, `ReciboCaja`: Modelos que definen un ciclo de facturación completo y robusto.
    *   **Integración Inter-Módulo:** Los modelos se relacionan correctamente con `Cliente`, `Producto` y `CuentaBancaria`.
*   **Componentes Faltantes:**
    *   **Automatización:** El código prevé, mediante comentarios, la automatización de asientos contables y transacciones financieras al crear un `ReciboCaja`, pero la lógica no está en el modelo.

#### `gestion_comercial/views.py`
*   **Componentes Existentes:**
    *   `FacturaVentaViewSet`: CRUD completo para facturas.
    *   `@action registrar_pago`: **Implementación Excelente.** Esta acción implementa la automatización que faltaba en el modelo. Crea el recibo, la transacción financiera y el asiento contable en una transacción atómica. Es el mejor ejemplo de la calidad de la arquitectura del ERP.

---

## 3. Análisis Funcional del Frontend

### 3.1. Hooks (`.../mi-negocio/hooks/`)

#### `useMiNegocioApi.ts`
*   **Componentes Existentes:**
    *   **Abstracción de API:** Hook centralizado y robusto para todas las llamadas a la API de "Mi Negocio".
    *   **Cobertura Funcional:** Contiene funciones para casi todos los módulos del backend: Perfil, Clientes, Contabilidad, Compras, Inventario, Financiera, Ventas, Activos Fijos, Presupuesto y Nómina.
*   **Componentes Faltantes:**
    *   **API de Gestión Archivística:** No existen funciones para este módulo.
    *   **API de Verificación:** No existen funciones para este módulo.
*   **Defectos Potenciales:**
    *   **Error de URL:** Las URLs se construyen con `/api/v1/...`. Si `axios` ya tiene `/api` como `baseURL`, las llamadas fallarán con un 404. **Este es el principal sospechoso del mal funcionamiento general del frontend.**

### 3.2. Módulo de Gestión Comercial (`.../gestion-comercial/`)

#### `page.tsx` (Lista de Facturas)
*   **Componentes Existentes:**
    *   **Vista de Lista:** Muestra correctamente una tabla con las facturas de venta obtenidas de la API.
    *   **Navegación:** Contiene un botón para navegar a la página de creación de nuevas facturas.
*   **Componentes Faltantes:**
    *   **Acciones de Fila:** La tabla no tiene botones para editar, ver detalle o eliminar facturas.

#### `ventas/nueva/page.tsx` (Nueva Factura)
*   **Componentes Existentes:**
    *   **Formulario de Creación:** UI completa para crear una factura con múltiples ítems.
    *   **Lógica de UI:** Permite añadir/eliminar ítems y recalcula totales.
    *   **Integración con API (Parcial):** Llama a `getClientes` para obtener la lista de clientes y a `createFacturaVenta` para guardar la factura.
*   **Componentes Faltantes:**
    *   **Integración con API de Inventario:** La lista de productos no se obtiene de la API, sino que se usan **datos de prueba (`mockProductos`)**. Esto hace que la funcionalidad sea incompleta y no apta para uso real.
