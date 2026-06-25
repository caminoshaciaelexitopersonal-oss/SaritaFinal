from .universe_competition_engine import UniverseCompetitionEngine
from .evolutionary_ecosystem_manager import EvolutionaryEcosystemManager
from .cross_universe_selection import CrossUniverseSelection
from .universe_survival_tracker import UniverseSurvivalTracker
from .meta_fitness_ranker import MetaFitnessRanker

class MetaSelectionEngine:
    def __init__(self):
        self.competition = UniverseCompetitionEngine()
        self.ecosystem = EvolutionaryEcosystemManager()
        self.cross_selection = CrossUniverseSelection()
        self.survival_tracker = UniverseSurvivalTracker()
        self.ranker = MetaFitnessRanker()

    def process_meta_selection(self, universes, performance_metrics):
        ranked = self.ranker.rank_meta_fitness(universes, performance_metrics)
        selected, culled = self.cross_selection.perform_selection(ranked)

        for univ in selected:
            self.survival_tracker.update_survival(univ["identity"]["id"], univ["age"])

        for univ in culled:
            self.survival_tracker.record_extinction(univ["identity"]["id"], univ["age"])

        return selected, culled
