class SelfArchitectureCalculator:
    """
    Calculates GSAI based on multidimensional architectural metrics.
    Phase 128.10.
    """
    def calculate_gsai(self, metrics):
        """
        metrics = {
            "cohesion": 0-1,
            "coupling": 0-1,
            "modularity": 0-1,
            "reutilización": 0-1,
            "mantenibilidad": 0-1,
            "complejidad": 0-1,
            "deuda_técnica": 0-1,
            "entropía": 0-1,
            "estabilidad": 0-1,
            "escalabilidad": 0-1,
            "evolucionabilidad": 0-1,
            "refactorización": 0-1
        }
        """
        # Complex weighted average
        # Higher is better, so we invert metrics like complexity/debt
        weights = {
            "cohesion": 0.1, "coupling": 0.1, "modularity": 0.1,
            "mantenibilidad": 0.1, "estabilidad": 0.1, "escalabilidad": 0.1,
            "evolucionabilidad": 0.1, "refactorización": 0.1,
            "complejidad": -0.05, "deuda_técnica": -0.1, "entropía": -0.05
        }

        score = 0.0
        for key, weight in weights.items():
            val = metrics.get(key, 0.5)
            if weight < 0:
                score += (1.0 - val) * abs(weight)
            else:
                score += val * weight

        # Normalize to 0-1
        return round(max(0.0, min(1.0, score * (1.0 / sum(abs(w) for w in weights.values())))), 4)

class GlobalSelfArchitectureIndex:
    def __init__(self):
        self.calculator = SelfArchitectureCalculator()
        self.history = []

    def update(self, metrics):
        gsai = self.calculator.calculate_gsai(metrics)
        self.history.append({"gsai": gsai, "metrics": metrics})
        return gsai

    def get_latest(self):
        return self.history[-1]["gsai"] if self.history else 0.0
