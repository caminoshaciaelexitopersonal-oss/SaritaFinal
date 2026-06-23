from .global_consistency_validator import GlobalConsistencyValidator
from .cross_engine_contradiction_detector import CrossEngineContradictionDetector
from .architectural_coherence_prover import ArchitecturalCoherenceProver
from .recursive_stability_monitor import RecursiveStabilityMonitor

class RecursiveCoherenceEngine:
    def __init__(self):
        self.validator = GlobalConsistencyValidator()
        self.detector = CrossEngineContradictionDetector()
        self.prover = ArchitecturalCoherenceProver()
        self.monitor = RecursiveStabilityMonitor()

    def audit_coherence(self, system_state):
        consistency = self.validator.validate_consistency(system_state.get("states", []))
        coherence = self.prover.prove_coherence(system_state.get("components", []))
        stability = self.monitor.monitor_stability(system_state.get("audit_history", []))

        return {
            "consistent": consistency,
            "coherence_score": coherence,
            "stability_score": stability
        }
