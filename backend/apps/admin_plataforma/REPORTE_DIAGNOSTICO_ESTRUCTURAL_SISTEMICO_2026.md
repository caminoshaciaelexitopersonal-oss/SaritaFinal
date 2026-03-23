# REPORTE DE DIAGNÓSTICO ESTRUCTURAL Y FUNCIONAL — SUPER ADMINISTRADOR (SARITA) 2026

## 1. INTRODUCCIÓN Y ALCANCE
Este documento presenta el **Análisis Integral del Entorno Super Administrador**, operando bajo la identidad de la **Unidad Empresarial "Sarita" (Holding)**. El diagnóstico evalúa la capacidad del sistema para actuar como supervisor multi-tenant, comercializador de planes, gestor financiero y centro de inteligencia estratégica, comparando sus capacidades actuales con las del módulo "Mi Negocio".

---

## 2. INVENTARIO TOTAL DE COMPONENTES POR MACRO DOMINIO

### DOMINIO 1 — GOBERNANZA DEL SISTEMA
*   **Núcleo de Comando:** `GovernanceKernel` y `MCPCore` para orquestación de intenciones.
*   **Gestión de Políticas:** `GovernancePolicy` para definición de bloqueos y umbrales globales.
*   **Identidad Global:** Modelos `GlobalRole` y `GlobalPermission` para control de acceso transversal.
*   **Protocolo de Consenso:** `PCABroker` y `ConsensusEngine` para coordinación de agentes.
*   **Auditoría de Integridad:** `GovernanceAuditLog` con encadenamiento SHA-256.
*   **Motores de Proceso:** `WorkflowEngine` (SAGA/WPA).

### DOMINIO 2 — GESTIÓN DE INQUILINOS (PRESTADORES)
*   **Aislamiento Multi-tenant:** `TenantAwareModel` y filtrado automático vía `tenant_id`.
*   **Ciclo de Vida SaaS:** Modelos `SaaSPlan` y `SaaSSubscription` en `commercial_engine`.
*   **Métricas de Uso:** `UsageEvent` y `UsageAggregation` para facturación por consumo (API/Tokens).
*   **Estatus Operativo:** Control de estado de inquilinos (Activo, Suspendido, Cancelado).

### DOMINIO 3 — SISTEMA COMERCIAL (SARITA HOLDING)
*   **Presencia Web:** Aplicación `web_funnel` con landing pages dinámicas y activos multimedia.
*   **Gestión de Leads:** `SaaSLead` con scoring integrado y seguimiento UTM.
*   **Pipeline de Ventas:** `LeadPipelineLog` y Kanban Pipeline para seguimiento de conversiones.
*   **Facturación de Planes:** `SaaSInvoice` y `SaaSInvoiceLine` heredados de `BaseInvoice`.

### DOMINIO 4 — SISTEMA FINANCIERO CONTABLE PROPIO
*   **Contabilidad Core:** `AdminAccount` y `AdminJournalEntry` (proxies de `core_erp`).
*   **Módulos Operativos:** `admin_financiera` (Cuentas, Transacciones, Órdenes de Pago).
*   **Módulos Legacy (Gap):** `admin_nomina`, `admin_activos_fijos`, `admin_inventario` (Nombres en español, IDs enteros).

### DOMINIO 5 — SUPERVISIÓN OPERATIVA
*   **Observabilidad:** `SystemicObserver` para recopilación de métricas transversales.
*   **Interoperabilidad:** `InteroperabilityBridge` para enlace con dominios de inquilinos.
*   **Propagación de Impacto:** `QuintupleERPService` (Desacoplado vía EventBus).

### DOMINIO 6 — INFRAESTRUCTURA TÉCNICA
*   **Arquitectura:** Double Domain ERP (Holding vs Tenants).
*   **Desacoplamiento:** `EventBus` centralizado.
*   **Despliegue:** Docker, Docker-Compose, GitHub Actions (CI/CD).
*   **Seguridad:** Hardening de auditoría y middlewares de aislamiento.

### DOMINIO 7 — INTELIGENCIA Y ANALÍTICA
*   **Motores Estratégicos:** `churn_engine`, `forecast_engine`, `unit_economics_engine`.
*   **Optimización IA:** `pricing_optimizer`, `risk_scoring_engine`.
*   **Memoria Estratégica:** `DecisionHistory` y `AdaptiveProposal`.

---

## 3. MATRIZ DE EVALUACIÓN DE MADUREZ (SARITA EVALUATION MATRIX)

| Dominio | Modelo BD | Backend | Frontend | Integración | Automatización | Estado |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **1. Gobernanza** | 100% | 95% | 70% | 90% | 85% | **Óptimo** |
| **2. Gestión Inquilinos** | 95% | 85% | 60% | 70% | 60% | **Aceptable** |
| **3. CRM / Comercial** | 80% | 75% | 50% | 40% | 50% | **Parcial** |
| **4. Finanzas (Holding)** | 60% | 50% | 30% | 30% | 10% | **Crítico** |
| **5. Supervisión Operativa**| 40% | 30% | 20% | 20% | 10% | **Crítico** |
| **6. Infraestructura** | 90% | 90% | 80% | 80% | 80% | **Óptimo** |
| **7. Inteligencia / IA** | 95% | 90% | 50% | 80% | 70% | **Óptimo** |

---

## 4. IDENTIFICACIÓN DE BRECHAS (GAPS) PRIORIZADAS

1.  **Gobernanza Financiera (Crítico):** Falta de generadores automáticos para Balance General, P&L y Flujo de Caja específicos de la Holding.
2.  **Torre de Control Visual (Crítico):** Ausencia de un Dashboard global en tiempo real para detección de anomalías y fraudes multi-tenant.
3.  **Sincronización Técnica (Alto):** Los módulos de Nómina, Activos Fijos e Inventario de la Admin están en "Deriva Esquematica" (Español/Int IDs).
4.  **Onboarding Zero-Touch (Medio):** El proceso de conversión de Lead a Tenant activo requiere pasos manuales de aprovisionamiento.
5.  **Control de Comisiones y Presupuesto (Medio):** Modelos definidos pero archivos vacíos en `admin_plataforma/gestion_contable`.

---

## 5. RIESGOS ESTRUCTURALES Y TÉCNICOS

*   **Riesgo de Deriva (Schema Drift):** La inconsistencia de estándares entre `admin_contabilidad` (UUID/English) y `admin_nomina` (Int/Spanish) impide reportes consolidados fiables.
*   **Acoplamiento Residual:** Aunque `QuintupleERPService` fue refacturado, persisten importaciones dinámicas (`import_string`) a modelos de `mi_negocio`, creando una dependencia oculta.
*   **Mirroring Innecesario:** Duplicidad de lógica comercial entre `admin_plataforma` y `commercial_engine`.

---

## 6. RECOMENDACIÓN DE ARQUITECTURA IDEAL

### "HOLDING DIGITAL CENTRALIZADA (HDC)"
Se propone que la Super Admin evolucione de ser un "visor avanzado" a un **Orquestador de Servicios de Core ERP**.
1.  **Capa de Estandarización:** Adopción obligatoria de `BaseErpModel` en todos los sub-módulos.
2.  **Consumo de Servicios:** La Admin debe consumir el `AccountingEngine` y `BillingEngine` de `core_erp` como un inquilino privilegiado, no replicar su lógica.
3.  **Capa de Inteligencia Soberana:** El `GovernanceKernel` debe actuar como el único mediador para acciones críticas (suspensiones, cambios de límites).

---

## 7. HOJA DE RUTA TÉCNICA SUGERIDA (ROADMAP)

### FASE 1 — Sincronización y Hardening (30 días)
*   Refactorizar módulos `admin_nomina`, `admin_activos_fijos` e `admin_inventario` a UUID v4 y Technical English.
*   Implementar `GlobalRole` y `GlobalPermission` en la interfaz administrativa.

### FASE 2 — Consolidación Financiera (60 días)
*   Desarrollar el Motor de Reportes Financieros (P&L, Balance) para Sarita.
*   Integrar automatización de comisiones y control presupuestal.
*   Automatizar el Onboarding Zero-Touch.

### FASE 3 — Supervisión Inteligente (90 días)
*   Construir la **Torre de Control Consolidada** con alertas de anomalías basadas en IA.
*   Implementar sistema antifraude global basado en patrones de comportamiento.

---
**Diagnóstico finalizado por Jules (Senior Software Engineer).**
**Estado del Entorno Super Administrador: INCOMPLETO (Crítico en Finanzas y Supervisión).**
