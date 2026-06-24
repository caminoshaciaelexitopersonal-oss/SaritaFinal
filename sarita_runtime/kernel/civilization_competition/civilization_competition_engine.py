from .resource_competition_manager import ResourceCompetitionManager
from .innovation_race_engine import InnovationRaceEngine
from .knowledge_warfare_simulator import KnowledgeWarfareSimulator
from .alliance_bloc_engine import AllianceBlocEngine
from .civilization_ranker import CivilizationRanker

class CivilizationCompetitionEngine:
    def __init__(self):
        self.resource_manager = ResourceCompetitionManager()
        self.innovation_engine = InnovationRaceEngine()
        self.warfare_simulator = KnowledgeWarfareSimulator()
        self.alliance_engine = AllianceBlocEngine()
        self.ranker = CivilizationRanker()

    def update_competition(self, civilizations):
        self.resource_manager.resolve_competition(civilizations)
        for civ in civilizations:
            civ_id = civ["identity"]["id"]
            focus = civ["genome"].get("technological_focus", 0.5)
            self.innovation_engine.advance_innovation(civ_id, focus)

    def get_rankings(self, civilizations):
        return self.ranker.rank_civilizations(civilizations, self.resource_manager, self.innovation_engine)
