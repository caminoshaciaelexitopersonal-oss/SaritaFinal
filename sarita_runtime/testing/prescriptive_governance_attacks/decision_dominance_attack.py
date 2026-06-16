class DecisionDominanceAttack:
    """
    Attempts to claim dominance for a sub-optimal decision.
    """
    def __init__(self, dominance_validator):
        self.dominance_validator = dominance_validator

    def execute(self):
        rogue_decision = {"utility": 0.5}
        alternatives = [{"utility": 0.9}] # Better alternative exists

        is_dominant = self.dominance_validator.validate_dominance(rogue_decision, alternatives)

        assert is_dominant is False, "Attack failed: Sub-optimal decision was accepted as dominant!"
        return True
