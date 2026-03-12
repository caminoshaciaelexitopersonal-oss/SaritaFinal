# COMPONENT INVENTORY: SARITA PLATFORM v1.0
**Lead Auditor:** Jules (Senior AI Software Engineer)
**Date:** March 2026

## 1. Unified Components (@sarita/shared-ui)
| Component | Web | Mobile | Desktop | Status |
| :--- | :---: | :---: | :---: | :--- |
| `UnifiedGovernmentDashboard` | ✔ | ✔ | ✔ | Stable |
| `UnifiedProviderDashboard` | ✔ | ✔ | ✔ | Stable |
| `AttractionCard` | ✔ | ✔ | ✔ | Stable |
| `ReservationTable` | ✔ | ❌ | ✔ | Partial (Mobile uses Card) |
| `KPIWidget` | ✔ | ✔ | ✔ | Stable |
| `InteractiveRouteMap` | ✔ | ✔ | ✔ | Stable |
| `DataExporter` | ✔ | ❌ | ✔ | Web/Desktop only |

## 2. Shared SDK Services
| Service | Domain | Consumed By |
| :--- | :--- | :--- |
| `AuthService` | Identity | Web, Mobile, Desktop |
| `ControlTowerService`| Governance | Web, Mobile, Desktop |
| `SyncEngine` | Persistence | Mobile, Desktop |
| `BillingService` | ERP | Web, Desktop (Mobile ⚠️) |

## 3. Platform Specifics (Bridge)
- **Desktop:** `ipcMain` for Printing and Local DB.
- **Mobile:** `expo-secure-store` and `expo-notifications`.
- **Web:** `next-pwa` Service Worker logic.
