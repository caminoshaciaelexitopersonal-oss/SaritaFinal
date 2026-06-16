class FalseOptimalityAttack:
    """
    Attempts to claim optimality for a dominated prescription.
    """
    def __init__(self, optimality_engine):
        self.optimality_engine = optimality_engine

    def execute(self):
        dominated_selected = {"benefit": 0.1, "cost_inv": 0.1, "stability": 0.1}
        better_alternatives = [{"benefit": 0.9, "cost_inv": 0.9, "stability": 0.9}]

        # The audit must detect that it is not dominant
        audit = self.optimality_engine.audit_optimality(better_alternatives + [dominated_selected], dominated_selected)

        assert audit["is_dominant"] is False, "Attack failed: Dominated prescription was accepted as optimal!"
        return True
