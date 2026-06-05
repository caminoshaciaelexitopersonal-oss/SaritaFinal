# Verifier Dependency Inventory (Phase 87.1)

| Verifier Component | Internal Dependency | Risk | target (Phase 87) |
| :--- | :--- | :--- | :--- |
| **ExternalVerifier** | `drift_detection` | Shared Logic | Detached logic |
| **AttestationValidator**| `hardware_trust` | Shared Adapters | Port-based measurement |
| **StateValidator** | `runtime_graph` | Shared Vertex Logic| JSON-only rebuilder |
| **TrustValidator** | `sovereign_trust` | Shared Certificates| Schema-based validation|

## Detachment Plan
1. Move all validation logic to `sarita_external_auditor/`.
2. Prohibit any `import sarita_runtime` within the detached package.
3. Use a standardized `Sovereign Evidence Bundle` for all verification inputs.
