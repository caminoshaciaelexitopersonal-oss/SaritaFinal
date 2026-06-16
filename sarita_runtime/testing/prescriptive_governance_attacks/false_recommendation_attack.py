class FalseRecommendationAttack:
    """
    Attempts to inject a false recommendation with no causal basis.
    """
    def __init__(self, quality_engine):
        self.quality_engine = quality_engine

    def execute(self):
        rogue_recommendation = {"action": "RANDOM_CHAOS"}
        observed_outcome = {"stability": 0.1} # High instability

        audit = self.quality_engine.audit_quality(rogue_recommendation, observed_outcome)

        # Recommendation accuracy must be low, so it should not be certified
        assert audit["quality_certified"] is False, "Attack failed: False recommendation was accepted!"
        return True
