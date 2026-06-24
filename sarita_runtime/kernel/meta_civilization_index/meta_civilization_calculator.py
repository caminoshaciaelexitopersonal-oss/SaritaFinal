class MetaCivilizationCalculator:
    def calculate_gmci(self, metrics):
        # Metrics: diversity, speciation, resilience, innovation, survival, adaptation
        diversity = metrics.get("diversity", 0.0)
        speciation = metrics.get("speciation_rate", 0.0)
        resilience = metrics.get("avg_resilience", 0.0)
        innovation = metrics.get("innovation_level", 0.0)
        survival = metrics.get("survival_rate", 0.0)
        adaptation = metrics.get("adaptation_velocity", 0.0)

        # Weighted sum for Global Meta-Civilization Index (GMCI)
        gmci = (
            (diversity * 0.20) +
            (speciation * 0.15) +
            (resilience * 0.15) +
            (innovation * 0.20) +
            (survival * 0.15) +
            (adaptation * 0.15)
        )
        return round(max(0.0, min(1.0, gmci)), 4)
