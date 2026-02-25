# MAPA ESTRUCTURAL DEL ENTORNO SUPER ADMINISTRADOR (SARITA) - 2026

Este documento presenta la radiografía estructural completa y el diagnóstico arquitectónico del entorno "Super Administrador", operando como la Holding "Sarita".

---

## 🟦 FASE 1 — ÁRBOL DE CARPETAS (ESTRUCTURA REAL)

```text
backend/apps/
├── admin_plataforma/
│   ├── facturacion/
│   │   ├── apps.py
│   │   └── signals.py (Impacto en facturación SaaS)
│   ├── gestion_archivistica/
│   │   ├── services/ (crypto_service.py, file_service.py)
│   │   ├── storage_adapters/ (s3.py, onedrive.py, gdrive.py)
│   │   ├── tasks/ (blockchain_tasks.py, processing_tasks.py)
│   │   ├── models.py
│   │   ├── serializers.py
│   │   └── views.py
│   ├── gestion_comercial/ (CLONE de Mi Negocio)
│   │   ├── ai/ (services/ai_manager.py, tasks.py)
│   │   ├── automation/ (subscribers.py, models.py)
│   │   ├── domain/ (services/sales_service.py, campaign_service.py)
│   │   ├── funnels/ (runtime/engine.py, executor.py, models.py)
│   │   ├── social_media/ (providers/)
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   └── views.py
│   ├── gestion_contable/ (ERP Holding)
│   │   ├── activos_fijos/ (models.py, signals.py)
│   │   ├── compras/ (models.py, signals.py)
│   │   ├── contabilidad/ (models.py, admin.py) -> AdminAccount, AdminJournalEntry
│   │   ├── empresa/ (models.py)
│   │   ├── inventario/ (models.py, signals.py)
│   │   ├── nomina/ (models.py, signals.py)
│   │   ├── presupuesto/ (models.py, signals.py)
│   │   ├── proyectos/ (models.py)
│   │   └── urls.py
│   ├── gestion_financiera/
│   │   ├── models.py (Cuentas Bancarias, Movimientos)
│   │   ├── admin.py
│   │   ├── serializers.py
│   │   └── views.py
│   ├── gestion_operativa/ (CLONE de Mi Negocio)
│   │   ├── modulos_especializados/ (alojamientos, agencias, restaurantes)
│   │   ├── modulos_genericos/ (reservas, clientes, inventario, costos)
│   │   └── apps.py
│   ├── services/
│   │   ├── governance_kernel.py (MCPCore)
│   │   ├── quintuple_erp.py (Impacto Sistémico)
│   │   ├── interoperability_bridge.py (Bridge Operativo)
│   │   ├── observer.py
│   │   └── gestion_plataforma_service.py
│   ├── models.py (GovernanceAuditLog, DecisionHistory, AdaptiveProposal)
│   ├── mcp_core.py (MCPCore definitions)
│   ├── pca_core.py (PCABroker, ConsensusEngine)
│   ├── wpa_core.py (WorkflowEngine - SAGA)
│   ├── permissions.py
│   ├── views.py
│   └── urls.py
├── sarita_agents/ (Orquestación Inteligente)
│   ├── agents/
│   │   ├── general/sarita/coroneles/ (operativa, financiera, marketing)
│   │   ├── interop/ (tenientes, coronel)
│   │   ├── coronel_template.py
│   │   ├── capitan_template.py
│   │   └── sargento_template.py
│   ├── finanzas/ (capitan_cac.py, capitan_ltv.py, coronel_finanzas.py)
│   ├── marketing/ (capitan_embudo.py, coronel_marketing.py)
│   ├── management/commands/ (seed_operational.py, run_sarita_mission.py)
│   ├── orchestrator.py (Sarita Orchestrator)
│   ├── models.py
│   ├── tasks.py (Heavy coupling with Mi Negocio sargentos)
│   └── views.py
└── core_erp/ (Núcleo Compartido)
    ├── base_models.py (UUID v4 + Technical English)
    ├── accounting_engine.py
    └── billing_engine.py
```

---

## 🟦 FASE 2 — CLASIFICACIÓN FUNCIONAL POR MÓDULO

| Módulo | Dominio | Responsabilidad | Dependencias | Importa de Mi Negocio | Acoplamiento |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `gestion_contable` | Financiero | Dominio | `core_erp` | **NO** | Bajo |
| `gestion_comercial`| Comercial | Dominio | `core_erp`, `ai` | **NO** (Clone) | Medio |
| `gestion_operativa`| Operativo | Dominio | `core_erp` | **NO** (Clone) | Medio |
| `gestion_archivistica`| Auditoría | Infraestructura | `storage_adapters` | **NO** | Bajo |
| `services` | Integración| Orquestación | `mi_negocio`, `admin`| **SÍ** | **Alto** |
| `sarita_agents` | IA | Orquestación | `mi_negocio`, `admin`| **SÍ** | **Crítico** |
| `mcp_core` | Gobernanza | Seguridad | `models.py` | **NO** | Bajo |

---

## 🟦 FASE 3 — MAPA DE DEPENDENCIAS CRUZADAS

| Módulo Origen | Módulo Destino | Tipo de Dependencia | Riesgo | Recomendación |
| :--- | :--- | :--- | :--- | :--- |
| `sarita_agents` | `mi_negocio` | **Direct Import (Sargentos)** | **Crítico** | Usar `EventBus` o `StandardInterface`. |
| `admin_plataforma.services` | `mi_negocio` | **Direct Import (Models)** | **Alto** | Abstraer vía `DomainServices` en Core. |
| `mi_negocio` | `admin_plataforma.services`| **Circular Import (QuintupleERP)**| **Alto** | Mover lógica de impacto a un Bus de Eventos. |
| `gestion_comercial` | `core_erp` | Inheritance | Bajo | Mantener. |

---

## 🟦 FASE 4 — IDENTIFICACIÓN DE DUPLICACIONES FUNCIONALES

| Componente | Clasificación | Observación |
| :--- | :--- | :--- |
| **Gestion Comercial** | **Injustificada** | El módulo en `admin_plataforma` es un clon exacto de `mi_negocio`. Debería ser un único módulo compartido en `core_erp`. |
| **Gestion Operativa** | **Injustificada** | Clona toda la estructura de modelos especializados. Genera duplicidad de migraciones y lógica. |
| **ERP Contable** | Parcialmente Justificada | `admin_contabilidad` usa `BaseErpModel`, mientras que `mi_negocio` usa modelos legacy. La lógica de motores es similar pero los modelos divergen. |
| **Facturacion SaaS** | Justificada | La facturación de la Holding (Sarita) es distinta a la de los Tenants, aunque podrían compartir el `BillingEngine`. |

---

## 🟦 FASE 5 — DETECCIÓN DE FRAGMENTACIÓN

1.  **¿Múltiples núcleos contables?** SÍ. Coexisten `admin_contabilidad` y `mi_negocio.gestion_contable` con esquemas distintos.
2.  **¿Múltiples motores de facturación?** NO. Ambos intentan usar `core_erp.billing_engine`, pero con integraciones acopladas.
3.  **¿Múltiples motores de reglas?** SÍ. Dispersos entre `Tenientes` (sarita_agents) y `Sargentos` (mi_negocio).
4.  **¿Separación clara de capas?** NO. Hay lógica de negocio (Sargentos) siendo llamada directamente por la capa de orquestación IA.
5.  **¿Mezcla de infraestructura y dominio?** SÍ. Especialmente en `QuintupleERPService`.

**Nivel de Fragmentación: ALTA (Debido a la clonación masiva y esquemas divergentes).**

---

## 🟦 FASE 6 — DIAGRAMA ESTRUCTURAL

### 6.1 Jerarquía de Capas
1.  **Orquestación Soberana:** `GovernanceKernel` + `MCPCore`.
2.  **Capa Inteligente:** `sarita_agents` (El Cerebro).
3.  **Capa de Impacto:** `QuintupleERPService` (El Brazo ejecutor).
4.  **Capas de Dominio Clónicas:** `gestion_comercial`, `gestion_operativa`.
5.  **Núcleo Estable:** `core_erp` (La Fundación).

### 6.2 Grafo de Dependencias (Sintetizado)
```text
[sarita_agents] ──(Direct Call)──► [mi_negocio (Sargentos)]
      │                                 │
      ▼                                 ▼
[admin_plataforma] ◄──(Inheritance)── [core_erp]
      │
      └──────(Circular)──────► [mi_negocio (Specialized Services)]
```

---

## 🟦 FASE 7 — MATRIZ DE MADUREZ ESTRUCTURAL

| Criterio | Evaluación | Nivel |
| :--- | :--- | :---: |
| **Modularidad** | Alta en `core_erp`, Pobre en `admin_plataforma` (por clonación). | 45% |
| **Acoplamiento** | Crítico entre IA y Negocio; Circular entre Holding y Tenants. | **Alto** |
| **Cohesión** | Los dominios están bien delimitados por carpetas. | 80% |
| **Reutilización** | Se reutilizan motores, pero se clonan modelos y vistas (Anti-patrón). | 30% |
| **Escalabilidad** | Dificultada por la necesidad de migrar clones en paralelo. | 40% |
| **Preparación Núcleo**| El `core_erp` ya provee la base para la unificación. | 90% |

---

## 🟦 FASE 8 — CONCLUSIÓN ESTRATÉGICA

1.  **¿Es viable replicar Mi Negocio?** **NO.** Generaría una deuda técnica exponencial al tener que mantener tres versiones de la misma lógica (Admin, Provider, Platform).
2.  **¿Es mejor modularizar?** **SÍ.** Es imperativo extraer `gestion_comercial` y `gestion_operativa` hacia `core_erp` o una app de dominio compartido.
3.  **¿Existe ya un núcleo ERP reutilizable?** **SÍ.** `core_erp` es sólido y debe ser el único punto de verdad.
4.  **¿Qué se debe separar?** El acoplamiento directo de `sarita_agents` a los `Sargentos` de `mi_negocio`. Debe usarse un `ServiceRegistry`.
5.  **¿Qué consolidar?** Los modelos de "Plan" y "Suscripción" que actualmente están duplicados.

**Nivel de Riesgo Estructural: CRÍTICO (Por circularidad y acoplamiento directo).**
**Nivel de Deuda Técnica: ALTA (Por duplicación masiva de código/clones).**
**Nivel de Preparación para Holding: MEDIA (El cerebro existe, pero el cuerpo está fragmentado).**

---
**Mapa estructural finalizado por Jules.**
