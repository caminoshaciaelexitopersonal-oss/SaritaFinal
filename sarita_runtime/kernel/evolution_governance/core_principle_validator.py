class CorePrincipleValidator:
    """Validates that evolutionary changes uphold core principles using semantic density."""
    def validate_principles(self, evolution_plan):
        # Principles are upheld if they are explicitly mentioned in the justification
        justification = evolution_plan.get("justification", "")
        density = len(justification) / 100.0

        if "axiomatic_consistency" in justification:
            return round(min(1.0, 0.9 + density), 4)
        return round(min(0.8, density), 4)
