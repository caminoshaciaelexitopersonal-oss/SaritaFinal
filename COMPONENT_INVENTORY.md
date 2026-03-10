# COMPONENT INVENTORY: SARITA v1.0
**Lead Auditor:** Jules (Senior AI Software Engineer)
**Fecha:** Marzo de 2026

## 1. Interfaz Web (Next.js 15)
### 1.1 Panel Gobierno (Admin)
- `AdminDashboard.tsx`, `StatisticsDashboard.tsx`, `AuditLogViewer.tsx`, `UserManager.tsx`.
- Módulos de Gobernanza: `ia-audit`, `integrity`, `admin-plataforma/inteligencia`, `admin-plataforma/autonomia`, `admin-plataforma/grc`.
- Gestión de Contenido: `HomePageManager.tsx`, `MenuManager.tsx`, `MunicipioContentManager.tsx`, `PaginaInstitucionalManager.tsx`.

### 1.2 Tablero Prestador (Mi Negocio)
- `PrestadorDashboard.tsx`, `PanelFacturacion.tsx`, `TablaReservas.tsx`, `FormularioServicio.tsx`.
- Gestión Contable: `contabilidadService.ts`, `nomina`, `activos`, `presupuesto`.
- Verificación: `VerificacionManager.tsx`, `HistorialVerificaciones.tsx`, `FormularioVerificacion.tsx`.

### 1.3 Descubre Turismo
- `AtractivosManager.tsx`, `RutasManager.tsx`, `MapComponent.tsx`, `ResenasSection.tsx`.
- Perfil: `ProfileForm.tsx`, `ArtesanoProfileForm.tsx`.
- Utilidades: `Search`, `Filters`, `Gallery`.

## 2. Interfaz Mobile (Expo)
### 2.1 Panel Gobierno
- `AdminDashboard.tsx`, `RegionalAnalyticsScreen.tsx`, `SystemObservabilityScreen.tsx`, `MonitoringScreen.tsx`.

### 2.2 Tablero Prestador (Mi Negocio)
- `BusinessDashboard.tsx`, `BusinessAccountingScreen.tsx`, `BusinessFinanceScreen.tsx`, `BusinessOrdersScreen.tsx`, `BusinessServicesScreen.tsx`, `BusinessReportsScreen.tsx`, `OperatorDashboard.tsx`, `ReputationScreen.tsx`.

### 2.3 Descubre Turismo
- `ExploreScreen.tsx`, `SearchBar.tsx`, `ARDiscoveryScreen.tsx`, `TourScreen.tsx`, `MapScreen.tsx`, `TravelFeedScreen.tsx`, `DestinationScreen.tsx`.
- Gestión: `BookingScreen.tsx`, `TicketScreen.tsx`, `WalletHomeScreen.tsx`.

## 3. Interfaz Desktop (Electron)
### 3.1 Panel Gobierno
- `PanelAdmin.tsx`.

### 3.2 Tablero Prestador (Mi Negocio)
- `TableroPrestador.tsx`, `CommercialDashboard`, `OperationsDashboard`, `FinanceDashboard`, `AccountingDashboard`.
- **Exclusivo:** Módulo POS (Point of Sale) para facturación física.

### 3.3 Descubre Turismo
- `DiscoveryDashboard.tsx`.

---
**Nota:** La estandarización se logra mediante el `Shared SDK` localizado en `sarita-platform/shared-sdk`, el cual provee hooks y servicios de API unificados para las tres plataformas.
