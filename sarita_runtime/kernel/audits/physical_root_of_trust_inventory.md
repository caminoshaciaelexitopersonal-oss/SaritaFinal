# Physical Root of Trust Inventory (Phase 85.1)

| Trust Component | Current Implementation | Physical Requirement |
| :--- | :--- | :--- |
| **Root Secret** | Software String | TPM/HSM Private Key |
| **Identity Registry**| Local Dictionary | Hardware-Signed Registry |
| **State Snapshots** | JSON/SQLite | Measured Boot / PCR |
| **Execution Proof** | SHA-256 Hash | Remote Attestation Token |

## Hardware Capability Targets
1. **TPM 2.0:** For platform measurement and PCR-anchored state.
2. **Secure Enclave:** For isolated execution of the `ConstitutionalCourt`.
3. **HSM:** For high-throughput signing of `TrustLedger` entries.
