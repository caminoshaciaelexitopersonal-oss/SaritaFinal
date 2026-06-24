from .civilization_birth_engine import CivilizationBirthEngine
from .civilization_speciation_engine import CivilizationSpeciationEngine
from .civilization_divergence_engine import CivilizationDivergenceEngine

class MetaCivilizationEngine:
    def __init__(self):
        self.birth_engine = CivilizationBirthEngine()
        self.speciation_engine = CivilizationSpeciationEngine(self.birth_engine)
        self.divergence_engine = CivilizationDivergenceEngine()
        self.history = []

    def initialize_ecosystem(self, initial_count=3):
        for _ in range(initial_count):
            self.birth_engine.birth_initial_civilization()
        return self.birth_engine.list_active()

    def evolve_step(self, environmental_pressure=0.5):
        active = self.birth_engine.list_active()
        new_speciations = []

        for civ in active:
            civ["age"] += 1
            if self.speciation_engine.check_speciation_trigger(civ["identity"]["id"], environmental_pressure):
                new_civ = self.speciation_engine.speciate(civ["identity"]["id"])
                new_speciations.append(new_civ)

        metrics = self.get_current_metrics()
        self.history.append(metrics)
        return new_speciations

    def get_current_metrics(self):
        active = self.birth_engine.list_active()
        diversity = self.divergence_engine.analyze_ecosystem_divergence(active)

        return {
            "total_civilizations": len(active),
            "ecosystem_diversity": diversity,
            "avg_age": sum(c["age"] for c in active) / len(active) if active else 0
        }
