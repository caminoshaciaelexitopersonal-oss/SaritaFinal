# COMPONENT INVENTORY: SARITA v1.0
**Lead Auditor:** Jules (Senior AI Software Engineer)
**Fecha:** Marzo de 2026

## 1. Web (Next.js 15)
- **Tourist (Descubre):** `atractivos`, `agenda-cultural`, `galeria`, `historia`, `rutas-turisticas`, `como-llegar`, `mapa`.
- **Prestador (Mi Negocio):** `gestion-contable`, `gestion-financiera`, `tesoreria`, `nomina`, `activos`, `presupuesto`, `cuentas-bancarias`.
- **Government (Admin):** `ia-audit`, `integrity`, `admin-plataforma` (30+ sub-módulos de gobernanza, autonomía, GRC, nodos, etc.).

## 2. Mobile (Expo)
- **Tourist:** `ExploreScreen`, `SearchBar`, `ARDiscoveryScreen`, `TourScreen`, `MapScreen`.
- **Prestador:** `BusinessDashboard`, `BusinessAccountingScreen`, `BusinessFinanceScreen`, `BusinessOrdersScreen`, `BusinessServicesScreen`, `BusinessReportsScreen`.
- **Government:** `AdminDashboard`, `RegionalAnalyticsScreen`, `SystemObservabilityScreen`, `MonitoringScreen`.

## 3. Desktop (Electron)
- **Tourist:** `DiscoveryDashboard`.
- **Prestador:** `TableroPrestador` (Consolidado).
- **Government:** `PanelAdmin`.
- **Common:** `Login`, `Home`.

---
**Nota:** Los componentes de Mobile y Desktop derivan lógica del `Shared SDK`.
