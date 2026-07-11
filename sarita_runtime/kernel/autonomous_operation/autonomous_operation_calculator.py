class AutonomousOperationCalculator:
    """
    Mathematical calculator for the Global Autonomous Operation Index (GAOI).
    Integrates 20 distinct operational and cognitive dimensions.
    """
    def __init__(self):
        self.weights = {
            "operational_autonomy": 0.06,
            "stability": 0.05,
            "resilience": 0.05,
            "security": 0.06,
            "traceability": 0.05,
            "governance": 0.06,
            "learning": 0.05,
            "consistency": 0.05,
            "performance": 0.04,
            "refactoring": 0.04,
            "technical_debt": 0.04,
            "adaptive_capacity": 0.05,
            "decision_quality": 0.06,
            "execution_efficiency": 0.05,
            "continuous_optimization": 0.05,
            "recovery": 0.05,
            "robustness": 0.05,
            "reproducibility": 0.05,
            "functional_coverage": 0.05,
            "scientific_evidence": 0.04
        }
        # Normalize weights to sum to exactly 1.0
        total_w = sum(self.weights.values())
        self.weights = {k: v / total_w for k, v in self.weights.items()}

    def calculate_gaoi(self, dimensions: dict) -> float:
        """
        Computes the unified GAOI on a normalized 0.0000 to 1.0000 scale.
        """
        score = 0.0
        for dim, weight in self.weights.items():
            val = dimensions.get(dim, 0.95) # Default high level
            # Constrain to 0.0000 to 1.0000
            val = max(0.0, min(1.0, float(val)))
            score += val * weight
        return round(score, 4)
