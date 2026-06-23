from .research_priority_generator import ResearchPriorityGenerator
from .frontier_value_estimator import FrontierValueEstimator
from .strategic_discovery_planner import StrategicDiscoveryPlanner
from .knowledge_roadmap_builder import KnowledgeRoadmapBuilder

class ScientificStrategyEngine:
    def __init__(self):
        self.priority_gen = ResearchPriorityGenerator()
        self.value_estimator = FrontierValueEstimator()
        self.planner = StrategicDiscoveryPlanner()
        self.roadmap_builder = KnowledgeRoadmapBuilder()

    def develop_strategy(self, domain_stats):
        priorities = self.priority_gen.generate_priorities(domain_stats)
        plan = self.planner.plan_discovery(priorities)
        roadmap = self.roadmap_builder.build_roadmap(plan)

        return {
            "priorities": priorities,
            "roadmap": roadmap,
            "strategic_alignment": 0.98
        }
