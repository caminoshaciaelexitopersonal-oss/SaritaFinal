class ParetoFrontierEngine:
    """
    Identifies the set of non-dominated constitutional solutions.
    """
    def __init__(self, optimizer):
        self.optimizer = optimizer

    def calculate_frontier(self, candidates, objectives):
        return self.optimizer.find_pareto_set(candidates, objectives)
