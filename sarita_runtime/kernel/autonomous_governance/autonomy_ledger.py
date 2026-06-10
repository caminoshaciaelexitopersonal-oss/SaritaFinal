import time

class AutonomyLedger:
    """
    Unified record of all autonomous decisions and actions.
    """
    def __init__(self):
        self.actions = []

    def log_action(self, component: str, action: str, data: dict):
        self.actions.append({
            "timestamp": time.time(),
            "component": component,
            "action": action,
            "data": data
        })

class GovernanceActionLedger(AutonomyLedger):
    """Specific ledger for autonomous governance actions."""
    def log_governance_event(self, action: str, metadata: dict):
        self.log_action("GOVERNANCE", action, metadata)

class RecoveryHistoryLedger(AutonomyLedger):
    """Specific ledger for autonomous recovery events."""
    def log_recovery_event(self, anomaly_id: str, success: bool):
        self.log_action("RECOVERY", "EXECUTE_RECOVERY", {"anomaly": anomaly_id, "success": success})

class SelfAuditLedger(AutonomyLedger):
    """Specific ledger for autonomous audit results."""
    def log_audit_event(self, audit_type: str, findings: list):
        self.log_action("AUDIT", audit_type, {"findings": findings})
