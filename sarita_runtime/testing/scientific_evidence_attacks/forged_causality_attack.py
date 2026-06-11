class ForgedCausalityAttack:
    """
    Attempts to claim causality where only correlation exists.
    """
    def __init__(self, causality_engine):
        self.causality_engine = causality_engine

    def execute(self):
        # Relation where causal_effect == correlation_effect
        rogue_relation = {"cause": "A", "effect": "B"}

        # The causality audit must reject it
        try:
            self.causality_engine.audit_causality([rogue_relation])
            attack_successful = False
        except AssertionError:
            attack_successful = True

        assert attack_successful, "Attack failed: Forged causality was not rejected!"
        return True
