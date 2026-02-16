# INFORME DE INVESTIGACIÓN: LOCALIZACIÓN Y ESTADO DEL PERFIL ARTESANOS

## 1. INVESTIGACIÓN A NIVEL DE DOMINIO

### A) Identidad Global (IAM)
- **Rol:** Existe el rol `ARTESANO` en la clase `CustomUser.Role` (app `api`).
- **Naturaleza:** Es un rol de primer nivel, paralelo a `PRESTADOR` y `TURISTA`.

### B) Dominio Gubernamental
- **Ubicación:** App `api`, modelos `Artesano` y `RubroArtesano`.
- **Atributos Regulatorios:** El perfil tiene un campo `aprobado` (booleano), lo que indica que es una entidad validada por la autoridad (Vía 1).
- **Vínculo:** Posee una relación con `Entity`, vinculándolo directamente a una Corporación o Secretaría.

### C) Dominio Comercial
- **Ubicación:** El modelo `ProviderProfile` (app `prestadores`) incluye `ARTISAN` como un `ProviderType`.
- **Tratamiento:** Se le reconoce como un prestador de servicios empresariales (Vía 2), permitiéndole acceder a los módulos de "Mi Negocio".

## 2. INVESTIGACIÓN A NIVEL DE BASE DE DATOS

- **Tablas Propias:**
  - `api_artesano`: Almacena el perfil informativo y de caracterización.
  - `api_rubroartesano`: Clasificación por oficio.
  - `api_imagenartesano`: Galería de productos/taller.
- **Redundancia Detectada:** Existe una coexistencia entre el modelo `Artesano` (en `api`) y el `ProviderProfile` (en `prestadores`). Actualmente no hay registros, por lo que el sistema es un "cascarón" listo para ser habitado.

## 3. INVESTIGACIÓN A NIVEL FUNCIONAL

- **Creación de Productos:** No existe una tabla especializada de `ArtisanProduct`. Depende del catálogo genérico de `prestadores`.
- **Pagos y Monedero:** Reconocido como entidad económica, pero sin lógica de "Taller" (pedidos de artesanías a medida).
- **Estado Actual:** **ESCENARIO B (Perfil + Catálogo Simple)**. Es más que un perfil informativo pero menos que un vendedor completo digitalizado.

## 4. INVESTIGACIÓN A NIVEL DE PERMISOS (RBAC)

- **Frontend:** El `Sidebar.tsx` detecta el rol `ARTESANO` y renombra la sección de "Mi Negocio" a "**Mi Taller**".
- **Dashboard:** Tiene acceso a los 5 módulos genéricos (Comercial, Contable, Financiero, Operativo, Archivístico).

## 5. MATRIZ DE DIAGNÓSTICO

| Escenario | Situación | Clasificación Actual |
| :--- | :--- | :---: |
| A | Solo perfil informativo | |
| B | Perfil + catálogo simple | **X (ACTUAL)** |
| C | Vendedor completo | |
| D | Entidad empresarial formal | |

## 6. MAPA DE DEPENDENCIAS DE AGENTES

- **Coronel:** `PrestadoresCoronel`.
- **Capitán:** `CapitanOperacionArtesanos`.
- **Sargento:** `SargentoGestionTallerArtesano`.
- **Soldados:** Existen 5 soldados especializados (`RegistroInventario`, `ValidacionPedido`, `ControlStock`, `ConfirmacionDespacho`, `MonitoreoVentas`).
- **Hallazgo:** La infraestructura de agentes es **superior** a la infraestructura de modelos actual. Los agentes están diseñados para una operatividad (Escenario C) que la base de datos aún no soporta totalmente.

## 7. RIESGO ESTRATÉGICO

El principal riesgo es la **fragmentación de identidad**. Si se crean registros en `api_artesano` sin un espejo en `prestadores_providerprofile`, el artesano tendrá un perfil público pero no podrá gestionar su contabilidad ni ventas.

## 8. RECOMENDACIÓN DE INTEGRACIÓN

1. **Unificación de Modelos:** Crear una señal (signal) que al aprobar un `Artesano` en el dominio Gov, genere automáticamente su `ProviderProfile` comercial.
2. **Construcción del Módulo Especializado:** Crear `backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_especializados/artesanos/` para manejar el inventario de materias primas y órdenes de taller.
3. **Persistencia de Agentes:** Conectar los Soldados existentes a los nuevos modelos de inventario artesanal.
