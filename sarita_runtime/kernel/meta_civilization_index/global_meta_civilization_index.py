from .meta_civilization_calculator import MetaCivilizationCalculator

class GlobalMetaCivilizationIndex:
    def __init__(self):
        self.calculator = MetaCivilizationCalculator()
        self.history = []

    def update_index(self, ecosystem_metrics):
        gmci = self.calculator.calculate_gmci(ecosystem_metrics)
        self.history.append(gmci)
        return gmci

    def get_latest(self):
        return self.history[-1] if self.history else 0.0
