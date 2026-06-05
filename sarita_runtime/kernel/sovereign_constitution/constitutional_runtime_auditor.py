import logging
from sarita_runtime.kernel.sovereign_constitution.immutable_architecture_registry import ImmutableArchitectureRegistry

class ConstitutionalRuntimeAuditor:
    """
    Continuously audits the running system for topological drift (Phase 81.5).
    """
    @staticmethod
    def perform_runtime_audit():
        is_stable, drift = ImmutableArchitectureRegistry.verify_integrity()
        if not is_stable:
            logging.critical(f"CONSTITUTIONAL DRIFT DETECTED: {drift}")
            return False, drift
        return True, "Topology matches constitutional baseline."

if __name__ == "__main__":
    import sys
    success, msg = ConstitutionalRuntimeAuditor.perform_runtime_audit()
    print(msg)
    if not success: sys.exit(1)
