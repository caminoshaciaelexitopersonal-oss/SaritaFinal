class ConstitutionalViolationException(Exception):
    """Raised when a constitutional law is violated at runtime (Phase 81.2)."""
    pass

import logging

class ConstitutionalRuntimeGuard:
    """
    Physically blocks unauthorized architectural operations (Phase 81.2/82.4).
    """
    def __init__(self, court=None):
        self.court = court

    def enforce_certified_mutation(self, component_id: str, file_path: str):
        """
        Enforces mutation based on cryptographic identity instead of stack (Phase 82.4).
        """
        if not self.court:
            raise ConstitutionalViolationException("Constitutional Violation: Constitutional Court not found.")

        from sarita_runtime.kernel.constitutional_court.constitutional_court import ConstitutionalCase
        case = ConstitutionalCase(component_id, "MUTATE_STATE", {"file_path": file_path})
        verdict = self.court.judge_case(case)

        if verdict.decision != "APPROVED":
            logging.critical(f"CONSTITUTIONAL VIOLATION: Mutation rejected for '{component_id}': {verdict.justification}")
            raise ConstitutionalViolationException(f"Constitutional Violation: {verdict.justification}")
        return True

    @staticmethod
    def enforce_single_writer():
        # Legacy/Bootstrap check - to be fully replaced by certified mutation
        pass

    @staticmethod
    def enforce_unified_authority(class_name: str):
        authorized_authorities = {"PhysicalResourceAuthority", "UnifiedExecutionGraph", "SovereignAuditLedger"}
        if class_name not in authorized_authorities:
            raise ConstitutionalViolationException(f"Constitutional Violation: Unauthorized authority '{class_name}'.")
