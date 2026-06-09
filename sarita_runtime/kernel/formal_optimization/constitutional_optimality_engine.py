class ConstitutionalOptimalityEngine:
    """
    Orchestrates the search for mathematically optimal decisions.
    """
    def __init__(self, optimizer, score_calculator):
        self.optimizer = optimizer
        self.score_calculator = score_calculator

    def find_optimal_decision(self, alternatives):
        """
        Evaluates a set of alternative decisions and returns the optimal one.
        """
        if not alternatives:
            return None

        scored_alternatives = []
        for alt in alternatives:
            score = self.score_calculator.calculate_gcoi(alt)
            scored_alternatives.append((alt, score))

        # Find the alternative with the highest GCOI
        optimal_alt, max_score = max(scored_alternatives, key=lambda x: x[1])

        return {
            "optimal_decision": optimal_alt,
            "gcoi": max_score,
            "alternatives_evaluated": len(alternatives)
        }
