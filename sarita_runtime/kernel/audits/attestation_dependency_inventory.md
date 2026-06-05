# Attestation Dependency Inventory (Phase 86.1)

| Attestant | Target | Current Dependency | Risk |
| :--- | :--- | :--- | :--- |
| **Runtime Engine** | Kernel Binary | `SovereignIdentityEngine` | Circular (Internal) |
| **State Guard** | Ledger / Graph | `ConstitutionalCourt` | Shared logic |
| **Trust Chain** | Root Certificate | `TrustAnchor` | Hardcoded string |

## Target State
Attestation must be anchored in a **Dual Trust Chain** where two independent authorities must sign off on any structural or identity change.
