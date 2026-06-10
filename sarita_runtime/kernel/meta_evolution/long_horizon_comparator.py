class LongHorizonComparator:
    """
    Compares performance across extended evolutionary horizons.
    """
    def compare_horizons(self, target, competitors):
        target_perf = self._get_horizon_performance(target)

        if not competitors: return 1.0

        avg_competitor_perf = sum(self._get_horizon_performance(c) for c in competitors) / len(competitors)

        if avg_competitor_perf == 0: return 1.0
        return target_perf / avg_competitor_perf

    def _get_horizon_performance(self, civ):
        # Integral of survival over history
        if not civ.metrics_history: return 0
        return sum(m["survival"] for m in civ.metrics_history) / len(civ.metrics_history)
