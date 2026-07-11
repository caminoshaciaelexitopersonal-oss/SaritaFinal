class HypothesisTracker:
    """
    Tracks the active progress of hypotheses as they move through various experimental pipelines.
    """
    def __init__(self, registry):
        self.registry = registry

    def mark_testing(self, hypothesis_id: str):
        hyp = self.registry.get(hypothesis_id)
        if hyp:
            hyp.status = "TESTING"

    def mark_outcome(self, hypothesis_id: str, accepted: bool):
        hyp = self.registry.get(hypothesis_id)
        if hyp:
            hyp.status = "ACCEPTED" if accepted else "REJECTED"
