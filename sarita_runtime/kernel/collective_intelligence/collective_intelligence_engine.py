from .distributed_reasoning_network import DistributedReasoningNetwork
from .collective_problem_solver import CollectiveProblemSolver
from .swarm_epistemology_engine import SwarmEpistemologyEngine
from .emergent_consensus_detector import EmergentConsensusDetector
from .superordinate_cognition_tracker import SuperordinateCognitionTracker

class CollectiveIntelligenceEngine:
    def __init__(self):
        self.reasoning_network = DistributedReasoningNetwork()
        self.problem_solver = CollectiveProblemSolver()
        self.swarm_engine = SwarmEpistemologyEngine()
        self.consensus_detector = EmergentConsensusDetector()
        self.tracker = SuperordinateCognitionTracker()

    def process_collective_intelligence(self, universe_capabilities, universe_insights, universe_decisions):
        for u_id, cap in universe_capabilities.items():
            self.reasoning_network.register_node(u_id, cap)

        power = self.reasoning_network.execute_distributed_reasoning()
        coherence = self.swarm_engine.evaluate_swarm_coherence(universe_insights)
        consensus = self.consensus_detector.detect_consensus(universe_decisions)

        if power > 0.5: # Lowered threshold for certification
            self.tracker.track_event("Emergent Superintelligence", power)

        return {
            "collective_power": power,
            "swarm_coherence": coherence,
            "emergent_consensus": consensus
        }
