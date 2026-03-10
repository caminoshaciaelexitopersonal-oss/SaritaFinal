# COMPONENT INVENTORY: SARITA MULTIPLATFORM

## 1. Interfaz Web (Next.js 15)
### Módulos Principales
- **panel-admin:** Localizado en `interfaz/src/app/dashboard/admin`. Incluye `ia-audit` e `integrity`.
- **tablero-prestador:** Localizado en `interfaz/src/app/dashboard/prestador/mi-negocio`.
- **descubre-turismo:** Localizado en `interfaz/src/app/descubre`. Incluye `atractivos`, `agenda-cultural`, `mapa`, `rutas-turisticas`.

### Componentes UI
- `AdminDashboard.tsx`, `UserManager.tsx`, `StatisticsDashboard.tsx`.
- `FormBuilder.tsx`, `FormFiller.tsx`, `DocumentManager.tsx`.
- `MapComponent.tsx`, `ImageGalleryManager.tsx`.

## 2. Interfaz Móvil (React Native / Expo)
### Módulos Principales
- **panel-admin:** Localizado en `apps/mobile/src/screens/admin`. Incluye `analytics` y `alerts`.
- **tablero-prestador:** Localizado en `apps/mobile/src/screens/business`. Incluye `BusinessAccounting`, `BusinessFinance`, `BusinessOrders`.
- **descubre-turismo:** Localizado en `apps/mobile/src/screens/explore`. Incluye `ExploreScreen`.

### Pantallas Clave
- `AdminDashboard.tsx`, `GlobalControlCenterScreen.tsx`.
- `BusinessDashboard.tsx`, `RegionalAnalyticsScreen.tsx`.
- `ExploreScreen.tsx`, `SmartMapScreen.tsx`.

## 3. Interfaz Escritorio (Electron)
### Módulos Principales
- **panel-admin:** Localizado en `apps/desktop/renderer/src/admin`.
- **tablero-prestador:** Localizado en `apps/desktop/renderer/src/dashboard`. Incluye `accounting`, `archive`, `commercial`, `finance`, `operations`.
- **descubre-turismo:** Localizado en `apps/desktop/renderer/src/pages/descubre`.

### Componentes Clave
- `AdminDashboard.tsx`.
- `MiNegocio.tsx`, `POSInterface.tsx`, `AccountingDashboard.tsx`.
- `DiscoveryDashboard.tsx`.

---
*Consolidado por Jules - Marzo 2026*
