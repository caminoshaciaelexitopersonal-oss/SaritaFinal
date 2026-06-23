class MetaConstitutionalCalculator:
    """
    Computes GMCI based on:
    - 20% Constitutional Legitimacy
    - 20% Axiomatic Consistency
    - 15% Foundational Stability
    - 15% Non-Obsolescence
    - 15% Constitutional Sovereignty
    - 10% Traceability
    - 5% Reproducibility
    """
    def compute(self, metrics):
        weights = {
            "legitimacy": 0.20,
            "consistency": 0.20,
            "stability": 0.15,
            "non_obsolescence": 0.15,
            "sovereignty": 0.15,
            "traceability": 0.10,
            "reproducibility": 0.05
        }

        gmci_score = 0.0
        for key, weight in weights.items():
            gmci_score += metrics.get(key, 0.0) * weight

        return {
            "gmci_score": round(gmci_score, 4),
            "submetrics": metrics,
            "certification": "METACONSTITUTIONAL_SUPREMACY" if gmci_score >= 0.95 else "VALID"
        }
