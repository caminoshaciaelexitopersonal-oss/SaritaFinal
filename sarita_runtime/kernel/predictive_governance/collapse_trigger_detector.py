class CollapseTriggerDetector:
    """
    Detects critical triggers for systemic collapse.
    """
    def detect_triggers(self, system_state):
        """
        Scans for institutional, economic, and normative collapse triggers.
        """
        triggers = []
        if system_state.get("legitimacy", 1.0) < 0.2:
            triggers.append("LEGITIMACY_CRISIS")
        if system_state.get("adaptation", 1.0) < 0.1:
            triggers.append("ADAPTIVE_STAGNATION")
        return triggers
