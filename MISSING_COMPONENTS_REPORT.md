# MISSING COMPONENTS REPORT: SARITA ECOSYSTEM

## 1. Desktop Platform (Electron)
- **Admin Users Manager:** Falta portar `UserManager.tsx` y `GlobalPermission` controls.
- **AI Local Bridge:** Interfaz para configuración de Ollama local vía IPC.
- **Inmersive Discovery:** No existen los componentes de `MapComponent` y `ImageSlider` en la versión de escritorio de "Descubre".
- **Real-time Analytics:** Falta el dashboard de `StatisticsDashboard` en la Torre de Control Desktop.

## 2. Mobile Platform (Expo)
- **Advanced Form Builder:** El creador de formularios (`FormBuilder`) solo existe en Web; Mobile solo permite llenado (`FormFiller`).
- **Regional Analytics:** Los reportes de `RegionalAnalytics` son limitados en comparación con la versión Web.
- **Audit Logs:** Falta el visualizador de `AuditLogViewer`.

## 3. Web Platform (Next.js)
- **Offline Sync Manager:** Aunque Web es online-only, falta una interfaz para monitorear el estado de sincronización de otros clientes (Mobile/Desktop) asociados al tenant.

---
*Generated on March 2026.*
