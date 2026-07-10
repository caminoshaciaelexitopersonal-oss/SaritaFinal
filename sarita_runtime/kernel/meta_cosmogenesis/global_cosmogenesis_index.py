from .cosmogenesis_calculator import CosmogenesisCalculator

class GlobalCosmogenesisIndex:
    """
    Maintains the state and history of the GCI.
    """
    def __init__(self):
        self.calculator = CosmogenesisCalculator()
        self.history = []

    def update_index(self, metrics):
        gci = self.calculator.calculate_gci(metrics)
        self.history.append({
            "index": gci,
            "metrics": metrics
        })
        return gci

    def get_latest(self):
        return self.history[-1]["index"] if self.history else 0.0
