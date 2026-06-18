from .belief_lifecycle_manager import BeliefLifecycleManager
from .knowledge_decay_tracker import KnowledgeDecayTracker
from .adaptive_truth_framework import AdaptiveTruthFramework

class EpistemicEvolutionEngine:
    def __init__(self):
        self.lifecycle_manager = BeliefLifecycleManager()
        self.decay_tracker = KnowledgeDecayTracker()
        self.truth_framework = AdaptiveTruthFramework()

    def evolve_knowledge(self, knowledge_base):
        decaying = self.decay_tracker.track_decay(knowledge_base)
        for area in decaying:
            knowledge_base[area]["status"] = "OBSOLETE"
        return knowledge_base
