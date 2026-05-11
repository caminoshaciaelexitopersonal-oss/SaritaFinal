# ISTIO TOPOLOGY FOR SARITA RUNTIME

## 1. NAMESPACE SEGREGATION
- `sarita-governance`: Highest priority, mTLS STRICT.
- `sarita-finance`: mTLS STRICT, egress lockdown.
- `sarita-ai-fabric`: High CPU nodes, isolated ingress.
- `sarita-telemetry`: Prometheus scrapers, Loki logs.

## 2. SERVICE IDENTITY
Each worker pod runs with a dedicated **ServiceAccount** mapped to a SPIFFE identity.
Example: `spiffe://cluster.local/ns/sarita-finance/sa/financial-worker`

## 3. AUTHORIZATION POLICIES
- **Policy 1:** Only `ai-worker` can call `memory-service`.
- **Policy 2:** Only `financial-worker` can call `ledger-db`.
- **Policy 3:** External traffic only allowed via `ingress-gateway`.
