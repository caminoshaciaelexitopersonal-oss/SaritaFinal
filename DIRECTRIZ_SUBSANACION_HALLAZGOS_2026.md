# DIRECTRIZ DE SUBSANACIÓN DE HALLAZGOS TÉCNICOS: SARITA MOBILE & DESKTOP 2026

**Responsable:** Jules (AI Senior Software Engineer)
**Estatus:** Crítico - Implementación Obligatoria
**Referencia de Auditoría:** AUDITORIA_DETALLADA_MOBILE_DESKTOP_2026.md

---

## 1. HALLAZGO A1: AUSENCIA DE TESTING AUTOMATIZADO
**Riesgo:** Regresiones funcionales en módulos críticos de contabilidad y pagos.

### Acción Correctiva:
Implementar Jest y React Native Testing Library.
```typescript
// Ejemplo de Test para BusinessService.ts
import { businessService } from './businessService';
import { api } from './api';

jest.mock('./api');

test('debe obtener el dashboard contable correctamente', async () => {
  (api.get as jest.Mock).mockResolvedValue({ data: { total_ventas: 100 } });
  const data = await businessService.getContabilidadGeneral();
  expect(data.total_ventas).toBe(100);
});
```

---

## 2. HALLAZGO A2: SEGURIDAD DE PERSISTENCIA EN DESKTOP
**Riesgo:** Extracción manual de tokens JWT desde el navegador/disco.

### Acción Correctiva:
Migrar a `safeStorage` de Electron.
```typescript
// En main.ts (Proceso Principal)
ipcMain.handle('secure-store-set', (event, key, value) => {
  const encrypted = safeStorage.encryptString(value);
  db.save(key, encrypted);
});

// En el Renderer (DesktopStorageProvider.ts)
async setItem(key, value) {
  await window.electronAPI.secureStoreSet(key, value);
}
```

---

## 3. HALLAZGO A3: GESTIÓN DE VARIABLES DE ENTORNO
**Riesgo:** Exposición de endpoints de desarrollo en producción.

### Acción Correctiva:
Usar `expo-constants` en Mobile.
```typescript
// apps/mobile/src/config/env.ts
import Constants from 'expo-constants';
export const API_URL = Constants.expoConfig?.extra?.apiUrl || "https://api.sarita.travel";
```

---

## 4. HALLAZGO A4: BRANDING Y ASSETS DE PRODUCCIÓN
**Riesgo:** Rechazo en tiendas (Google Play/App Store) por falta de assets de marca.

### Acción Correctiva:
Sustituir placeholders en `apps/mobile/assets/` con archivos PNG/SVG optimizados siguiendo la guía de estilo SARITA.

---

## 5. HALLAZGO A5: MONITOREO Y OBSERVABILIDAD
**Riesgo:** Fallos silenciosos en dispositivos de prestadores sin reporte técnico.

### Acción Correctiva:
Integrar **Sentry SDK** en el punto de entrada de ambas apps.
```typescript
Sentry.init({
  dsn: "https://sarita-sentry-dsn@sentry.io/project",
  tracesSampleRate: 1.0,
});
```

---

**Cronograma de Ejecución:**
*   **Semana 1:** Seguridad (A2) y Configuración (A3).
*   **Semana 2:** Implementación de Pruebas Unitarias (A1).
*   **Semana 3:** Assets Visuales (A4) y Sentry (A5).

---
**Aprobado por Ingeniería de Software SARITA**
