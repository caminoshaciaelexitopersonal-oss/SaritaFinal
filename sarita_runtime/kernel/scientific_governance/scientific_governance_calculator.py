class ScientificGovernanceCalculator:
    def calculate_gsgi(self, metrics):
        sp = metrics.get("strategic_prioritization", 0.0)
        kg = metrics.get("knowledge_governance", 0.0)
        ra = metrics.get("resource_allocation", 0.0)
        fe = metrics.get("frontier_expansion", 0.0)
        sr = metrics.get("scientific_risk", 0.0)
        le = metrics.get("long_term_evolution", 0.0)

        gsgi = (0.20 * sp + 0.20 * kg + 0.15 * ra + 0.15 * fe + 0.15 * sr + 0.15 * le)
        return max(0.0000, min(1.0000, gsgi))
