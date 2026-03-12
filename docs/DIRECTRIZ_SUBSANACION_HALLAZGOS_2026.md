# DIRECTRIZ MAESTRA: SUBSANACIÓN DE HALLAZGOS Y EXCELENCIA TÉCNICA 2026
**Hacia la Transformación Digital de Talla Mundial**

**Objetivo:** Eliminar la deuda técnica, cerrar las brechas funcionales y elevar el sistema SARITA a un estándar de ingeniería de clase mundial (Production-Ready Nivel 10+).

---

## 1. ELIMINACIÓN DE DEUDA TÉCNICA (LIMPIEZA DE CÓDIGO)
El sistema presenta **335 marcadores** de deuda acumulada. No es posible operar a escala nacional con este nivel de incertidumbre.

- **[P0] Acción Inmediata:** Implementar la lógica real en los stubs de `BillingEngine` y `AccountingEngine`. Específicamente el método `process_usage_billing` debe pasar de un `pass` a una integración con el `usage_billing` module.
- **[P0] Resolución de TODOs Críticos:** Priorizar los TODOs en `nomina/views.py` (Cálculo de provisiones) y `governance_service.py` (Políticas dinámicas).
- **[P1] Manejo de Excepciones:** Reemplazar todos los bloques `except: pass` por logging estructurado vía `EnterpriseJSONFormatter` y ruteo de errores a la torre de control.

## 2. CIERRE DE BRECHAS DE PARIDAD (MULTI-CLIENT)
La arquitectura de "Cerebro Único" exige paridad funcional en los tres cuerpos (Web, Mobile, Desktop).

- **[P1] Fortalecimiento Desktop:** Implementar los sub-módulos de Gestión Contable, Nómina y Archivística en la aplicación Electron, replicando la lógica de la versión Web.
- **[P1] Autonomía Mobile:** Habilitar el panel de configuración de niveles de autonomía IA (N1-N7) en la aplicación móvil para el rol de Gobierno.
- **[P2] Shared Library Strategy:** Unificar los hooks y servicios en `sarita-platform/shared-sdk` para eliminar la duplicación actual entre `interfaz` y `web-ventas-frontend`.

## 3. EVOLUCIÓN DE LA INTELIGENCIA ARTIFICIAL (IA SOBERANA)
La jerarquía militar de agentes debe ser auditable y altamente resiliente.

- **[P1] Certificación de Soldados (N6):** Implementar las pruebas de resistencia para el 30% restante de soldados que operan bajo "Mocks". Cada soldado debe tener un contrato de entrada/salida validado por el `GovernanceKernel`.
- **[P1] Memoria y Contexto:** Activar el `RiskAnalyticsService` para que los Capitanes (N3) puedan tomar decisiones basadas en proyecciones financieras reales y no solo en reglas estáticas.

## 4. BLINDAJE DE INFRAESTRUCTURA Y SEGURIDAD
Preparación definitiva para AWS y cumplimiento internacional.

- **[P0] Stress Testing AWS:** Realizar una simulación de carga masiva (5,000 concurrentes) en un entorno de infraestructura idéntico a producción para validar el `DatabaseRouter` y los bloqueos de `Wallet`.
- **[P1] Seguridad S-0.3:** Implementar el "Anillo de Defensa 3" que incluye el congelamiento automático de cuentas ante detecciones de anomalías por la IA de seguridad.
- **[P2] Cumplimiento Global:** Implementar el cifrado en reposo para datos sensibles en PostgreSQL y SQLite (AES-256) cumpliendo con GDPR.

---

## ESTRATEGIA DE EJECUCIÓN (ROADMAP)

### FASE 1: Estabilización y Hardening (30 días)
- **Meta:** 0 Deuda Técnica P0.
- **Entregable:** Informe de cobertura de tests al 85% y stubs contables cerrados.

### FASE 2: Alineación y Paridad (45 días)
- **Meta:** 100% Paridad Estructural y Funcional.
- **Entregable:** Release v1.1 con Desktop y Mobile nivelados.

### FASE 3: Inteligencia Autónoma (60 días)
- **Meta:** IA N1-N7 operando con toma de decisiones real.
- **Entregable:** Dashboard de Auditoría Forense de IA activo.

### FASE 4: Lanzamiento Mundial (90 días)
- **Meta:** Certificación de Producción Nivel 10.
- **Entregable:** Despliegue Multi-región en AWS con WAF avanzado.

---
**Firmado por Jules.**
*Lead Architect & Senior Engineer.*
**Fecha:** Marzo 2026.
