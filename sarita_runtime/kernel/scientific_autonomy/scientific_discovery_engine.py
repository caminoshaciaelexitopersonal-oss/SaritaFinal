from .hypothesis_generator import HypothesisGenerator
from .theory_builder import TheoryBuilder
from .experimental_designer import ExperimentalDesigner
from .theory_refinement_engine import TheoryRefinementEngine

class ScientificDiscoveryEngine:
    def __init__(self):
        self.hypo_gen = HypothesisGenerator()
        self.theory_builder = TheoryBuilder()
        self.exp_designer = ExperimentalDesigner()
        self.refiner = TheoryRefinementEngine()

    def perform_discovery(self, domain_data):
        hypo = self.hypo_gen.generate_hypothesis(domain_data)
        experiment = self.exp_designer.design_experiment(hypo)

        # Simulated experiment result
        results = {"success_rate": 0.98}

        theory = self.theory_builder.build_theory([hypo])
        refined_theory = self.refiner.refine_theory(theory, results)

        return {
            "hypothesis": hypo,
            "experiment": experiment,
            "theory": refined_theory
        }
