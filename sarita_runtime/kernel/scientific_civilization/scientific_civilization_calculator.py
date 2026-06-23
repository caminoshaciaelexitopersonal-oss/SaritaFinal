class ScientificCivilizationCalculator:
    def calculate_gsci2(self, metrics):
        ks = metrics.get("knowledge_sustainability", 0.0)
        cc = metrics.get("civilization_continuity", 0.0)
        kh = metrics.get("knowledge_heritage", 0.0)
        cr = metrics.get("civilization_resilience", 0.0)
        se = metrics.get("scientific_economy", 0.0)
        tg = metrics.get("temporal_governance", 0.0)

        gsci2 = (ks + cc + kh + cr + se + tg) / 6.0
        return max(0.0000, min(1.0000, gsci2))
