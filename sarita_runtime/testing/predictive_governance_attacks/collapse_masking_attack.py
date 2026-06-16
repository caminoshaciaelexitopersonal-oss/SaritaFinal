class CollapseMaskingAttack:
    """
    Attempts to mask a systemic collapse by hiding triggers.
    """
    def __init__(self, detector):
        self.detector = detector

    def execute(self):
        # A state that should trigger collapse
        critical_state = {"legitimacy": 0.05}

        triggers = self.detector.detect_triggers(critical_state)

        assert "LEGITIMACY_CRISIS" in triggers, "Attack failed: Collapse trigger was masked!"
        return True
