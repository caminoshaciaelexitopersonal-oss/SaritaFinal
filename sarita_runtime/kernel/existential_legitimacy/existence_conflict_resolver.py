class ExistenceConflictResolver:
    """
    Resolves conflicts between survival, identity, and legitimacy.
    """
    def resolve_conflict(self, factors: list):
        # Rule: Legitimacy > Identity > Survival
        if "LEGITIMACY" in factors:
            return "LEGITIMACY_PRIORITY"
        return factors[0]
