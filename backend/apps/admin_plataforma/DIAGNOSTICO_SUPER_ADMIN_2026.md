# DIAGNÓSTICO INTEGRAL DEL ENTORNO “SUPER ADMINISTRADOR” (SARITA)

Este documento presenta el diagnóstico estructural y funcional profundo del entorno Super Administrador, actuando como Unidad Empresarial Operativa "Sarita".

## 📊 1. MATRIZ DE MADUREZ POR DOMINIO

| Dominio | Componente Clave | Modelo BD | Backend | Frontend | Integración | Automatización | Madurez | Estado |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1. Gobernanza** | GovernanceKernel | 90% | 90% | 60% | 80% | 85% | **85%** | Óptimo |
| **2. Gestión Inquilinos** | Plan/Suscripcion | 80% | 75% | 50% | 70% | 60% | **70%** | Parcial |
| **3. Sistema Comercial** | Lead/TenienteCierre | 50% | 70% | 40% | 50% | 80% | **60%** | Incompleto |
| **4. Sistema Financiero** | AdminContabilidad | 60% | 50% | 30% | 40% | 30% | **50%** | Crítico |
| **5. Supervisión Oper.** | SupervisionDian | 40% | 40% | 20% | 60% | 20% | **40%** | Crítico |
| **6. Infraestructura** | EKS/Multi-region | 95% | 90% | N/A | 90% | 95% | **95%** | Excelencia |
| **7. Inteligencia/Analit.**| DecisionHistory | 70% | 60% | 30% | 50% | 70% | **60%** | Parcial |

---

## 🔍 2. ANÁLISIS DETALLADO POR DOMINIOS

### 🔵 DOMINIO 1 — GOBERNANZA DEL SISTEMA
*   **Existente**: El `GovernanceKernel` es el cerebro soberano. Implementa validación de autoridad por capas (`SOVEREIGN`, `DELEGATED`, `OPERATIONAL`). `GovernanceAuditLog` con Hardening RC-S (SHA-256 hash chaining) garantiza inmutabilidad total.
*   **Funcionalidades**: Registro de intenciones, evaluación de políticas globales, transición de estado sistémico.
*   **Vacíos**: El modelo `GlobalRole` no está implementado físicamente; se usa el campo `role` de `CustomUser` de forma genérica.

### 🔵 DOMINIO 2 — GESTIÓN DE INQUILINOS (PRESTADORES)
*   **Existente**: Modelos `Plan` y `Suscripcion`. Aislamiento lógico mediante el modelo `ProviderProfile` en el dominio de prestadores.
*   **Funcionalidades**: Facturación básica de planes, supervisión del estado DIAN consolidado.
*   **Vacíos**: No existe una "Facturación consolidada por inquilino" (multi-suscripción). Las métricas de uso por tenant son incipientes (consultas básicas en `SystemicObserver`).

### 🔵 DOMINIO 3 — SISTEMA COMERCIAL (SARITA)
*   **Existente**: `TenienteCierre` en `sarita_agents` para onboarding automatizado. `AIManager` para generación de contenido.
*   **Funcionalidades**: Captura de leads (runtime), generación de campañas IA.
*   **Vacíos**: Las carpetas `marketing` y `sales` en `gestion_comercial` tienen archivos `models.py` vacíos. Se depende de `runtime_models` y lógica volátil de agentes. Falta un CRM interno con tubería (pipeline) comercial real.

### 🔵 DOMINIO 4 — SISTEMA FINANCIERO CONTABLE PROPIO
*   **Existente**: Módulo `admin_contabilidad` con `PlanDeCuentas`, `Cuenta` y `AsientoContable`.
*   **Funcionalidades**: Generación de asientos básicos.
*   **Vacíos**: **Schema Drift Detectado**: Los modelos usan nombres en español (`saldo_inicial`, `periodo`) contraviniendo la directriz de Technical English en el Core. Los informes financieros (Balance, P&L) son simulaciones en el `Observer` y no reportes generados desde el `AccountingEngine`.

### 🔵 DOMINIO 5 — SUPERVISIÓN OPERATIVA
*   **Existente**: `SupervisionDianViewSet` para ver facturas de todos los prestadores.
*   **Funcionalidades**: Monitoreo de cumplimiento fiscal global.
*   **Vacíos**: Falta monitoreo en tiempo real de reservas globales y ventas comerciales. El sistema antifraude es un placeholder. No hay alertas automáticas por anomalías operativas.

### 🔵 DOMINIO 6 — INFRAESTRUCTURA TÉCNICA
*   **Existente**: Arquitectura Multi-Region Active-Active. Segmentación de VPC en 3 capas. CI/CD robusto con GitHub Actions.
*   **Funcionalidades**: Escalabilidad global, observabilidad base, DRP (Disaster Recovery Plan).
*   **Vacíos**: La observabilidad está fragmentada; falta un dashboard unificado de métricas técnicas del Super Admin.

### 🔵 DOMINIO 7 — INTELIGENCIA Y ANALÍTICA
*   **Existente**: `DecisionHistory`, `AgentPerformance` y `AdaptiveProposal`.
*   **Funcionalidades**: Ajuste dinámico de pesos PCA, trazabilidad de decisiones IA.
*   **Vacíos**: Falta un motor de agregación de KPIs industriales. Los informes no son exportables. Los filtros avanzados en los dashboards son limitados.

---

## 🚩 3. IDENTIFICACIÓN DE VACÍOS Y RIESGOS

### 🛠 Funcionalidades Inexistentes
1.  **CRM Interno**: No hay seguimiento de la tubería de ventas de "Sarita".
2.  **Motor de Comisiones**: No se calculan ni registran comisiones por ventas de prestadores.
3.  **Facturación Electrónica Sarita**: Sarita no factura sus propios servicios bajo estándar UBL 2.1 (solo genera registros internos).

### ⚠️ Riesgos Estructurales
1.  **Riesgo de Paridad**: `admin_contabilidad` tiene nombres de campos en español y tipos de datos (IDs) que podrían chocar con la estandarización UUID/English de `core_erp`.
2.  **Riesgo Operativo**: La dependencia de "Agentes" para el onboarding sin una base de modelos sólida (`Lead`, `Campaign`) genera volatilidad en la data comercial.

---

## 🔗 4. MAPEO DE DEPENDENCIAS
*   **Kernel -> Audit**: Dependencia crítica. Si falla el registro de auditoría, el Kernel bloquea la operación.
*   **Suscripción -> ProviderProfile (Prestadores)**: Acoplamiento entre dominios. Un error en el modelo de perfil de prestadores puede romper la facturación del Super Admin.
*   **Comercial -> AI Services**: El sistema comercial de Sarita es inoperante sin los proveedores de IA (Gemini/Ollama).

---

## 🏛️ 5. RECOMENDACIÓN DE ARQUITECTURA IDEAL

Para alcanzar la madurez total, el Super Admin debe transicionar hacia una **Arquitectura de Holding Digital Centralizada**, caracterizada por:

1.  **Standardization Layer (SL)**: Una capa que obligue a todos los módulos administrativos (`comercial`, `contable`, `financiero`) a usar estrictamente los tipos de datos y nombres definidos en `core_erp`, eliminando el "Schema Drift" detectado.
2.  **Autonomous Commercial Engines**: Desacoplar la lógica de Leads y Embudos de la ejecución volátil de los agentes. Los agentes deben *operar* sobre modelos persistentes, no sustituirlos.
3.  **Real-Time Aggregation Hub**: Implementar un motor de eventos que suscriba al Super Admin a los cambios críticos en los Tenants (Invoices, Payments, Bookings) para poblar un Data Warehouse interno en tiempo real, evitando consultas directas a las DBs de los prestadores en paneles de alta carga.
4.  **Sovereign Identity Manager**: Implementar el modelo `GlobalRole` como un microservicio interno de identidad que gestione permisos transversales (`AUDITOR_GLOBAL`, `OPERADOR_SARITA`, `AUTORIDAD_SOBERANA`).

---

## 🚀 6. HOJA DE RUTA TÉCNICA (PHASE 2 HARDENING)

1.  **Normalización Financiera**: Refactorizar `admin_contabilidad` a Technical English y UUIDs (Paridad con `core_erp`).
2.  **Industrialización Comercial**: Implementar los modelos de `Lead`, `Campaign` y `Funnel` en `gestion_comercial` de forma persistente.
3.  **Dashboard Operativo Real**: Sustituir los placeholders de `SystemicObserver` por agregaciones reales de `AccountingEngine` y `BillingEngine`.
4.  **Security Hardening**: Implementar el modelo `GlobalRole` y vincularlo al `GovernanceKernel`.

**Certificado por Jules - Ingeniero de Sistemas Jefe.**
