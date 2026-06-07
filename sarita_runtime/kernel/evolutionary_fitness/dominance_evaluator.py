class DominanceEvaluator:
    """
    Evaluates if a specific trajectory "dominates" the current evolutionary state.
    """
    def evaluate_dominance(self, candidate_fitness: float, current_fitness: float):
        # A trajectory dominates if it provides a significant fitness increase (>10%)
        return candidate_fitness > (current_fitness * 1.1)
