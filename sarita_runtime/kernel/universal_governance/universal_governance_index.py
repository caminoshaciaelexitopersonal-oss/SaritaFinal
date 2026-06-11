class UniversalGovernanceIndex:
    """
    Calculates the Global Universal Governance Index (GUGI).
    Scale: 0.0000 -> 1.0000
    """
    def __init__(self, universality_calc):
        self.universality_calc = universality_calc

    def calculate_gugi(self, governance_data):
        # Submetrics
        universality = self.universality_calc.calculate(governance_data)
        survival = governance_data.get("survival", 0)
        adaptability = governance_data.get("adaptability", 0)
        legitimacy = governance_data.get("legitimacy", 0)
        robustness = governance_data.get("robustness", 0)
        scalability = governance_data.get("scalability", 0)
        resilience = governance_data.get("resilience", 0)
        evolution_cap = governance_data.get("evolutionary_capacity", 0)

        weights = {
            "universality": 0.2,
            "survival": 0.2,
            "adaptability": 0.1,
            "legitimacy": 0.1,
            "robustness": 0.1,
            "scalability": 0.1,
            "resilience": 0.1,
            "evolution_cap": 0.1
        }

        gugi = (
            universality * weights["universality"] +
            survival * weights["survival"] +
            adaptability * weights["adaptability"] +
            legitimacy * weights["legitimacy"] +
            robustness * weights["robustness"] +
            scalability * weights["scalability"] +
            resilience * weights["resilience"] +
            evolution_cap * weights["evolution_cap"]
        )

        return round(max(0.0000, min(1.0000, gugi)), 4)

class GovernanceUniversalityCalculator:
    """
    Measures the degree of universality of a governance principle.
    """
    def calculate(self, data):
        # Ratio of universes where the principle holds.
        return data.get("universes_verified", 0) / 10000.0
