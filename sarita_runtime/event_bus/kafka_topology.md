# TOPOLOGÍA KAFKA: SARITA SOBERANA

## CLUSTER CONFIGURATION
- **Replication Factor:** 3 (Garantía de alta disponibilidad).
- **Min Insync Replicas:** 2 (Consistencia garantizada).
- **Retention Policy:** 7 días (Compactación activada para topics de estado).

## TOPICS & PARTITIONS
| Topic Name | Partitions | Retention | Compacted |
|------------|------------|-----------|-----------|
| `finance.ledger` | 12 | 10y (Legal) | No |
| `ai.memory.stream` | 24 | 24h | No |
| `core.tenants.state` | 3 | Forever | Yes |
| `infra.telemetry` | 48 | 6h | No |

## CONSUMER GROUPS
- `finance-auditor-group`: Procesa transacciones para validación forense.
- `ai-orchestrator-group`: Reacciona a eventos de agentes para coordinar la jerarquía.
- `telemetry-aggregator-group`: Alimenta Grafana y Prometheus.
