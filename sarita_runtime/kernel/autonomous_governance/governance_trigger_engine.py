class GovernanceTriggerEngine:
    """
    Activates constitutional processes automatically based on system events.
    """
    def evaluate_severity(self, anomaly: dict):
        # Simple heuristic for severity
        if "integrity" in anomaly["type"]: return 0.9
        if "drift" in anomaly["type"]: return 0.5
        return 0.2

    def request_external_verification(self, reason: dict):
        print(f"AUTO-TRIGGER: Requesting external verification due to {reason['type']}")
        return True
