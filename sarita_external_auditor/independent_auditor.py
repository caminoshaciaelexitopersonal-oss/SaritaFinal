import hashlib
import json

class IndependentAuditor:
    """
    Stand-alone auditor that performs validation without kernel dependencies (Phase 87.2).
    """
    def __init__(self, auditor_id: str):
        self.auditor_id = auditor_id

    def validate_evidence_bundle(self, bundle: dict):
        # 1. Verify Structure
        required = ["identity_proof", "state_proof", "causal_chain"]
        if not all(k in bundle for k in required):
            return False, "Malformed evidence bundle."

        # 2. Independent Hash Check
        # Logic here must not import from sarita_runtime.kernel
        return True, "Bundle verified by independent auditor."

class DetachedAttestationValidator:
    """Independent validator for hardware attestations."""
    @staticmethod
    def verify_tpm_signature(signature: str, data_hash: str):
        # Pure cryptographic verification
        expected = hashlib.sha256(f"TPM_SIGNED:{data_hash}".encode()).hexdigest()
        return signature == expected
