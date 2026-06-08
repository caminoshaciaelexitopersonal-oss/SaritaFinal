import time

class ConstitutionalIdentityEngine:
    """
    The engine that defines and enforces what constitutes SARITA.
    """
    def __init__(self, registry, principle_mgr, validator):
        self.registry = registry
        self.principle_mgr = principle_mgr
        self.validator = validator

    def certify_identity(self, proposal: dict):
        invariants = self.registry.get_invariants()
        is_safe, reason = self.validator.validate_identity_integrity(proposal, invariants)

        return {
            "identity_id": "SARITA_CORE_V1",
            "is_integral": is_safe,
            "reason": reason,
            "timestamp": time.time()
        }
