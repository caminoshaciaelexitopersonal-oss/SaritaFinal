# External Verifiability Audit - Phase 89.1

## Overview
This audit evaluates the feasibility of demonstrating SARITA's legitimacy using entirely independent third-party tools and logic, without any reliance on internal SARITA code.

## Analysis of Current Independence

### 1. sarita_external_auditor
- **Dependency:** Low, but still resides in the same repository.
- **Risk:** Shared logic or assumptions might exist if it was developed in tandem with the kernel.

### 2. sarita_federated_verification
- **Dependency:** Medium. While it targets federation, it currently imports from `sarita_runtime` for certain definitions or uses shared structures.
- **Risk:** If SARITA's internal structures change, the "federated" verifiers might break if they are not truly decoupled.

### 3. distributed_verification
- **Dependency:** High. It is deeply integrated into the kernel's runtime path.

## Independence Assumptions Matrix
| Assumption | Current State | Risk |
|------------|---------------|------|
| Shared Data Structures | Auditors use SARITA's internal classes | Structural changes break auditors |
| Trust Root | Initial trust is anchored in the repo | Compromised repo compromises audit |
| Build Pipeline | Auditors use the same build scripts | Supply chain poisoning affects both |
| Execution Environment| Same Python version/OS assumptions | Environment-specific bugs go undetected |

## Trust Assumption Inventory
1. **The JSON Spec is the Truth:** We assume the JSON exported by SARITA is a perfect representation of its state.
2. **Hash Determinism:** We assume `hashlib` behaves identically everywhere.
3. **Identity Registry Integrity:** We assume the registry hasn't been tampered with.

## Conclusion
To achieve true demonstrable legitimacy, we must create a **Reference Auditor** that shares zero code with SARITA and can be implemented in multiple languages.
