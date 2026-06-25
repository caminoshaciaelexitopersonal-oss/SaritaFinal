from .historical_path_generator import HistoricalPathGenerator
from .causal_chain_evolver import CausalChainEvolver
from .epoch_creator import EpochCreator
from .historical_unexpected_event_detector import HistoricalUnexpectedEventDetector

class EmergentHistoryEngine:
    def __init__(self):
        self.path_gen = HistoricalPathGenerator()
        self.causal_evolver = CausalChainEvolver()
        self.epoch_creator = EpochCreator()
        self.unexpected_detector = HistoricalUnexpectedEventDetector()
        self.step = 0
        self.baseline_metrics = {}

    def record_history(self, event_type, participants, metrics):
        path = self.path_gen.generate_path(event_type, participants)
        for p in participants:
            self.causal_evolver.add_event(p, path)

        unexpected = self.unexpected_detector.detect_unexpected(metrics, self.baseline_metrics)
        if unexpected:
            for p in participants:
                self.causal_evolver.add_event(p, f"UNEXPECTED: {unexpected}")

        self.baseline_metrics = metrics.copy()
        self.step += 1

        if self.step % 10 == 0:
            self.epoch_creator.declare_epoch(f"Epoch {self.step // 10}", self.step, "Emergent Complexity")

        return path
