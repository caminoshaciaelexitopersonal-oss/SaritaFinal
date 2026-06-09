class MultiObjectiveOptimizer:
    """
    Handles optimization across multiple competing constitutional objectives.
    """
    def optimize(self, candidates, objectives):
        """
        Given a set of candidates and objective weights, returns the best candidate.
        """
        results = []
        for candidate in candidates:
            total_score = 0
            for obj, weight in objectives.items():
                val = candidate.get(obj, 0.0)
                total_score += val * weight
            results.append((candidate, total_score))

        return max(results, key=lambda x: x[1])[0]

    def find_pareto_set(self, candidates, objectives):
        """
        Finds the set of non-dominated solutions.
        """
        pareto_set = []
        for c1 in candidates:
            is_dominated = False
            for c2 in candidates:
                if c1 == c2:
                    continue
                # c2 dominates c1 if it is better in all objectives
                if all(c2.get(obj, 0) >= c1.get(obj, 0) for obj in objectives) and \
                   any(c2.get(obj, 0) > c1.get(obj, 0) for obj in objectives):
                    is_dominated = True
                    break
            if not is_dominated:
                pareto_set.append(c1)
        return pareto_set
