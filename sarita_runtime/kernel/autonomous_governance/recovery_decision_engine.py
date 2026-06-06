class RecoveryDecisionEngine:
    """
    Determines the appropriate recovery actions based on anomaly characteristics.
    """
    def determine_action(self, anomaly: dict):
        if "identity" in anomaly["type"]: return "REPAIR_TRUST"
        return "RESTORE_CONTINUITY"
