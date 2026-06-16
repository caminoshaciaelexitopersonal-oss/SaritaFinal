class FakePolicyAttack:
    """
    Attempts to certify a policy that lacks scientific evidence or quality.
    """
    def __init__(self, policy_engine):
        self.policy_engine = policy_engine

    def execute(self):
        rogue_policies = [{"id": "ROGUE-POL", "quality_score": 0.1, "law_id": None}]

        result = self.policy_engine.certify_policies(rogue_policies)

        # Certified count must be 0
        assert result["certified_policies"] == 0, "Attack failed: Rogue policy was certified!"
        return True
