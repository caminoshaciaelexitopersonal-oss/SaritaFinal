class PolicySpoofingAttack:
    """
    Attempts to claim high resilience for a weak policy.
    """
    def __init__(self, policy_validator):
        self.policy_validator = policy_validator

    def execute(self):
        rogue_policy = {"id": "ROGUE-P1", "resilience": 0.1}

        is_valid = self.policy_validator.validate_resilience(rogue_policy)

        assert is_valid is False, "Attack failed: Weak policy was certified as resilient!"
        return True
