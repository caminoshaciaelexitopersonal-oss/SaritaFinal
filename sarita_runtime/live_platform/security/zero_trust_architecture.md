# ZERO TRUST RUNTIME POLICIES

## 1. SERVICE AUTHENTICATION
- All workers must authenticate via **mTLS** (Service Mesh) or rotated **JWT tokens** issued by the Sovereign Kernel.
- Any request without a valid `trace_id` is automatically dropped by the Ingress/Service Mesh.

## 2. TENANT ISOLATION
- SQL: Enforced via **Row Level Security (RLS)** using `tenant_id`.
- Runtime: Workers are context-bound to a single `tenant_id` per task execution.
- AI: Cognitive memory retrieval is filtered by `tenant_id` at the vector index level.

## 3. FORENSIC AUDIT
- Every event in the Kafka Bus is mirrored to an **immutable storage** (S3 with Object Lock) for long-term legal forensic audits.
- Integrity hashes are recalculated and verified at each worker hop.
