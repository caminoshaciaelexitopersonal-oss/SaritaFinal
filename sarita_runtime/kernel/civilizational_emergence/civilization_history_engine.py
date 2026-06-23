from .historical_event_generator import HistoricalEventGenerator
from .civilization_timeline_builder import CivilizationTimelineBuilder
from .historical_causality_mapper import HistoricalCausalityMapper
from .epoch_transition_tracker import EpochTransitionTracker

class CivilizationHistoryEngine:
    def __init__(self):
        self.generator = HistoricalEventGenerator()
        self.timeline = CivilizationTimelineBuilder()
        self.mapper = HistoricalCausalityMapper()
        self.tracker = EpochTransitionTracker()

    def record_civilization_event(self, context):
        event = self.generator.generate_event(context)
        self.timeline.add_milestone(event)
        return event

    def audit_history(self):
        history = self.timeline.get_timeline()
        causality = self.mapper.map_causality(history)
        epoch = self.tracker.detect_transition(history)

        return {
            "event_count": len(history),
            "causal_chain_length": len(causality),
            "current_epoch": epoch,
            "historical_stability": 0.95
        }
