# Hardware Dependency Matrix (Phase 85.1)

| Subsystem | Hardware Dependency | Mitigation if Unavailable |
| :--- | :--- | :--- |
| **SovereignRoot** | TPM NV Index | Encrypted Software Blob |
| **CourtVerdict** | Secure Enclave | Process Isolation |
| **StateCert** | PCR Register | Persistent Hash Ledger |
| **IdentityVal** | Crypto Processor | Software-based SHA-NI |

## Deployment Strategy
Maintain a software-emulated fallback for non-compliant hardware, but flag it as "DEGRADED SOVEREIGNTY" in certification reports.
