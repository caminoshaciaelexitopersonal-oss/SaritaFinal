class CrossUniverseValidator:
    def validate_metrics(self, metrics, universe_group_a, universe_group_b):
        # Metrics are validated by two independent groups of universes
        # Logic: groups must reach similar conclusions
        conclusion_a = self._get_conclusion(metrics, universe_group_a)
        conclusion_b = self._get_conclusion(metrics, universe_group_b)

        return conclusion_a == conclusion_b

    def _get_conclusion(self, metrics, universes):
        # Weighted conclusion based on universe epistemic stability
        weight = sum(u["laws"].get("epistemic_stability", 0.5) for u in universes) / len(universes)
        return metrics * weight > 0.4
