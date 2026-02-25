# AUDITORÍA DETALLADA DE DEPENDENCIAS CRUZADAS — FASE 1

## 1. INVENTARIO DE IMPORTS CRUZADOS

### 1.1 ADMIN_PLATAFORMA ➔ MI_NEGOCIO
| Archivo Origen | Componente Importado | Tipo | Severidad |
| :--- | :--- | :--- | :---: |
| `services/quintuple_erp.py` | `OperacionComercial` | Modelo | 🔴 Crítico |
| `services/quintuple_erp.py` | `Reserva` | Modelo | 🔴 Crítico |
| `services/quintuple_erp.py` | `AsientoContable`, `Periodo`| Modelo | 🔴 Crítico |
| `services/quintuple_erp.py` | `OrdenPago` | Modelo | 🔴 Crítico |
| `services/quintuple_erp.py` | `Document`, `Process` | Modelo | 🔴 Crítico |
| `services/interop_bridge.py` | `Reserva` | Modelo | 🔴 Crítico |

### 1.2 MI_NEGOCIO ➔ ADMIN_PLATAFORMA
| Archivo Origen | Componente Importado | Tipo | Severidad |
| :--- | :--- | :--- | :---: |
| `.../agencias/services.py` | `QuintupleERPService` | Servicio | 🔴 Crítico (Ciclo) |
| `.../guias/services.py` | `QuintupleERPService` | Servicio | 🔴 Crítico (Ciclo) |
| `.../bares/services.py` | `QuintupleERPService` | Servicio | 🔴 Crítico (Ciclo) |
| `.../transporte/services.py` | `QuintupleERPService` | Servicio | 🔴 Crítico (Ciclo) |

### 1.3 SARITA_AGENTS ➔ MI_NEGOCIO
| Archivo Origen | Componente Importado | Tipo | Severidad |
| :--- | :--- | :--- | :---: |
| `tasks.py` | `SargentoArchivistico` | Sargento | 🔴 Crítico |
| `tasks.py` | `SargentoOperativo` | Sargento | 🔴 Crítico |
| `tasks.py` | `SargentoComercial` | Sargento | 🔴 Crítico |
| `agents/.../tenientes.py` | `SargentoEspecializado` | Sargento | 🔴 Crítico |
| `commands/seed_...` | `ProcesoOperativo` | Modelo | 🔴 Crítico |
| `.../soldados_fin...py` | `Presupuesto`, `Credito` | Modelo | 🔴 Crítico |

### 1.4 SARITA_AGENTS ➔ ADMIN_PLATAFORMA
| Archivo Origen | Componente Importado | Tipo | Severidad |
| :--- | :--- | :--- | :---: |
| `orchestrator.py` | `GovernancePolicy` | Modelo | 🟡 Medio |
| `agents/interop/tenientes.py`| `InteroperabilityBridge` | Servicio | 🔴 Crítico |

---

## 2. IDENTIFICACIÓN DE CICLOS CRÍTICOS (DEPENDENCIAS CIRCULARES)

### CICLO A: EL BUCLE DEL ERP
`mi_negocio` ➔ `admin_plataforma.QuintupleERPService` ➔ `mi_negocio.models` ➔ `mi_negocio`
*   **Impacto:** Bloquea la migración de modelos y rompe la arquitectura multi-tenant.
*   **Solución:** Reemplazar llamadas directas por eventos en el `EventBus`.

### CICLO B: LA RED DE SARGENTOS
`sarita_agents` ➔ `mi_negocio.sargentos` ➔ `mi_negocio.models`
*   **Impacto:** Los agentes están casados con la implementación de base de datos de los inquilinos.
*   **Solución:** Crear `application_services` como capa de abstracción.

---

## 3. GRAFO REAL DE DEPENDENCIAS (BASELINE F1)

```text
[sarita_agents] ───────(Direct)───────► [mi_negocio]
      │                                     ▲
      │                                     │
      ▼                                     │
[admin_plataforma] ◄────(Circular)────► [mi_negocio]
      │                                     │
      └───────────────► [core_erp] ◄────────┘
```

---
## 4. ESTADO POST-REFACTOR (CIERRE FASE 1)
*   **Ciclos de Módulo:** 0 detectados.
*   **Imports Estáticos mi_negocio:** 0 detectados.
*   **Mecanismo de Comunicación:** EventBus (Core) + Dynamic Dispatch.
*   **Aislamiento de IA:** Logrado vía `application_services`.

**Auditoría finalizada.**
