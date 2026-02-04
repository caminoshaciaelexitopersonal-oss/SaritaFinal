# GOVERNANCE VISUAL CONTROL MATRIX - SARITA

**Fecha:** 24 de Mayo de 2024
**Estado:** Auditoría de Interfaz de Gobernanza

## 1. INDICADORES DE CUMPLIMIENTO (GRC)
| Componente | Ubicación | Función Visual | Estado |
| :--- | :--- | :--- | :--- |
| `GRCIndicator` | Módulos Críticos ERP | Muestra Riesgos Activos, Controles Aplicados y Estado del Módulo (Operativo/Solo Lectura). | ✅ Activo |
| `TraceabilityBanner` | Vistas de Datos | Expone el origen del dato (API), el modelo de backend y el nivel de certeza/estabilidad del flujo. | ✅ Activo |
| `AuditGuard` (Banner) | DashboardLayout | Franja ámbar persistente cuando el "Modo Auditoría" está activo para el SuperAdmin. | ✅ Activo |

## 2. CONTROL DE AUTORIDAD (UI/UX)
- **¿Quién decide?**: Los módulos exponen indicadores de "Optimización IA" vs "Intervención Manual" (ej. en Centro de Soberanía).
- **Nivel de Autoridad**: El `GRCIndicator` muestra explícitamente el ROL del usuario activo que accede a la información.
- **Transparencia SADI**: El `SADIVoiceLayer` y `VoiceConfirmation` proporcionan feedback visual claro sobre el estado del motor de voz (Escuchando/Procesando/Confirmando).

## 3. ESTADOS DE EJECUCIÓN
- **Modo Demo**: Claramente identificado en los banners de trazabilidad para módulos en desarrollo (Funnel Builder, Marketing).
- **Modo Real**: Identificado como "Datos reales - Backend validado" en módulos contables, operativos y financieros.

## 4. CONCLUSIÓN
La interfaz cumple con la directiva de exponer la gobernanza sin necesidad de activar la lógica compleja de backend. El usuario tiene visibilidad total sobre la integridad, el riesgo y la autoridad de la información que consume.
