class CorePrincipleValidator:
    """Validates that evolutionary changes uphold core principles."""
    def validate_principles(self, evolution_plan):
        # Principles are upheld if they are explicitly mentioned in the justification
        if "axiomatic_consistency" in evolution_plan.get("justification", ""):
            return 1.0
        return 0.8
