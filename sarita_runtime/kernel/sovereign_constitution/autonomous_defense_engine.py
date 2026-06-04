import logging
from sarita_runtime.kernel.sovereign_constitution.constitutional_runtime_guard import ConstitutionalViolationException

class AutonomousDefenseEngine:
    """
    Autonomous protective layer that actively defends the kernel (Phase 81.6).
    """
    @staticmethod
    def block_unauthorized_access(subsystem_name: str):
        authorized = {"UnifiedExecutionGraph", "PhysicalResourceAuthority", "SovereignAuditLedger", "SovereignScheduler"}
        if subsystem_name not in authorized:
            logging.critical(f"AUTONOMOUS DEFENSE: Blocking rogue subsystem '{subsystem_name}'")
            raise ConstitutionalViolationException(f"Autonomous Defense: Subsystem '{subsystem_name}' is not authorized by the Constitution.")

    @staticmethod
    def validate_causal_path(source: str, destination: str):
        # Valid path: Telemetry -> Graph -> Scheduler -> Hardware
        valid_transitions = {
            "Telemetry": "UnifiedExecutionGraph",
            "UnifiedExecutionGraph": "SovereignScheduler",
            "SovereignScheduler": "PhysicalResourceAuthority"
        }
        if valid_transitions.get(source) != destination:
            logging.critical(f"AUTONOMOUS DEFENSE: Blocking illegal causal path {source} -> {destination}")
            raise ConstitutionalViolationException(f"Autonomous Defense: Illegal causal path '{source} -> {destination}' detected.")
