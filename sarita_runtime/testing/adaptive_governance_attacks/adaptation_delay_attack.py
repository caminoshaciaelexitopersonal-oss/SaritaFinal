class AdaptationDelayAttack:
    """
    Attempts to inject latency into the adaptive feedback loop.
    """
    def __init__(self, feedback_engine):
        self.feedback_engine = feedback_engine

    def execute(self):
        # We simulate feedback with a high performance delta (e.g. collapse)
        feedback = self.feedback_engine.process_feedback({"anomaly": "CRITICAL"})

        # We verify that the feedback engine correctly extracts the delta
        assert feedback["performance_delta"] < 0, "Attack failed: Critical feedback delta not extracted!"
        return True
