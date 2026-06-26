from .self_architecture_calculator import SelfArchitectureCalculator

class GlobalSelfArchitectureIndex:
    def __init__(self):
        self.calculator = SelfArchitectureCalculator()
        self.history = []

    def update(self, metrics):
        score = self.calculator.calculate_gsai(metrics)
        self.history.append({
            "score": score,
            "metrics": metrics
        })
        return score

    def get_latest(self):
        return self.history[-1]["score"] if self.history else 0.0
