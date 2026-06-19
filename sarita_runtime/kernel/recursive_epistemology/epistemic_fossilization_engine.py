from .dogma_detector import DogmaDetector
from .stagnation_analyzer import StagnationAnalyzer
from .novelty_pressure_generator import NoveltyPressureGenerator

class EpistemicFossilizationEngine:
    def __init__(self):
        self.detector = DogmaDetector()
        self.analyzer = StagnationAnalyzer()
        self.generator = NoveltyPressureGenerator()

    def check_fossilization(self, knowledge_area, performance):
        is_stagnant = self.analyzer.analyze_stagnation(performance)
        pressure = self.generator.generate_pressure(knowledge_area)
        return {"stagnant": is_stagnant, "suggested_pressure": pressure}
