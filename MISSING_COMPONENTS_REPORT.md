# MISSING COMPONENTS REPORT: SARITA PLATFORM v1.0
**Lead Auditor:** Jules (Senior AI Software Engineer)
**Date:** March 2026

## 1. Brechas en Desktop (Electrón)
- **Institutional Layer:** Falta `AdminAccountingScreen` y `GovernanceKernelMonitor` (actualmente solo en Web).
- **Human Capital:** Ausencia de `AdminPayrollScreen` para gestión de nómina local.
- **Turismo:** No existe `InteractiveTourismMap` (solo visor estático).

## 2. Brechas en Mobile (Expo)
- **Advanced Admin:** Falta `AuditLogViewer` y `LLMConfigManager`.
- **Prestador:** `BusinessReportsScreen` es limitado en comparación con los gráficos interactivos de la Web.

## 3. Brechas en Web (Next.js)
- **Resilience:** Falta el indicador visual de `OfflineSyncStatus` que sí poseen las apps nativas.

---
**Prioridad de Acción:**
1.  Portar `AnalyticsDashboard` a Desktop.
2.  Implementar `UserPermissionMatrix` en Mobile.
3.  Habilitar `OfflineMode` en Web via Service Workers.
