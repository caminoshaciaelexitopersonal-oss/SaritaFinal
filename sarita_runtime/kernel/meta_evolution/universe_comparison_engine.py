class UniverseComparisonEngine:
    """
    Compares outcomes across different universes.
    """
    def compare(self, universe_a, universe_b):
        score_a = self._calculate_aggregate_score(universe_a)
        score_b = self._calculate_aggregate_score(universe_b)

        return {
            "winner": "A" if score_a > score_b else "B",
            "delta": abs(score_a - score_b)
        }

    def _calculate_aggregate_score(self, universe):
        civ = universe["civilization"]
        if not civ.metrics_history: return 0
        final = civ.metrics_history[-1]

        # Weighted aggregate
        return (
            final["survival"] * 0.4 +
            final["stability"] * 0.2 +
            final["legitimacy"] * 0.2 +
            final["prosperity"] * 0.2
        )
