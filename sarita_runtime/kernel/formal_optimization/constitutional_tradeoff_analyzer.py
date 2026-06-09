class ConstitutionalTradeoffAnalyzer:
    """
    Analyzes tradeoffs between competing constitutional pillars.
    """
    def analyze_tradeoffs(self, pareto_set, objectives):
        analysis = []
        for i, sol in enumerate(pareto_set):
            # Calculate how much of objective A we lose to gain objective B
            tradeoffs = {}
            for obj in objectives:
                tradeoffs[obj] = sol.get(obj, 0.0)
            analysis.append({
                "solution_index": i,
                "values": tradeoffs
            })
        return analysis
