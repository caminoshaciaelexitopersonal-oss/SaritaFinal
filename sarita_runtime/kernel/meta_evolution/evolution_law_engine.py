from .law_mutation_engine import LawMutationEngine
from .law_selection_engine import LawSelectionEngine
from .law_extinction_engine import LawExtinctionEngine
from .law_recombination_engine import LawRecombinationEngine
from .law_fitness_evaluator import LawFitnessEvaluator

class EvolutionaryLawEngine:
    def __init__(self):
        self.mutator = LawMutationEngine()
        self.evaluator = LawFitnessEvaluator()
        self.selector = LawSelectionEngine(self.evaluator)
        self.extinction = LawExtinctionEngine()
        self.recombiner = LawRecombinationEngine()

    def evolve_laws(self, universe_laws_list, performance_map):
        best_laws = self.selector.select_best_laws(universe_laws_list, performance_map)

        new_generation = []
        # Keep best
        new_generation.extend(best_laws)

        # Mutate and recombine to fill back
        while len(new_generation) < len(universe_laws_list):
            parent_a = best_laws[0]
            parent_b = best_laws[1] if len(best_laws) > 1 else best_laws[0]

            offspring = self.recombiner.recombine(parent_a, parent_b)
            offspring = self.mutator.mutate_laws(offspring)
            new_generation.append(offspring)

        return new_generation
