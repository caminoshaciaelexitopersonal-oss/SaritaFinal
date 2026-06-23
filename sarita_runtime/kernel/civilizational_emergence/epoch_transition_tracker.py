class EpochTransitionTracker:
    def detect_transition(self, timeline):
        # Detects if a new "era" has started based on cumulative changes
        if len(timeline) > 10:
            return "NEW_ERA_REACHED"
        return "STABLE_ERA"
