class EvolutionarySelectionEngine:
    """
    The engine that automatically selects trajectories to maximize survival.
    """
    def __init__(self, manager, evaluator, validator):
        self.manager = manager
        self.evaluator = evaluator
        self.validator = validator

    def perform_selection(self, current_fitness: float, current_p_s: float, candidates: list):
        best = self.manager.select_best_trajectory(candidates)
        if not best:
            return None

        dominates = self.evaluator.evaluate_dominance(best["fitness"], current_fitness)
        is_valid = self.validator.validate_selection(best["p_s"], current_p_s)

        if is_valid and (dominates or best["p_s"] > current_p_s):
            return best
        return None # Stick with current trajectory
