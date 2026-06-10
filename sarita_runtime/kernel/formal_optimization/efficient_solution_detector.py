class EfficientSolutionDetector:
    """
    Detects if a given solution is on the Pareto frontier.
    """
    def is_efficient(self, solution, all_solutions, objectives):
        for other in all_solutions:
            # If any other solution dominates this one, it's not efficient
            better_in_all = all(other.get(obj, 0) >= solution.get(obj, 0) for obj in objectives)
            strictly_better_in_one = any(other.get(obj, 0) > solution.get(obj, 0) for obj in objectives)
            if better_in_all and strictly_better_in_one:
                return False
        return True
