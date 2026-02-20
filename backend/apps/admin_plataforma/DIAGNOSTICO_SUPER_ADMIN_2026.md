# DIAGNÓSTICO INTEGRAL DEL ENTORNO SUPER ADMINISTRADOR (SARITA) - 2026

Este documento presenta el diagnóstico estructural y funcional profundo del entorno Super Administrador, actuando como la **Unidad Empresarial Operativa "Sarita" (Holding)**, alineado con la directriz técnica de análisis integral.

## 1. INVENTARIO DE COMPONENTES POR MACRO DOMINIO

### DOMINIO 1: GOBERNANZA DEL SISTEMA
- **GovernanceKernel (`governance_kernel.py`):** Motor soberano que valida autoridad (Sovereign/Delegated/Operational) y resuelve intenciones de negocio.
- **MCP Core (`mcp_core.py`):** Orquestador central de comandos con máquina de estados persistente.
- **PCA Core (`pca_core.py`):** Controlador de consenso entre agentes basado en pesos dinámicos y especialidad.
- **WPA Core (`wpa_core.py`):** Motor de workflows autónomos que implementa el patrón SAGA para reversibilidad.
- **Global Roles & Permissions:** Modelos `GlobalRole` y `GlobalPermission` implementados en el core de identidad (`api/models.py`).
- **Audit Hardening:** Registro `GovernanceAuditLog` con encadenamiento de hashes SHA-256 para integridad forense.

### DOMINIO 2: GESTIÓN DE INQUILINOS (PRESTADORES)
- **Tenant Isolation:** Implementado mediante `Company` (Tenant) y `ProviderProfile`. El aislamiento de datos se garantiza vía `TenantAwareModel`.
- **SaaS Lifecycle:** Modelos `SaaSPlan` y `SaaSSubscription` centralizados en `commercial_engine`.
- **Usage Metrics:** Motores de agregación `UsageEvent` y `UsageAggregation` para facturación basada en consumo.

### DOMINIO 3: SISTEMA COMERCIAL (SARITA HOLDING)
- **AI Marketing OS:** Sistema operativo de marketing en `gestion_comercial` con `AIManager` para orquestación de LLMs (Gemini, Groq, Ollama).
- **Lead Management:** Modelo `SaaSLead` con scoring automatizado en `commercial_engine`.
- **Web Funnel:** Infraestructura de captación y onboarding integrada con la generación automática de perfiles.

### DOMINIO 4: SISTEMA FINANCIERO PROPIO
- **Contabilidad Admin:** Ubicada en `admin_plataforma/gestion_contable`. Utiliza `AdminAccount`, `AdminJournalEntry` heredados de `core_erp`.
- **Motores de Impacto:** `AccountingEngine` y `BillingEngine` (centralizados en `core_erp`) utilizados para procesar la suscripción SaaS.
- **Módulos con Deriva:** `admin_nomina`, `admin_activos_fijos` y `admin_inventario` presentan inconsistencias técnicas (Nombres en español e IDs enteros).

### DOMINIO 5: SUPERVISIÓN OPERATIVA
- **Interoperability Bridge:** Capa para consulta de datos entre dominios aislados (Admin <-> Tenants).
- **Quintuple ERP Service:** Orquestador de impacto financiero multicuenta.
- **Estado:** Crítico. Falta un Dashboard de Anomalías Globales y una Torre de Control visual consolidada.

### DOMINIO 6: INFRAESTRUCTURA TÉCNICA
- **Double Domain ERP:** Arquitectura de aislamiento total que protege la contabilidad de la Holding de los datos de los inquilinos.
- **Security:** Modelo Zero-Trust, mTLS entre agentes y observabilidad técnica integrada.

### DOMINIO 7: INTELIGENCIA Y ANALÍTICA
- **Decision Intelligence:** Modelos `DecisionHistory` y `AdaptiveProposal` para optimización sistémica basada en IA.
- **Agent Performance:** Seguimiento de precisión de agentes para ajuste de autoridad en tiempo real.

---

## 2. MATRIZ DE MADUREZ (SARITA EVALUATION MATRIX)

| Dominio | Modelo BD | Backend | Frontend | Integración | Automatización | Estado |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Gobernanza** | 100% | 95% | 70% | 90% | 85% | **Óptimo** |
| **Gestión Inquilinos** | 95% | 85% | 60% | 70% | 60% | **Aceptable** |
| **CRM / Comercial** | 80% | 75% | 40% | 30% | 50% | **Parcial** |
| **Finanzas (Holding)** | 70% | 60% | 30% | 40% | 20% | **Incompleto** |
| **Supervisión Operativa**| 40% | 30% | 15% | 20% | 10% | **Crítico** |
| **Infraestructura** | 90% | 90% | 80% | 80% | 80% | **Óptimo** |
| **IA / Analítica** | 85% | 80% | 50% | 60% | 40% | **En Desarrollo** |

---

## 3. IDENTIFICACIÓN DE BRECHAS (GAPS) Y RIESGOS

### BRECHAS FUNCIONALES
1. **Torre de Control (Domain 5):** Ausencia de un panel visual que consolide KPIs de todos los tenants en tiempo real (Ventas globales, Reservas, Alertas de riesgo).
2. **Generador de Reportes Financieros (Domain 4):** Falta de automatización para generar el Balance General y P&L consolidado de la Holding "Sarita".
3. **Automatización de Onboarding (Domain 2):** El flujo desde Lead convertido a Tenant activo requiere intervención manual en pasos de infraestructura.

### RIESGOS ESTRUCTURALES
- **Deriva de Esquema (Técnico):**
    - **Inconsistencia de Naming:** Uso masivo de español en nombres de clases y campos en sub-módulos operativos y contables (`Empleado`, `Contrato`, `nombre`, `descripcion`).
    - **Inconsistencia de Identidad:** Falta de UUID v4 como llave primaria en módulos de Nómina, Activos Fijos e Inventario (uso de `INTEGER` IDs).
    - **Divergencia de Herencia:** Múltiples modelos no heredan de `core_erp.base_models`, lo que impide la auditoría sistémica unificada y el rastreo de integridad de hashes.
- **Acoplamiento de Modelos (Arquitectura):** Dependencia directa entre modelos de diferentes dominios que deberían comunicarse vía `EventBus` o servicios de abstracción.

---

## 4. DETALLE DE DERIVA DE ESQUEMA POR MÓDULO

| Módulo | Clase Ejemplo | Estado Naming | Estado PK | Herencia Core |
| :--- | :--- | :--- | :--- | :--- |
| **Nómina** | `Empleado` | Español | INTEGER | No |
| **Activos Fijos** | `ActivoFijo` | Español | INTEGER | No |
| **Inventario** | `Producto` | Español | INTEGER | No |
| **Finanzas** | `CuentaBancaria`| Mixto | UUID | Sí |
| **Operativa** | `Product` | Mixto | UUID | Parcial |
| **Archivística** | `Process` | English | UUID | No |
| **Contabilidad**| `AdminAccount` | English | UUID | Sí |
| **Plan Cuentas** | `AdminChartOfAccounts`| English | INTEGER | No |

---

## 5. RECOMENDACIÓN DE ARQUITECTURA IDEAL Y HOJA DE RUTA

### ARQUITECTURA SUGERIDA: "HOLDING DIGITAL CENTRALIZADA"
- **Standardization Layer (SL):** Implementar una capa que obligue a todos los módulos de `admin_plataforma` a heredar de `core_erp.base_models` y usar UUIDs.
- **Observability Hub:** Crear un microservicio de agregación de eventos para alimentar la Torre de Control sin acoplarse a las bases de datos de los inquilinos.

### HOJA DE RUTA TÉCNICA SUGERIDA
1. **Fase 1 (Sincronización Técnica):** Refactorizar `admin_nomina` y `admin_activos_fijos` a Technical English + UUID.
2. **Fase 2 (Consolidación Comercial):** Unificar los modelos de Planes y Suscripciones bajo el `commercial_engine` y activar el `BillingEngine` para la Holding.
3. **Fase 3 (Visibilidad Estratégica):** Desarrollar la Torre de Control (Dashboard Global) y el Motor de Reportes Financieros Automatizados.

---
**Diagnóstico finalizado por Jules - Ingeniero de Sistemas Superior.**
