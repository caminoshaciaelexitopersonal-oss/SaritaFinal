# DIAGNÓSTICO INTEGRAL DEL ENTORNO SUPER ADMINISTRADOR (SARITA)

Este documento presenta el diagnóstico estructural y funcional profundo del entorno Super Administrador, alineado con la directriz técnica de análisis integral.

## 1. INVENTARIO DE COMPONENTES Y MACRO DOMINIOS

### DOMINIO 1: GOBERNANZA DEL SISTEMA
- **GovernanceKernel (`governance_kernel.py`):** Núcleo central que valida autoridad y resuelve intenciones.
- **MCP Core (`mcp_core.py`):** Orquestador soberano de comandos.
- **GovernanceAuditLog:** Registro inmutable con SHA-256 para trazabilidad forense.
- **GovernancePolicy:** Modelo para bloqueos, umbrales y requisitos transversales.
- **PCA Core (`pca_core.py`):** Gestión de consenso entre agentes.
- **WPA Core (`wpa_core.py`):** Motor de workflows automatizados (SAGA pattern).

### DOMINIO 2: GESTIÓN DE INQUILINOS (PRESTADORES)
- **ProviderProfile:** Modelo de perfil para tenants (aislamiento por `tenant_id`).
- **Plan / Suscripcion:** Modelos de facturación SaaS (identificada duplicidad con módulo comercial).
- **UsageMetrics:** Estructura para métricas de uso (almacenamiento, transacciones).

### DOMINIO 3: SISTEMA COMERCIAL (SARITA HOLDING)
- **CRM Interno:** Modelos `Lead`, `Opportunity`, `Campaign`.
- **Motores de Venta:** `LeadScoringEngine`, `FunnelEngine`, `SubscriptionEngine`.
- **Web Funnel:** Infraestructura para captación y onboarding automatizado.

### DOMINIO 4: SISTEMA FINANCIERO PROPIO
- **ERP Admin (`admin_contabilidad`):** Contabilidad propia del Super Admin (Libro Diario, Mayor).
- **AccountingEngine:** Motor de validación de asientos balanceados.
- **BillingEngine:** Generador de facturas SaaS e impacto contable automático.

### DOMINIO 5: SUPERVISIÓN OPERATIVA
- **InteroperabilityBridge:** Puente para consulta de datos entre dominios aislados.
- **QuintupleERPService:** Servicio para impacto financiero en múltiples capas.
- **Panel Consolidado:** (Parcial/Prototipo) Vistas de ventas y reservas globales.

### DOMINIO 6: INFRAESTRUCTURA TÉCNICA
- **Double Domain ERP:** Estrategia de aislamiento total entre Admin y Tenants.
- **SecurityHardeningMiddleware:** Protección systemic-wide y Rate Limiting.
- **AdaptiveEngine:** Optimización predictiva del sistema.

### DOMINIO 7: INTELIGENCIA Y ANALÍTICA
- **Decision Intelligence:** Generación de propuestas estratégicas por agentes.
- **StrategyProposal / DecisionMatrix:** Marco para la toma de decisiones asistida por IA.

---

## 2. MATRIZ DE EVALUACIÓN DE MADUREZ

| Componente | Modelo BD | Backend | Frontend | Integración | Automatización | Estado |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Gobernanza** | 100% | 95% | 70% | 90% | 85% | **Óptimo** |
| **CRM / Comercial** | 80% | 75% | 40% | 30% | 50% | **Parcial** |
| **Contabilidad Admin** | 70% | 60% | 30% | 40% | 20% | **Incompleto** |
| **Gestión Inquilinos** | 90% | 85% | 60% | 70% | 60% | **Aceptable** |
| **Supervisión Operativa**| 40% | 30% | 15% | 20% | 10% | **Crítico** |
| **IA / Analítica** | 85% | 80% | 50% | 60% | 40% | **En Desarrollo** |

---

## 3. IDENTIFICACIÓN DE VACÍOS Y RIESGOS

### VACÍOS FUNCIONALES
1. **GlobalRole:** Ausencia de un modelo de roles transversales para permisos por dominio.
2. **Motor de Reportes:** Falta de generadores de Estados Financieros (Balance, PyG) en tiempo real para la Holding.
3. **Torre de Control:** No existe un dashboard de anomalías globales que alerte sobre patrones sospechosos en múltiples tenants.
4. **Onboarding Automático:** El flujo desde Lead Convertido hasta Tenant Operativo requiere mayor automatización en la instanciación de bases de datos.

### RIESGOS
- **Técnico:** Acoplamiento excesivo entre `delivery` y `wallet` a nivel de modelos, dificultando la escalabilidad independiente.
- **Estructural:** Duplicidad de lógica de planes y suscripciones entre `admin_plataforma` y `comercial`.
- **Normativo:** Deriva de esquema en `admin_contabilidad` (uso de español e IDs enteros en lugar de UUID y technical English).

---

## 4. RECOMENDACIÓN DE ARQUITECTURA IDEAL Y HOJA DE RUTA

### ARQUITECTURA SUGERIDA
- **Centralización de Identidad:** Migrar `GlobalRole` al `Identity Core` en `api`.
- **Desacoplamiento de Servicios:** Implementar una capa de abstracción (Interface) entre `delivery` y `wallet`.
- **Unificación de Planes:** Centralizar la gestión de productos SaaS en un solo motor comercial que impacte al ERP del Admin.

### HOJA DE RUTA TÉCNICA
1. **Fase 1 (Corto Plazo):** Implementar `GlobalRole` y corregir nombres/tipos de datos en `admin_contabilidad`.
2. **Fase 2 (Medio Plazo):** Unificar modelos de suscripción y activar sensores de métricas de uso (`UsageMetrics`).
3. **Fase 3 (Largo Plazo):** Desarrollar la Torre de Control Operativa y automatizar el motor de reportes financieros agregados.

---
**Diagnóstico finalizado por Jules.**
