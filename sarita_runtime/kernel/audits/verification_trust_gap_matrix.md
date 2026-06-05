# Verification Trust Gap Matrix (Phase 86.1)

| Verification Domain | Internal Mechanism | External Gap | Impact |
| :--- | :--- | :--- | :--- |
| **Code Identity** | SHA-256 Hash | No external baseline | Root compromise hides tampering |
| **State Transitions** | Event Replay | No continuity proof | Ledger poisoning looks valid |
| **Hardware Trust** | Simulated TPM | No real PCR anchor | Simulation can be spoofed |
| **Authority** | Court Verdict | No cross-validation | Single authority failure |

## Remediation Goal
100% of internal evidence must be reproducible and verifiable by an independent, external process (`ExternalVerifier`).
