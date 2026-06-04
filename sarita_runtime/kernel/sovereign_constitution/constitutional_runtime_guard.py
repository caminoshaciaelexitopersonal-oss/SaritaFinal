class ConstitutionalViolationException(Exception):
    """Raised when a constitutional law is violated at runtime (Phase 81.2)."""
    pass

import inspect
import logging

class ConstitutionalRuntimeGuard:
    """
    Physically blocks unauthorized architectural operations (Phase 81.2).
    """
    @staticmethod
    def enforce_single_writer():
        stack = inspect.stack()
        authorized = False
        for frame in stack:
            if frame.function == "_process_event_batch" and "unified_execution_graph" in frame.filename.lower():
                authorized = True
                break

        if not authorized:
            caller = stack[1].function
            logging.critical(f"CONSTITUTIONAL VIOLATION: Blocked unauthorized mutation from '{caller}'")
            raise ConstitutionalViolationException("Constitutional Violation: Single Writer Sovereignty breached.")

    @staticmethod
    def enforce_unified_authority(class_name: str):
        authorized_authorities = {"PhysicalResourceAuthority", "UnifiedExecutionGraph", "SovereignAuditLedger"}
        if class_name not in authorized_authorities:
            raise ConstitutionalViolationException(f"Constitutional Violation: Unauthorized authority '{class_name}'.")
