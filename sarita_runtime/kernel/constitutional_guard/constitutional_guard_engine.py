import inspect
import logging

class SingleWriterGuard:
    """
    Enforces that only the authorized thread can modify the Graph state (Phase 80.2).
    """
    @staticmethod
    def validate_caller():
        stack = inspect.stack()
        # Find if the caller is inside UnifiedExecutionGraph._process_event_batch
        authorized = False
        for frame in stack:
            if frame.function == "_process_event_batch":
                authorized = True
                break

        if not authorized:
            caller = stack[1].function
            logging.error(f"CONSTITUTIONAL VIOLATION: Unauthorized state mutation attempt from '{caller}'")
            raise PermissionError("Sovereign Violation: Direct state mutation prohibited outside the Single Writer context.")
        return True

class AuthorityGuard:
    """
    Ensures authority remains unified (Phase 80.2).
    """
    AUTHORIZED_AUTHORITIES = {"PhysicalResourceAuthority", "UnifiedExecutionGraph"}

    @staticmethod
    def check_authority_registration(class_name: str):
        if class_name not in AuthorityGuard.AUTHORIZED_AUTHORITIES:
            raise PermissionError(f"Constitutional Violation: '{class_name}' is not an authorized sovereign authority.")
        return True
