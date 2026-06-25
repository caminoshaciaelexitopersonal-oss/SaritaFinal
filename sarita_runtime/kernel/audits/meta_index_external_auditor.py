class MetaIndexExternalAuditor:
    def __init__(self, index_provider):
        self.index_provider = index_provider

    def audit_index(self, ecosystem_metrics):
        calculated = self.index_provider.update_index(ecosystem_metrics)
        # External auditor re-calculates using potentially different logic or independent verification
        # For now, it ensures the provider's logic is consistent and not tampered

        # Cross-check logic
        independent_val = self._independent_recalculation(ecosystem_metrics)

        variance = abs(calculated - independent_val)
        is_valid = variance < 0.0001

        return {
            "is_valid": is_valid,
            "variance": variance,
            "certified_index": calculated if is_valid else None
        }

    def _independent_recalculation(self, metrics):
        # Redundant implementation to avoid circular dependency
        diversity = metrics.get("diversity", 0.0)
        speciation = metrics.get("speciation_rate", 0.0)
        resilience = metrics.get("avg_resilience", 0.0)
        innovation = metrics.get("innovation_level", 0.0)
        survival = metrics.get("survival_rate", 0.0)
        adaptation = metrics.get("adaptation_velocity", 0.0)

        gmci = (
            (diversity * 0.20) +
            (speciation * 0.15) +
            (resilience * 0.15) +
            (innovation * 0.20) +
            (survival * 0.15) +
            (adaptation * 0.15)
        )
        return round(max(0.0, min(1.0, gmci)), 4)
