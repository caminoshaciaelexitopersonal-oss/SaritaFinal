# COMPONENT INVENTORY: SARITA ECHOSYSTEM

## 1. Web Platform (Next.js 15)
### Screens & Layouts
- **Dashboard Admin:** `/app/dashboard/admin`
- **Dashboard Prestador:** `/app/dashboard/prestador`
- **Descubre Turismo:** `/app/descubre`
- **Auth:** `/app/dashboard/login`, `/app/dashboard/registro`
- **Sub-módulos:** `atractivos`, `delivery`, `formularios`, `verificacion`, `agenda-cultural`, `mapa`, `rutas-turisticas`.

### Components
- **Core UI:** `Button`, `Card`, `Input`, `Modal`, `Sidebar`, `Header`, `NotificationBell`.
- **Business/ERP:** `ArtesanoProfileForm`, `AtractivoForm`, `FormBuilder`, `DocumentManager`, `ResenasManager`.
- **Specialized:** `MapComponent`, `ImageGalleryManager`, `LLMKeysManager`, `AuditLogViewer`.

## 2. Mobile Platform (Expo / React Native)
### Screens (MainNavigator)
- **Tourist:** `ExploreScreen`, `BookingsScreen`, `WalletHomeScreen`, `DeliveryHomeScreen`, `PassportScreen`, `VirtualGuideScreen`.
- **Prestador:** `BusinessDashboard`, `BusinessServicesScreen`, `BusinessOrdersScreen`, `BusinessAccountingScreen`, `BusinessFinanceScreen`.
- **Admin:** `AdminDashboard`, `GlobalControlCenterScreen`, `SystemObservabilityScreen`, `CountryDashboard`.

### Components
- **UI:** `Button`, `Card`, `Input`, `Loader`, `TourCard`.
- **Specialized:** Native Map integrations, QR Scanner (Passport), Push Notifications.

## 3. Desktop Platform (Electron)
### Screens (React-Router)
- **Main:** `HomePage`, `LoginPage`.
- **Mi Negocio:** `BusinessManager`, `CustomersManager`, `SalesManager`, `ArchiveDashboard`, `AccountingDashboard`, `FinanceDashboard`.
- **Admin:** `AdminDashboard` (Torre de Control).
- **Domain:** `WalletDashboard`, `DeliveryManager`.

### Components
- **UI:** `Button`, `Card`, `Navbar`, `Sidebar`.
- **Hardware Integration:** Local database (SQLite), POS printers integration (via main process).

## 4. Shared SDK (Logic & Service Parity)
- **Auth Service:** Universal token management (JWT).
- **API Client:** Shared Axios instances with interceptors.
- **AI Engine:** Client-side LLM routing logic.
- **Models:** Common TypeScript interfaces for ERP and Tourism entities.

---
*Inventory consolidated on March 2026.*
