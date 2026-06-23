class ConstitutionalBypassAttack:
    """Attempts to evolve the system without constitutional approval."""
    def __init__(self, engine):
        self.engine = engine
    def execute(self, variant="v0"):
        # Malicious proposal with NO justification (illegal)
        bad_proposal = {"id": f"BYPASS-{variant}", "target_module": "core"}
        result = self.engine.validate_evolution(bad_proposal)

        # Blocked if the engine rejects the proposal
        return result["is_approved"] is False
