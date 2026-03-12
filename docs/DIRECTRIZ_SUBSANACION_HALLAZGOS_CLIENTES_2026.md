# DIRECTRIZ DE SUBSANACIÓN DE HALLAZGOS: CLIENTES MOBILE Y DESKTOP 2026

**Versión:** 1.0 - Estándar de Excelencia Operativa
**Estado:** MANDATARIO / EJECUCIÓN INMEDIATA
**Fecha:** 24 de Mayo de 2024

---

## 1. PROPÓSITO
Tras la Auditoría Técnica Integral realizada a las capas de cliente (Mobile y Desktop) del ecosistema SARITA, se han identificado puntos críticos que requieren subsanación inmediata para elevar el sistema a un nivel de **Clase Mundial**. Esta directriz detalla los hallazgos y las acciones correctivas obligatorias.

---

## 2. HALLAZGOS Y ACCIONES DE SUBSANACIÓN

### 2.1 Seguridad en la Persistencia (Desktop)
*   **Hallazgo:** Los tokens JWT se almacenaban en `localStorage` en texto plano, vulnerable a accesos físicos no autorizados.
*   **Acción Correctiva (SUBSANADO):** Se migró la lógica de `apps/desktop/renderer/src/services/storage.ts` para utilizar un puente IPC hacia `safeStorage` de Electron.
*   **Mandato:** Ninguna aplicación de escritorio SARITA debe utilizar `localStorage` para datos sensibles a partir de esta fecha.

### 2.2 Sincronización y Resiliencia (Mobile)
*   **Hallazgo:** El sistema `SyncSargento` (N5) está presente pero solo se utiliza en módulos de "Mi Negocio", dejando al usuario viajero (Vía 1) vulnerable ante caídas de red durante reservas críticas.
*   **Acción de Subsanación:** Extender `SyncSargento` a los servicios de `bookingService.ts` y `paymentService.ts` en Mobile para asegurar transacciones resilientes en cualquier contexto geográfico.

### 2.3 Optimización de Rendimiento (UX Parity)
*   **Hallazgo:** La carga inicial de la aplicación móvil es pesada debido a la importación masiva de pantallas en `MainNavigator.tsx`.
*   **Acción de Subsanación:** Implementar **Code Splitting / Lazy Loading** mediante `React.lazy()` para módulos no críticos. Priorizar la carga del Home y el Wallet.

### 2.4 Interoperabilidad de IA Local (Hardware Adaptation)
*   **Hallazgo:** Los modelos de IA locales (Ollama) en Desktop y Mobile se seleccionan mediante lógica estática basada en RAM, sin considerar la carga térmica o el estado de la batería.
*   **Acción de Subsanación:** Robustecer `deviceIntelligence.ts` y `hardwareIntelligence.ts` para que la selección del modelo (ej. `llama3` vs `phi3`) sea dinámica y considere el perfil energético del dispositivo.

### 2.5 Consistencia de UI (Design System)
*   **Hallazgo:** Existen ligeras variaciones en el radio de los bordes y las sombras entre los componentes `Card.tsx` de Mobile y Desktop frente al frontend Web.
*   **Acción de Subsanación:** Unificar las variables de estilo (Tokens de Diseño) en el Shared SDK o asegurar que los archivos `tailwind.config.js` y `index.css` de ambas capas consuman exactamente los mismos valores hexadecimales del manual de marca SARITA.

---

## 3. PROTOCOLO DE VERIFICACIÓN DE SUBSANACIÓN
Para considerar un hallazgo como subsanado, se debe:
1.  **Ejecutar Auditoría SHA-256:** Verificar que el cambio no altere la cadena de integridad si afecta al Ledger Engine.
2.  **Prueba de Estrés (Offline):** Validar que la sincronización diferida funcione correctamente bajo simulación de red 2G/Latencia alta.
3.  **Análisis de Seguridad:** Realizar un escaneo de dependencias rotas tras la actualización de Electron o React Native.

---

## 4. CONCLUSIÓN
La subsanación de estos hallazgos no es opcional. Es el paso final para garantizar que SARITA sea una plataforma inexpugnable, rápida y verdaderamente inteligente, lista para liderar el mercado global de tecnología turística y ERP.

**ESTADO:** En proceso de remediación continua.
