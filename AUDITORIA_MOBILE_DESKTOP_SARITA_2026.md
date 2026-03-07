# INFORME DE AUDITORÍA TÉCNICA INTEGRAL: CAPAS MOBILE Y DESKTOP - ECOSISTEMA SARITA 2026

**Fecha:** 07 de Marzo de 2026
**Responsable:** Jules (AI Senior Engineer)
**Estado Global:** Fase de Cimentación / Arquitectura Base

---

## 1. RESUMEN EJECUTIVO
Tras un análisis exhaustivo del repositorio actual del ecosistema SARITA, se determina que las capas de cliente **Mobile App (React Native)** y **Desktop App (Electron)** se encuentran en una etapa de **madurez 0 (Skeleton/Planificación)**. Aunque la arquitectura Single Backend – Multi Client está sólidamente definida en el núcleo Django, las implementaciones específicas de los clientes móvil y escritorio no existen físicamente en la estructura de archivos actual, a excepción de un esqueleto inicial en `sarita-platform/shared-sdk`.

El backend está 100% preparado para recibir estos clientes, pero se requiere la activación inmediata de los repositorios/carpetas de front-end móvil y escritorio para cumplir con los estándares de clase mundial.

---

## 2. ESTADO DE MADUREZ POR CAPA

| Capa | Estado | Madurez | Observaciones |
| :--- | :--- | :--- | :--- |
| **Backend (Django)** | Operativo | 100% | Listo para Multi-Client (JWT, RS256, CORS). |
| **Web Dashboard** | Operativo | 95% | Funcional pero con lógica no compartida. |
| **Mobile (React Native)** | Inexistente | 0% | Falta configuración de Metro, Android/iOS folders. |
| **Desktop (Electron)** | Inexistente | 0% | Falta proceso Main/Renderer y empaquetado. |
| **Shared SDK** | Esqueleto | 5% | Solo existe `package.json`. |

---

## 3. ANÁLISIS EXHAUSTIVO (Carpeta por Carpeta / Archivo por Archivo)

### 3.1. Núcleo de Integración: `sarita-platform/shared-sdk/`
- **`package.json`**:
    - *Estado:* Mínimo.
    - *Debilidad:* Solo incluye `axios` y `typescript`.
    - *Faltante Crítico:* No hay exportación de servicios, tipos de TypeScript (Interfaces) ni lógica de interceptores compartida.
    - *Línea de Código:* No hay archivos `.ts` de implementación.

### 3.2. Configuración de Entorno (Environment)
- **Estado Actual:** El backend maneja variables de entorno correctamente, pero no hay archivos `.env.example` o configuraciones específicas para `react-native-config` o `dotenv` en Electron.
- **Riesgo:** Inconsistencia en las URLs de la API entre entornos de desarrollo, staging y producción.

### 3.3. Conexión API Gateway y Autenticación JWT
- **Fortaleza:** El backend ya implementa `rest_framework_simplejwt` con firmas **RS256** (Llaves Privadas/Públicas detectadas en `backend/keys/`).
- **Debilidad:** La lógica de refresco de tokens y persistencia (SecureStore en Mobile / SafeStorage en Electron) no está implementada.
- **Inconsistencia:** El `middleware.ts` de Next.js valida el JWT localmente, pero esta lógica debe ser replicada en el SDK compartido para que el cliente Mobile/Desktop no dependa de implementaciones web.

---

## 4. RIESGOS TÉCNICOS Y DESVIACIONES ARQUITECTÓNICAS

1.  **Duplicación de Lógica (Drift):** Al no tener el SDK compartido activo, existe el riesgo inminente de que se replique la lógica de cálculo de impuestos, validación de formularios y mapeo de datos en cada cliente, violando el principio SARITA de "Single Source of Truth" en el Backend.
2.  **CORS & Seguridad:** La configuración actual de `CORS_ALLOWED_ORIGINS` en `settings.py` solo permite `localhost:3000`. No contempla los esquemas `ms-appx://` (Windows/Electron) o los orígenes de apps móviles.
3.  **Gestión de Sesión:** Next.js usa Cookies `httpOnly`. Los clientes Mobile y Desktop **deben** usar el Header `Authorization: Bearer <token>`, lo cual requiere una validación dual en el backend (ya soportada pero no probada para clientes no-web).

---

## 5. RECOMENDACIONES PARA NIVEL "PRODUCTION-READY" (CLASE MUNDIAL)

### Para el Perfil de Prestador (Vía 2):
Para que un prestador de servicios turísticos compita globalmente, las apps deben ofrecer:
1.  **Offline-First:** Sincronización con base de datos local (SQLite/WatermelonDB) para zonas con poca cobertura.
2.  **Notificaciones Push Geofencing:** Alertas al prestador cuando un turista está cerca de su ubicación (requiere Firebase/APNs).
3.  **Firma Digital Móvil:** Integración con la cámara para escaneo de documentos y biometría.

### Acciones Inmediatas:
1.  **Industrialización del SDK:** Mover todos los servicios de `interfaz/src/services/` a `@sarita/shared-sdk`.
2.  **Estructuración de Mobile:**
    - Crear `apps/mobile/` usando React Native (Expo o CLI).
    - Configurar `metro.config.js` para soportar monorepo (workspace).
3.  **Estructuración de Desktop:**
    - Crear `apps/desktop/` usando Electron.
    - Implementar `auto-updater` para distribución de instaladores (.exe, .dmg).

---

## 6. CONCLUSIÓN DEL AUDITOR
El ecosistema SARITA tiene un "Cerebro" (Backend) de clase mundial, pero carece actualmente de las "Extremidades" (Mobile/Desktop). La estructura es escalable, pero la ausencia de código fuente en estas capas indica que no se ha iniciado la implementación física. Se recomienda proceder con la generación de los boilerplate siguiendo los estándares de seguridad ya establecidos en la Fase 8.
