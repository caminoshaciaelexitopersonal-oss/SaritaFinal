# Operational Independence Audit (Phase 87.1)

## 1. Dependency Analysis
The current `ExternalVerifier` and `IndependentAttestationValidator` (Phase 86) are defined within the `sarita_runtime` package. While logically separate, they still share the same codebase and Python environment as the kernel.

## 2. Identified Verifier Gaps
* **Internal Module Imports:** External verifiers currently import from `sarita_runtime.kernel`, creating a compile-time and runtime dependency on the system they are auditing.
* **Lack of Consensus:** Validation is currently performed by a single external engine. There is no mechanism to require consensus among multiple, distinct auditors.
* **Code Access Requirement:** Auditing currently requires access to the kernel's source code to perform hash measurements and state comparisons.
* **Proprietary Evidence Format:** Evidence is stored in the `SovereignAuditLedger` (SQLite), which requires specific kernel knowledge to parse and reconstruct.

## 3. Findings
* **`external_verifier.py`:** Depends on `sarita_runtime/kernel/drift_detection` logic.
* **`state_continuity_engine.py`:** Integrated into the kernel's directory structure, making it difficult to package as a standalone audit tool.

## 4. Conclusion
To achieve Absolute Independence, the audit infrastructure must be detached into a standalone package (`sarita_external_auditor`) that interacts with the kernel only via standardized evidence export protocols.
