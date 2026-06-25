class MetaEvolutionCalculator:
    def calculate_gmei2(self, metrics):
        # Metrics: univ_diversity, law_diversity, ontological_divergence, survival_rate, collective_intel, audit_independence
        u_div = metrics.get("univ_diversity", 0.0)
        l_div = metrics.get("law_diversity", 0.0)
        o_div = metrics.get("ontological_divergence", 0.0)
        survival = metrics.get("survival_rate", 0.0)
        intel = metrics.get("collective_intel", 0.0)
        audit = metrics.get("audit_independence", 0.0)

        # Weighted sum for Global Meta-Evolution Index (GMEI-2)
        gmei2 = (
            (u_div * 0.15) +
            (l_div * 0.20) +
            (o_div * 0.20) +
            (survival * 0.15) +
            (intel * 0.15) +
            (audit * 0.15)
        )
        return round(max(0.0, min(1.0, gmei2)), 4)
