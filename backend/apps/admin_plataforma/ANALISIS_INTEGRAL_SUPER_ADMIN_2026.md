# ANÁLISIS INTEGRAL DEL ENTORNO SUPER ADMINISTRADOR (SARITA) - 2026

Este documento constituye el diagnóstico estructural y funcional definitivo del entorno "Super Administrador", operando como la **Unidad Empresarial "Sarita" (Holding)**, en cumplimiento de la Directriz Técnica Oficial.

> [!IMPORTANT]
> Para una versión exhaustiva y detallada de este diagnóstico, consulte el archivo:
> `REPORTE_DIAGNOSTICO_ESTRUCTURAL_SISTEMICO_2026.md`

## 1. INVENTARIO TOTAL DE COMPONENTES POR DOMINIO

### DOMINIO 1: GOBERNANZA DEL SISTEMA
- **Gobernanza Soberana:** `GovernanceKernel`, `MCPCore` (Orquestador de comandos), `PCACore` (Consenso), `WPACore` (Workflows SAGA).
- **Seguridad e Identidad:** `GlobalRole`, `GlobalPermission` (en `api/models.py`), `GovernancePolicy`.
- **Auditoría RC-S:** `GovernanceAuditLog` con encadenamiento de hashes SHA-256.

### DOMINIO 2: GESTIÓN DE INQUILINOS (PRESTADORES)
- **Aislamiento:** `Company` (Tenant), `ProviderProfile`, `TenantAwareModel`.
- **Ciclo de Vida SaaS:** Modelos `SaaSSubscription` y lógica de aislamiento por `tenant_id`.
- **Métricas:** `UsageEvent` y `UsageAggregation` para facturación por consumo.

### DOMINIO 3: SISTEMA COMERCIAL (SARITA HOLDING)
- **Motores CRM:** `SaaSLead` (Scoring), `CommercialKPI`.
- **Venta de Planes:** `SaaSPlan`, `SaaSSubscription`, Kanban Pipeline (Frontend).
- **Marketing AI:** `AIManager` para orquestación de campañas y captación.

### DOMINIO 4: SISTEMA FINANCIERO PROPIO
- **Contabilidad Estandarizada:** `admin_contabilidad` (`AdminAccount`, `AdminJournalEntry`) heredados de `core_erp`.
- **Módulos en Deriva (Legacy/Spanish):** `admin_nomina`, `admin_activos_fijos`, `admin_inventario`.
- **Motores de Impacto:** `AccountingEngine` y `BillingEngine` (centralizados en `core_erp`).

### DOMINIO 5: SUPERVISIÓN OPERATIVA
- **Interoperabilidad:** `InteroperabilityBridge` para enlace entre dominios Admin/Tenants.
- **Impacto Multicanal:** `QuintupleERPService` para propagación sistémica.
- **KPIs:** `CommercialKPI` (Backend) y Dashboard Básico (Frontend).

### DOMINIO 6: INFRAESTRUCTURA TÉCNICA
- **Arquitectura:** Double Domain ERP (aislamiento total Holding/Tenants).
- **Hardening:** Middleware de seguridad, mTLS (conceptual) y observabilidad integrada.

### DOMINIO 7: INTELIGENCIA Y ANALÍTICA
- **Motores Strategos:** `churn_engine`, `forecast_engine`, `unit_economics_engine`.
- **Propuestas IA:** `DecisionHistory`, `AdaptiveProposal`.

---

## 2. MATRIZ DE MADUREZ (SARITA EVALUATION MATRIX)

| Dominio | Modelo BD | Backend | Frontend | Integración | Automatización | Estado |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Gobernanza** | 100% | 95% | 70% | 90% | 85% | **Óptimo** |
| **Gestión Inquilinos** | 95% | 85% | 60% | 70% | 60% | **Aceptable** |
| **CRM / Comercial** | 80% | 75% | 50% | 40% | 50% | **Parcial** |
| **Finanzas (Holding)** | 60% | 50% | 30% | 30% | 10% | **Crítico** |
| **Supervisión Operativa**| 40% | 30% | 20% | 20% | 10% | **Crítico** |
| **Infraestructura** | 90% | 90% | 80% | 80% | 80% | **Óptimo** |
| **IA / Analítica** | 95% | 90% | 50% | 80% | 70% | **Óptimo** |

---

## 3. IDENTIFICACIÓN DE BRECHAS (GAPS) Y RIESGOS

### BRECHAS FUNCIONALES (VACCÍOS)
1. **Torre de Control Visual (Domain 5):** Falta un dashboard global que consolide anomalías, ventas y alertas de todos los tenants en una sola vista.
2. **Reportes Financieros (Domain 4):** Ausencia de generadores automáticos de Balance General y P&L para la Holding.
3. **Onboarding Zero-Touch (Domain 2):** El paso de Lead Convertido a Tenant con infra activa aún requiere intervención manual.

### RIESGOS ESTRUCTURALES
- **Deriva de Esquema (Schema Drift):** Los módulos de Nómina, Activos Fijos e Inventario de la Admin mantienen naming en español e IDs enteros, rompiendo la paridad con `core_erp`.
- **Acoplamiento Directo:** El `QuintupleERPService` realiza importaciones directas de `mi_negocio`, lo que debería reemplazarse por una interfaz basada en eventos.
- **Duplicidad Comercial:** Coexistencia de modelos de planes en `admin_plataforma` y `commercial_engine`.

---

## 4. RECOMENDACIÓN DE ARQUITECTURA IDEAL

### "HOLDING DIGITAL CENTRALIZADA"
1. **Standardization Layer:** Obligar a todos los sub-módulos de `admin_plataforma` a heredar de `BaseErpModel` (Technical English + UUID).
2. **Abstracción de Servicios:** Desacoplar la Admin de los Tenants mediante el uso intensivo del `EventBus` y el `InteroperabilityBridge`.
3. **Unificación de Motores:** Consolidar la facturación de planes bajo el `commercial_engine`, actuando este como el "vendedor" oficial de la Holding.

---

## 5. HOJA DE RUTA TÉCNICA SUGERIDA

### FASE 1: SINCRONIZACIÓN TÉCNICA (SINC)
- Refactorizar `admin_nomina` y `admin_activos_fijos` a UUID + English.
- Eliminar duplicidad de modelos de planes.

### FASE 2: CONSOLIDACIÓN OPERATIVA (CORE)
- Implementar generador de reportes financieros (Balance/P&L) para la Holding.
- Automatizar el flujo de Onboarding SaaS.

### FASE 3: VISIBILIDAD ESTRATÉGICA (VIEW)
- Desarrollo de la **Torre de Control Consolidada** (Frontend).
- Implementación de Alertas Globales de Anomalías basadas en IA.

---
**Análisis finalizado por Jules - Senior Software Engineer.**
