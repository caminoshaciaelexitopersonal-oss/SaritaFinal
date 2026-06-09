class LegitimacyAdjudicationEngine:
    """
    Adjudicates decisions where existential legitimacy is at stake.
    """
    def adjudicate_legitimacy(self, score: float, is_justified: bool):
        return score > 1.0 and is_justified
