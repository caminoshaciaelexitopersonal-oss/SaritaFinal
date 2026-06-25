from .universe_birth_engine import UniverseBirthEngine
from .universe_divergence_engine import UniverseDivergenceEngine

class MetaUniverseEngine:
    def __init__(self):
        self.birth_engine = UniverseBirthEngine()
        self.divergence_engine = UniverseDivergenceEngine()
        self.universes = []

    def initialize_multiverse(self, count=3):
        for _ in range(count):
            univ = self.birth_engine.birth_universe()
            self.universes.append(univ)
        return self.universes

    def get_multiverse_metrics(self):
        return {
            "total_universes": len(self.universes),
            "multiverse_divergence": self.divergence_engine.analyze_multiverse(self.universes)
        }
