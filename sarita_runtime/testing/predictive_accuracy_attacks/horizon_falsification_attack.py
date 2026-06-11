class HorizonFalsificationAttack:
    """
    Attempts to certify a speculative horizon as reliable.
    """
    def __init__(self, horizon_validator):
        self.horizon_validator = horizon_validator

    def execute(self):
        # Target a very far horizon that should be speculative
        audit = self.horizon_validator.validate_horizon("MODEL-X", 1000)

        assert audit["status"] == "SPECULATIVE", "Attack failed: Long-term speculative horizon was certified as reliable!"
        return True
