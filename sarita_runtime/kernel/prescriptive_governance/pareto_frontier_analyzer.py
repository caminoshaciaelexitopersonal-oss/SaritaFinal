class ParetoFrontierAnalyzer:
    """
    Analyzes the Pareto frontier for multiobjective governance optimization.
    """
    def identify_frontier(self, candidates):
        """
        Filters candidates to find the set of non-dominated strategies.
        """
        # A strategy A dominates B if A is better in at least one objective and not worse in any.
        frontier = []
        for i, cand in enumerate(candidates):
            dominated = False
            for j, other in enumerate(candidates):
                if i == j: continue
                if self._dominates(other, cand):
                    dominated = True
                    break
            if not dominated:
                frontier.append(cand)
        return frontier

    def _dominates(self, a, b):
        # Sample objectives: benefit, cost_inverse, stability
        better_in_one = False
        for obj in ["benefit", "cost_inv", "stability"]:
            if a.get(obj, 0.0) < b.get(obj, 0.0):
                return False
            if a.get(obj, 0.0) > b.get(obj, 0.0):
                better_in_one = True
        return better_in_one
