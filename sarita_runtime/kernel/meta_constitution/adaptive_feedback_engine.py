class AdaptiveFeedbackEngine:
    """
    Orchestrates the feedback loop between predictions and real-world results.
    """
    def __init__(self, tracker, monitor, evaluator):
        self.tracker = tracker
        self.monitor = monitor
        self.evaluator = evaluator

    def process_feedback(self, prediction: dict, actual_stability: float, actual_risk: str):
        # 1. Track real outcome
        actual_outcome = self.tracker.track_outcome(
            prediction["amendment_id"],
            actual_stability,
            actual_risk
        )

        # 2. Monitor accuracy
        accuracy_report = self.monitor.monitor_accuracy(prediction, actual_outcome)

        # 3. Evaluate effectiveness (long-term)
        effectiveness = self.evaluator.evaluate_policy(
            prediction["amendment_id"],
            [actual_stability]
        )

        return {
            "accuracy_report": accuracy_report,
            "effectiveness": effectiveness
        }
