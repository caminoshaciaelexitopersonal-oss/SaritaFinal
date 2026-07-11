class SafeExecutionValidator:
    """
    Evaluates execution risks, dependency counts, and failure probability
    to validate whether a task can be safely executed.
    """
    def __init__(self, failure_prediction_engine):
        self.failure_engine = failure_prediction_engine

    def validate_safety(self, task: dict) -> dict:
        """
        Validates safety thresholds for an action.
        """
        risk = task.get("risk", 0.5)
        # Calculate failure probability using the predictor
        fail_prob = self.failure_engine.estimate_failure_probability(
            risk=risk,
            complexity=task.get("complexity", 0.4),
            dependency_count=len(task.get("dependencies", []))
        )

        # Actions with failure probability > 0.85 are blocked as hazardous
        is_safe = fail_prob <= 0.85
        reason = "" if is_safe else f"Extremely high failure probability predicted: {fail_prob}"

        return {
            "safe": is_safe,
            "failure_probability": fail_prob,
            "reason": reason
        }
