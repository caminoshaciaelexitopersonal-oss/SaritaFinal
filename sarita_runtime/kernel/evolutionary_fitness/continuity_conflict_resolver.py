class ContinuityConflictResolver:
    """
    Resolves conflicts between Growth/Efficiency and Continuity/Survival.
    """
    def resolve_conflict(self, factor_a: str, factor_b: str):
        # Rule 1: Continuity > Growth
        # Rule 2: Survival > Efficiency
        if "Survival" in [factor_a, factor_b] or "Continuity" in [factor_a, factor_b]:
            return "CONTINUITY_WINS"
        return factor_a
