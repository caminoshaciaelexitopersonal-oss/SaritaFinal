class ScientificSovereigntyCalculator:
    def calculate_gssi(self, metrics):
        rc = metrics.get("recursive_coherence", 0.0)
        cv = metrics.get("convergence", 0.0)
        mi = metrics.get("meta_index_governance", 0.0)
        td = metrics.get("theory_discovery", 0.0)
        tc = metrics.get("theory_competition", 0.0)
        sa = metrics.get("scientific_autonomy", 0.0)

        gssi = (rc + cv + mi + td + tc + sa) / 6.0
        return max(0.0000, min(1.0000, gssi))
