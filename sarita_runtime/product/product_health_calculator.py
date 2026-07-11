class ProductHealthCalculator:
    """
    Evaluates 16 distinct dimensional weights to compute the Product Health Index (PHI).
    Scale: 0.0000 to 1.0000.
    """
    def __init__(self):
        self.weights = {
            "runtime": 0.08,
            "architecture": 0.07,
            "consistency": 0.08,
            "governance": 0.08,
            "security": 0.08,
            "certification": 0.07,
            "learning": 0.06,
            "auto_architecture": 0.06,
            "operation": 0.07,
            "evidence": 0.05,
            "apis": 0.05,
            "knowledge_graph": 0.05,
            "global_state": 0.06,
            "event_bus": 0.06,
            "control_center": 0.04,
            "orchestration": 0.04
        }
        # Normalize weights to exactly 1.0
        tot = sum(self.weights.values())
        self.weights = {k: v / tot for k, v in self.weights.items()}

    def calculate_phi(self, dimensions: dict) -> float:
        score = 0.0
        for dim, weight in self.weights.items():
            val = float(dimensions.get(dim, 0.9850)) # Default high level
            val = max(0.0, min(1.0, val))
            score += val * weight
        return round(score, 4)
