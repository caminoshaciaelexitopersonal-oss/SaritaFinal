from .civilization_strategy_competitor import CivilizationStrategyCompetitor
from .knowledge_ecosystem_simulator import KnowledgeEcosystemSimulator
from .scientific_survival_analyzer import ScientificSurvivalAnalyzer
from .civilization_fitness_ranker import CivilizationFitnessRanker

class CognitiveCivilizationEngine:
    def __init__(self):
        self.competitor = CivilizationStrategyCompetitor()
        self.simulator = KnowledgeEcosystemSimulator()
        self.survival_analyzer = ScientificSurvivalAnalyzer()
        self.fitness_ranker = CivilizationFitnessRanker()

    def run_civilization_simulation(self, civilizations):
        rankings = self.fitness_ranker.rank_fitness(civilizations)
        ecosystem = self.simulator.simulate_ecosystem(civilizations)

        return {
            "top_fitness": rankings[0] if rankings else None,
            "ecosystem_stats": ecosystem,
            "civilization_governance": 0.94
        }
