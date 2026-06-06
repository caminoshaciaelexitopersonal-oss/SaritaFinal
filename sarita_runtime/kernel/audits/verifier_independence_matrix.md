# Verifier Independence Matrix - Phase 90.1

| Verifier | Domain | Language | Authorship | Trust Anchor | Independence Gap |
|----------|--------|----------|------------|--------------|------------------|
| **Core Auditor** | Internal | Python | SARITA Org | Kernel Trust | Low (Self-verifying) |
| **External Auditor**| External | Python | SARITA Org | External Key | Medium (Same Logic) |
| **Federated Node** | Federated| Python | Independent| Domain Key | High (Shared Protocol)|
| **Reference Node** | Independent| Polyglot | Third-Party | Spec-based | Absolute |

## Shared Risk Areas
- **Spec Vulnerability:** A flaw in the SUEP V2 specification would affect ALL verifiers simultaneously.
- **Format Bias:** Over-reliance on JSON might hide issues that a binary-encoded protocol (e.g. Protobuf) would reveal.
