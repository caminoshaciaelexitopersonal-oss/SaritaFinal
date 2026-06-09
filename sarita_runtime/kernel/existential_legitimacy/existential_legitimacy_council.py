class ExistentialLegitimacyCouncil:
    """
    The supreme authority for existential legitimacy.
    """
    def __init__(self, adjudicator, reviewer, resolver):
        self.adjudicator = adjudicator
        self.reviewer = reviewer
        self.resolver = resolver

    def resolve_existential_tension(self, score: float, is_justified: bool, benefit: float, cost: float):
        # 1. Adjudicate
        ok = self.adjudicator.adjudicate_legitimacy(score, is_justified)

        # 2. Review value
        val_ok = self.reviewer.review_value(benefit, cost)

        # 3. Resolve conflict
        priority = self.resolver.resolve_conflict(["SURVIVAL", "IDENTITY", "LEGITIMACY"])

        return {
            "verdict": ok and val_ok,
            "precedence": priority,
            "justification": "Existential Legitimacy Mandate"
        }
