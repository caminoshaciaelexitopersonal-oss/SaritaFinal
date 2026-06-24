from .cultural_mutation_generator import CulturalMutationGenerator
from .tradition_builder import TraditionBuilder
from .cultural_selection_engine import CulturalSelectionEngine
from .belief_ecosystem_manager import BeliefEcosystemManager
from .memetic_evolution_tracker import MemeticEvolutionTracker

class CulturalEvolutionEngine:
    def __init__(self):
        self.mutation_gen = CulturalMutationGenerator()
        self.tradition_builder = TraditionBuilder()
        self.selection_engine = CulturalSelectionEngine()
        self.belief_manager = BeliefEcosystemManager()
        self.meme_tracker = MemeticEvolutionTracker()
        self.civilization_cultures = {} # civ_id -> culture_state

    def initialize_culture(self, civ_id):
        initial_culture = {
            "linguistic": 0.5,
            "artistic": 0.5,
            "ritualistic": 0.5,
            "philosophical": 0.5,
            "technological": 0.5
        }
        self.civilization_cultures[civ_id] = initial_culture
        return initial_culture

    def evolve_culture(self, civ_id, adaptation_pressure=0.5):
        if civ_id not in self.civilization_cultures:
            self.initialize_culture(civ_id)

        current_culture = self.civilization_cultures[civ_id]

        # Generate candidates via mutation
        candidates = []
        for _ in range(5):
            mutated, _ = self.mutation_gen.generate_mutation(current_culture)
            candidates.append(mutated)

        # Select best candidate
        selected = self.selection_engine.select_culture(candidates, adaptation_pressure)
        self.civilization_cultures[civ_id] = selected

        # Create traditions and track memes
        tradition = self.tradition_builder.build_tradition(civ_id, selected)
        self.belief_manager.add_belief(civ_id, tradition)
        self.meme_tracker.track_meme(tradition["id"], civ_id)

        return selected

    def get_culture(self, civ_id):
        return self.civilization_cultures.get(civ_id)
