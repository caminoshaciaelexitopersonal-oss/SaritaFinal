# DIRECTRIZ MAESTRA DE ROBUSTEZ Y PERFECCIÓN: CLIENTES MOBILE Y DESKTOP SARITA 2026

**Versión:** 4.0 - Interoperabilidad Total, UX Parity y Orquestación IA N1-N7
**Estado:** MANDATARIO / NIVEL 10
**Fecha:** 24 de Mayo de 2024

---

## 1. OBJETIVO ESTRATÉGICO
Transformar las aplicaciones **Mobile (Expo/React Native)** y **Desktop (Electron/React)** en espejos funcionales y estéticos del ecosistema web oficial de SARITA. Se busca alcanzar la **Interoperabilidad Total**, donde cada API disponible en el backend sea consumida eficientemente, permitiendo que un prestador de servicios turísticos opere su negocio con estándares de clase mundial desde cualquier dispositivo.

---

## 2. ARQUITECTURA DE INTEROPERABILIDAD Y AGENTES

### 2.1 Centralización en el Shared SDK
*   **Mandato:** Ninguna lógica de validación contable, cálculo de impuestos (DIAN UBL 2.1) o reglas de negocio de IA debe ser escrita en el cliente.
*   **Acción:** Utilizar `@sarita/shared-sdk` para toda interacción con el API.
*   **Agentes IA:** Las interfaces deben actuar como terminales para la jerarquía de agentes:
    *   **N1-N2 (Estratégicos):** Dashboard de control macro y simulaciones de impacto regional (Solo Admin/Gobierno).
    *   **N3-N4 (Operativos):** Copilotos de gestión en el ERP "Mi Negocio" que sugieren optimización de precios y recursos.
    *   **N5 (Sargento):** Garantiza la sincronización de datos y la integridad transaccional offline.
    *   **N6-N7 (Tácticos):** Chatbots y comandos de voz para interacción rápida del usuario final.

---

## 3. MAPA DE RUTA: PANTALLAS Y FUNCIONALIDADES REQUERIDAS

### 3.1 VÍA 1: CIUDADANOS Y TURISTAS (EXPANDIDO)
Para igualar al frontend oficial (`interfaz/src/app/descubre` y `mi-viaje`), se deben robustecer:
*   **Exploración Avanzada:** Filtros dinámicos por categorías (Atractivos, Historia, Agenda Cultural).
*   **Monedero Real:** Gestión de pagos QR, historial de transacciones y recompensas por lealtad.
*   **Delivery Integrado:** Rastreo en tiempo real, chat con el repartidor y calificación de platos.
*   **Pasaporte Digital:** Visualización de logros, sellos de visita y preferencias culturales.

### 3.2 VÍA 2: EMPRESARIOS - ERP "MI NEGOCIO" (CLASE MUNDIAL)
Nivelación total con el Dashboard operativo empresarial:
*   **Módulo Contable (GESCONTABLE):**
    *   Visualización de Balance General y Estado de Resultados.
    *   Registro de asientos contables con validación de partida doble.
    *   Acceso a nómina y depreciación de activos fijos.
*   **Módulo Comercial (CRM):**
    *   Embudo de ventas interactivo (Pipeline).
    *   Gestión de clientes con historial de compras y preferencias.
    *   Lanzamiento de promociones segmentadas.
*   **Módulo Operativo:**
    *   Calendario de reservas sincronizado.
    *   Gestión de personal (staff) y recursos (vehículos, equipos).
    *   Check-in/Check-out digital de turistas.
*   **Módulo Archivístico:**
    *   Carga y visualización de documentos legales y técnicos.
    *   Trazabilidad SHA-256 de cada archivo subido.

### 3.3 VÍA 3: GUBERNAMENTAL Y ADMIN (CONTROL TOTAL)
*   **Cerebro Global:** Visualización de métricas GMV, crecimiento de usuarios y salud del ecosistema.
*   **Gestión de Crisis:** Tablero de alertas globales y monitoreo de eventos masivos.
*   **Configuración de IA:** Interfaz para ajustar parámetros de los agentes y modelos locales (Ollama).

---

## 4. ESTÁNDARES DE ROBUSTEZ TÉCNICA

1.  **Seguridad de Grado Bancario:**
    *   Mobile: Almacenamiento en `SecureStore`.
    *   Desktop: Migración inmediata a `safeStorage` de Electron.
2.  **Resiliencia Total:** Implementación de `SyncSargento` en todos los formularios para que el sistema funcione 100% offline y sincronice al detectar red.
3.  **Hardware Intelligence:**
    *   Uso de `deviceIntelligence.ts` y `hardwareIntelligence.ts` para adaptar la carga de IA al dispositivo.
    *   Integración nativa en Desktop para impresoras térmicas y escáneres de identidad.
4.  **UX Parity:** Uso estricto de componentes `ui/index.tsx` (Card, Button, Loader) compartidos para que la marca SARITA sea consistente.

---

## 5. CONCLUSIÓN: EL PRESTADOR DE CLASE MUNDIAL
Con esta directriz, el prestador de servicios no solo usa una app, sino que opera una **Estación de Trabajo Inteligente**. La interoperabilidad total asegura que un cambio en la contabilidad en el escritorio se refleje en el reporte móvil instantáneamente, y que los agentes IA trabajen en segundo plano para maximizar la rentabilidad del negocio turístico bajo el modelo SARITA.

**MANDATO:** Nivelación completada para Junio 2026.
