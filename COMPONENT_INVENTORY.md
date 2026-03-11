# COMPONENT INVENTORY: SARITA PLATFORM v1.0
**Lead Auditor:** Jules (Senior AI Software Engineer)
**Date:** March 2026

## 1. Web Components (Next.js 15)
Ubicación: `interfaz/src/components`

- **Dashboard Admin:** `AdminDashboard.tsx`, `AdminProviderManager.tsx`, `ArtesanosManager.tsx`, `AtractivosManager.tsx`, `AuditLogViewer.tsx`, `CapacitacionesManager.tsx`, `FormManager.tsx`, `LLMKeysManager.tsx`, `SiteConfigManager.tsx`, `UserManager.tsx`
- **Dashboard Prestador (Mi Negocio):** `FeedbackManager.tsx`, `FeedbackProveedor.tsx`, `FormularioVerificacion.tsx`, `HistorialVerificaciones.tsx`, `PrestadorManager.tsx`, `DocumentManager.tsx`
- **Descubre Turismo:** `AtractivoForm.tsx`, `CapacitacionDetail.tsx`, `ConsejoConsultivoDashboard.tsx`, `HistoriaManager.tsx`, `ImageGalleryManager.tsx`, `ImageSlider.tsx`, `MapComponent.tsx`, `ResenasSection.tsx`
- **Generales / UI:** `Header.tsx`, `Sidebar.tsx`, `Modal.tsx`, `NotificationBell.tsx`, `SaveButton.tsx`, `Loader.tsx`

## 2. Mobile Components (React Native / Expo)
Ubicación: `apps/mobile/src/components`

- **UI Atoms:** `Button.tsx`, `Card.tsx`, `Input.tsx`, `Loader.tsx`
- **Domain Specific:** `TourCard.tsx`

## 3. Desktop Components (Electron / React)
Ubicación: `apps/desktop/renderer/src/components`

- **UI Atoms:** `Button.tsx`, `Card.tsx`
- **Layout:** `Navbar.tsx`, `Sidebar.tsx`

---
**Análisis:** Existe una brecha masiva entre Web (rica en lógica de dominio) y Mobile/Desktop (enfocadas en UI básica). Se requiere portar la lógica de negocio a componentes compartidos.
