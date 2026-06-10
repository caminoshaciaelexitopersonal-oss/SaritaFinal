class ParadigmDominanceValidator:
    """
    Validates if a paradigm has potential for dominance.
    """
    def validate_dominance(self, paradigm, score):
        return score > 0.7
