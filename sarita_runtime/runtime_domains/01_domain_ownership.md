# DOMAIN OWNERSHIP Y BOUNDED CONTEXTS (RUNTIME)
**Objetivo:** Definir límites claros de responsabilidad y ejecución.

## 1. MATRIZ DE DOMINIOS
| Dominio | Ownership | Responsabilidad | Eventos Emitidos |
|---------|-----------|-----------------|------------------|
| **Governance** | Sovereign Kernel | Políticas, RLS, Auditoría | `policy.violated`, `tenant.frozen` |
| **Finance** | Meta-Financial Brain | Ledger, Pagos, Tax | `payment.settled`, `ledger.updated` |
| **Tourism** | Operational Engine | Reservas, Inventario | `booking.created`, `slot.reserved` |
| **AI** | War Room SCTA | Inferencia, Razonamiento | `decision.made`, `agent.failed` |
| **Telemetry** | Observability Matrix | Métricas, Tracing, Logs | `anomaly.detected`, `sla.breached` |

## 2. ANTI-CORRUPTION LAYERS (ACL)
Cada dominio runtime interactúa mediante un ACL que valida:
- **Esquema:** Cumplimiento de JSONSchema.
- **Autoridad:** El productor del evento tiene permiso jerárquico.
- **Trazabilidad:** Presencia obligatoria de `trace_id`.

## 3. DEPENDENCIAS PERMITIDAS
- Los dominios solo pueden hablar entre sí mediante el **Event Bus**.
- Prohibidas las llamadas directas entre workers de diferentes dominios (Shared Nothing Architecture).
