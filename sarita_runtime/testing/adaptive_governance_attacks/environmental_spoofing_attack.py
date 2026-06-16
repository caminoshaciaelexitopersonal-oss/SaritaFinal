class EnvironmentalSpoofingAttack:
    """
    Attempts to spoof environmental data to trigger incorrect adaptations.
    """
    def __init__(self, change_engine):
        self.change_engine = change_engine

    def execute(self):
        rogue_context = {"cultural_shift": 1.0} # Extreme spoof

        # The engine must detect and record the shift correctly
        detection = self.change_engine.detect_environment_shifts(rogue_context, {})

        assert detection["shift_detected"] is True, "Attack failed: Environmental spoofing not detected!"
        return True
