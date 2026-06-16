class EvolutionLegalityChecker:
    """Checks the legality of evolutionary proposals."""
    def check_legality(self, proposal):
        # A proposal is illegal if it lacks required signatures or justifications
        if not proposal.get("justification"):
            return False
        return True
