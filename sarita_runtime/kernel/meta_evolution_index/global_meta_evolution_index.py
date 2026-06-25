from .meta_evolution_calculator import MetaEvolutionCalculator

class GlobalMetaEvolutionIndex:
    def __init__(self):
        self.calculator = MetaEvolutionCalculator()
        self.history = []

    def update_index(self, metrics):
        index = self.calculator.calculate_gmei2(metrics)
        self.history.append(index)
        return index

    def get_latest(self):
        return self.history[-1] if self.history else 0.0
