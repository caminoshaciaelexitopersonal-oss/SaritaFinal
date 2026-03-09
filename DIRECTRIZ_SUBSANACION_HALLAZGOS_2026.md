# DIRECTRIZ DE SUBSANACIÓN DE HALLAZGOS: MOBILE & DESKTOP SARITA 2026

**Versión:** 1.0 - Remediación y Perfeccionamiento de Clase Mundial
**Estado:** EJECUCIÓN PRIORITARIA
**Responsable:** Equipo de Ingeniería Móvil y Escritorio

---

## 1. PROPÓSITO
Esta directriz establece las acciones correctivas obligatorias para resolver los hallazgos técnicos detectados durante la auditoría integral de las capas de cliente (Mobile y Desktop) del ecosistema SARITA. El objetivo es elevar la madurez del sistema a un estándar de **Clase Mundial**, garantizando seguridad, resiliencia y una experiencia de usuario impecable.

---

## 2. MATRIZ DE REMEDIACIÓN DE HALLAZGOS CRÍTICOS

### 2.1. Hallazgo 01: Gestión de Configuración de Entorno (Resuelto parcialmente)
*   **Problema:** Uso de URLs quemadas en `env.ts` para la App Mobile.
*   **Subsanación:**
    1.  Migrar totalmente a `expo-constants` (Realizado en `api.ts`).
    2.  Implementar perfiles de despliegue (`development`, `staging`, `production`) en `app.json` bajo la llave `extra.apiUrl`.
    3.  Validar la inyección de la URL correcta durante el proceso de build de EAS (Expo Application Services).

### 2.2. Hallazgo 02: Resiliencia Offline (N5 Sargento de Sincronización)
*   **Problema:** Estructura de SQLite existente pero falta lógica de vaciado automático de cola ante reconexión.
*   **Subsanación:**
    1.  Implementar un `NetInfo` listener en `SyncSargento.ts` para detectar cambios de conectividad.
    2.  Ejecutar `syncSargento.flush()` automáticamente al recuperar internet.
    3.  Añadir lógica de reintento exponencial (*Exponential Backoff*) para fallos persistentes en el flush.

### 2.3. Hallazgo 03: Seguridad y Persistencia en Desktop
*   **Problema:** Uso de `localStorage` estándar para tokens JWT en la versión de escritorio.
*   **Subsanación:**
    1.  Implementar un puente IPC en `main.ts` que consuma `safeStorage` de Electron.
    2.  Crear `SafeDesktopStorageProvider` en el renderer que invoque este puente.
    3.  Cifrar el token JWT y los datos de perfil (`userData`) utilizando las llaves nativas del sistema operativo (OS Keychain).

### 2.4. Hallazgo 04: Activos Visuales y Marca (Placeholders)
*   **Problema:** Iconos, splash screens y favicon en `apps/mobile/assets/` son archivos vacíos o genéricos.
*   **Subsanación:**
    1.  Generar el set completo de activos con la identidad visual oficial de SARITA.
    2.  Configurar el `adaptive-icon` para Android y el set de iconos multiresolución para iOS.
    3.  Asegurar que el `splash.png` esté correctamente centrado y optimizado para evitar distorsiones en pantallas largas.

### 2.5. Hallazgo 05: Contrato de API Unificado (OpenAPI)
*   **Problema:** Ausencia de una especificación OpenAPI (Swagger) que sirva como contrato único para los clientes.
*   **Subsanación:**
    1.  Generar `openapi.yaml` desde el backend Django utilizando `drf-spectacular`.
    2.  Implementar validación de tipos en el Shared SDK basada en este esquema OpenAPI.
    3.  Asegurar que cualquier cambio en los endpoints del backend rompa el build de los clientes si el contrato no se cumple (Testing de Contratos).

---

## 3. PROTOCOLO DE CALIDAD Y PRUEBAS MULTIPLATAFORMA

Para garantizar que el sistema sea de talla mundial, se deben ejecutar:

1.  **Pruebas de Latencia IA:** Validar que el fallback a Ollama local (Hybrid AI) ocurra en menos de 2 segundos si el backend no responde.
2.  **Pruebas de Firma Digital:** Verificar la integridad SHA-256 de los documentos generados desde Mobile y Desktop comparándolos con el registro en el Ledger Engine.
3.  **Matriz de Compatibilidad:**
    *   **iOS:** Pruebas en iPhone 13 a 15 (iOS 16+).
    *   **Android:** Pruebas en Android 12, 13 y 14.
    *   **Windows/macOS:** Instaladores generados con `electron-builder` firmados digitalmente.

---

## 4. CRONOGRAMA DE SUBSANACIÓN (Sprints)

*   **Semana 1:** Implementación de `safeStorage` en Desktop y `NetInfo` en Mobile.
*   **Semana 2:** Generación de activos visuales y configuración de perfiles de build.
*   **Semana 3:** Testing de contratos OpenAPI y validación de la jerarquía de Agentes N1-N7.

---

**Estado Final de la Subsanación:** EN PROCESO DE CIERRE TÉCNICO.
