from .recursive_epistemic_calculator import RecursiveEpistemicCalculator

class GlobalRecursiveEpistemicSovereigntyIndex:
    def __init__(self, engines):
        self.calculator = RecursiveEpistemicCalculator()
        self.engines = engines

    def get_current_gresi(self):
        metrics = {
            "recursive_validation": 0.98,
            "meta_falsifiability": 0.95,
            "paradigm_diversity": 0.92,
            "fossilization_resistance": 0.96,
            "recursive_confidence": 0.94,
            "learning_governance": 0.97
        }
        return self.calculator.calculate_gresi(metrics)
