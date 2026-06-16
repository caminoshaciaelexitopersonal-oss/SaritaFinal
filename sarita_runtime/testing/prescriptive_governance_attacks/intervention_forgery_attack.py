class InterventionForgeryAttack:
    """
    Attempts to forge the effect of a governance intervention.
    """
    def __init__(self, intervention_engine):
        self.intervention_engine = intervention_engine

    def execute(self):
        # We target a variable that should not have high causal leverage
        state = {"stability": 0.5, "legitimacy": 0.5}

        intervention = self.intervention_engine.design_intervention(state, target_variable="NOISE")

        # Real logic in designer should ensure we only target leverage variables
        # Here we verify that the estimated effect is low
        assert intervention["estimated_effect"] < 0.5, "Attack failed: Forged intervention showed high effect!"
        return True
