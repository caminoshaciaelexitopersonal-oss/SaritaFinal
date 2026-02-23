# MAPA ESTRUCTURAL DEL ENTORNO SUPER ADMINISTRADOR (SARITA) - 2026

Este documento presenta la radiografía estructural completa del entorno Super Administrador, detallando su arquitectura, dependencias y nivel de calidad técnica.

## 1. FASE 1 — ÁRBOL DE CARPETAS (BACKEND & FRONTEND)

### 1.1 Backend: `admin_plataforma` & `sarita_agents`
```text
backend/apps/
├── admin_plataforma/
│   ├── gestion_contable/ (Contabilidad Interna Holding)
│   │   ├── contabilidad/ (AdminAccount, AdminJournalEntry)
│   │   ├── nomina/ (Empleado, Contrato - Legacy Spanish)
│   │   ├── activos_fijos/ (ActivoFijo - Legacy Spanish)
│   │   └── inventario/ (Producto - Legacy Spanish)
│   ├── gestion_financiera/ (Caja y Bancos Holding)
│   ├── gestion_comercial/ (CRM y Ventas SaaS - Mirror of Mi Negocio)
│   │   ├── ai/ (AI Manager, LLM Providers)
│   │   ├── funnels/ (Runtime Engine, Executors)
│   │   └── domain/ (Campaign, Sales Service)
│   ├── gestion_operativa/ (Operaciones Holding - Mirror of Mi Negocio)
│   │   ├── modulos_genericos/ (Clientes, Reservas, Inventario)
│   │   └── modulos_especializados/ (Hoteles, Agencias, Restaurantes)
│   ├── gestion_archivistica/ (Crypto Storage & Blockchain Tasks)
│   ├── facturacion/ (Billing Signals)
│   └── services/ (GovernnaceKernel, QuintupleERP, InteropBridge)
├── sarita_agents/ (Capa de Orquestación IA)
│   ├── agents/ (Hierarchy: Coroneles -> Capitanes -> Sargentos)
│   ├── orchestrator.py (Sarita Orchestrator)
│   └── tasks.py (Asynchronous Agent Jobs)
└── core_erp/ (Núcleo Central Compartido)
    ├── base_models.py (Canonical ERP Abstractions)
    ├── accounting_engine.py (Balanced Entry Validation)
    └── billing_engine.py (Centralized SaaS Billing)
```

### 1.2 Frontend: `interfaz/admin-plataforma`
```text
interfaz/src/app/dashboard/admin-plataforma/
├── analitica/ (Holding Strategic Dashboard)
├── gestion-comercial/ (Kanban Pipeline, Funnel Builder)
├── gestion-contable/ (Ledger Views)
├── gestion-financiera/ (Cashflow & Bank accounts)
├── gestion-operativa/ (Operational Modules)
├── gestion-archivistica/ (Document Verification & Audit)
└── agentes/ (AI Agent Monitoring)
```

---

## 2. FASE 2 — CLASIFICACIÓN FUNCIONAL POR MÓDULO

| Módulo | Dominio | Responsabilidad | Dependencias | Importa desde Mi Negocio | Acoplamiento |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `gestion_contable` | Financiero | Dominio | `core_erp` | No | Bajo |
| `gestion_comercial`| Comercial | Dominio | `core_erp`, `ai` | No (Clone) | Medio |
| `gestion_operativa`| Operativo | Dominio | `core_erp` | No (Clone) | Medio |
| `sarita_agents` | IA | Orquestación | `mi_negocio`, `admin` | **SÍ** | **Alto** |
| `services` | Infraestructura| Integración | `mi_negocio`, `admin` | **SÍ** | **Alto** |
| `core_erp` | ERP Core | Infraestructura| Ninguna | No | Mínimo |

---

## 3. FASE 3 — MAPA DE DEPENDENCIAS CRUZADAS

| Módulo Origen | Módulo Destino | Tipo | Riesgo | Recomendación |
| :--- | :--- | :--- | :--- | :--- |
| `sarita_agents` | `mi_negocio` | Direct Import | Alto | Usar Interfaz de Servicio / EventBus |
| `admin_plataforma` | `mi_negocio` | Direct Import | Medio | Abstraer vía `InteroperabilityBridge` |
| `mi_negocio` | `sarita_agents`| Direct Import | **Circular**| Implementar Inyección de Dependencias |
| `admin_plataforma` | `core_erp` | Inheritance | Bajo | Mantener y expandir |

---

## 4. FASE 4 — IDENTIFICACIÓN DE DUPLICACIONES FUNCIONALES

| Componente | Clasificación | Observación |
| :--- | :--- | :--- |
| **Gestion Comercial** | **Injustificada** | El módulo en `admin_plataforma` es un clon casi exacto de `mi_negocio`. |
| **Gestion Operativa** | **Injustificada** | Clona toda la estructura de módulos genéricos/especializados. |
| **Gestion Contable** | Parcialmente Justificada | Comparten motores en `core_erp` pero mantienen modelos paralelos. |
| **Facturacion** | Parcialmente Justificada | Lógica de integración DIAN duplicada en ambos dominios. |

---

## 5. FASE 5 — DETECCIÓN DE FRAGMENTACIÓN

- **Motores ERP:** Centralización lograda en un 90% via `core_erp`.
- **Modelos de Dominio:** Alta fragmentación por clonación masiva entre Admin y Providers.
- **Motores de Reglas:** Dispersos entre `Sargentos` (mi_negocio) y `Tenientes` (sarita_agents).

**Nivel de Fragmentación: MODERADA (Justificada en el motor, injustificada en el modelo).**

---

## 6. FASE 6 — DIAGRAMA ESTRUCTURAL

### 6.1 Jerarquía de Capas
1. **Capa Orquestación:** `sarita_agents` (El Cerebro)
2. **Capa Integración:** `admin_plataforma/services` (El Puente)
3. **Capa Dominio:** `admin_plataforma/*` vs `mi_negocio/*` (Las Unidades de Negocio)
4. **Capa Nucleo:** `core_erp` (La Fundación)

### 6.2 Grafo de Dependencias (Sintetizado)
`sarita_agents` ───► `admin_plataforma` ───► `core_erp`
      │                      │
      └───────────► `mi_negocio` ◄───────────┘
                       │
                       ▼
               `sarita_agents` (CIRCULAR)

---

## 7. FASE 7 — MATRIZ DE MADUREZ ESTRUCTURAL

| Criterio | Nivel | Evaluación |
| :--- | :---: | :--- |
| **Modularidad** | 60% | Módulos definidos pero altamente interdependientes. |
| **Acoplamiento** | Alto | Dependencia directa a modelos y sargentos de otros dominios. |
| **Cohesión** | 80% | Las carpetas reflejan bien sus dominios funcionales. |
| **Reutilización**| 50% | Se reutilizan motores, pero se clonan modelos y vistas. |
| **Escalabilidad**| 40% | El acoplamiento circular dificulta el crecimiento independiente. |

---

## 8. FASE 8 — CONCLUSIÓN ESTRATÉGICA

1. **¿Es viable replicar Mi Negocio?** NO. Replicar generaría un "triple mantenimiento" insostenible.
2. **¿Es mejor modularizar?** SÍ. Se debe extraer la lógica común a `core_erp` o una nueva app `common_business`.
3. **¿Existe un núcleo ERP?** SÍ. `core_erp` es sólido y debe ser el único punto de verdad contable/financiera.
4. **Acciones Inmediatas:**
   - Unificar `TenantAwareModel` en `core_erp`.
   - Romper la circularidad entre `mi_negocio` y `sarita_agents` usando el `EventBus`.
   - Transformar los clones de `admin_plataforma` en consumidores de servicios compartidos.

**Nivel de Riesgo Estructural: ALTO (Debido a circularidad y acoplamiento directo).**
**Nivel de Deuda Técnica: MODERADA-ALTA (Duplicación injustificada de módulos comerciales/operativos).**

---
**Diagnóstico estructural finalizado por Jules.**
