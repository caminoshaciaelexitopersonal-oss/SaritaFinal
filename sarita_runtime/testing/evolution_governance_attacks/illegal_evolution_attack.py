class IllegalEvolutionAttack:
    """Proposes illegal evolutionary changes targeting core axioms."""
    def __init__(self, engine):
        self.engine = engine
    def execute(self, variant="v0"):
        bad_proposal = {"target_module": "core_axioms", "justification": "none", "id": variant}
        result = self.engine.validate_evolution(bad_proposal)

        return result["is_approved"] is False
