class ExecutionFeedbackEngine:
    """
    Analyzes execution results, timing, quality, stability, and safety
    to calculate numeric feedback signals.
    """
    def __init__(self):
        pass

    def evaluate_feedback(self, run_time_sec: float, success: bool, rollback_triggered: bool, quality_delta: float) -> dict:
        """
        Calculates mathematical rewards or penalties based on execution results.
        """
        # Base reward
        reward = 1.0 if success else -1.0

        # Penalize rollback
        if rollback_triggered:
            reward -= 0.5

        # Time penalty (exponential decay for extreme latency)
        time_penalty = min(0.3, run_time_sec * 0.05)
        reward -= time_penalty

        # Quality boost/penalty
        reward += quality_delta * 2.0

        # Clip reward to -2.0 to 2.0
        reward = max(-2.0, min(2.0, reward))

        stability_impact = 1.0 if (success and not rollback_triggered) else 0.4

        return {
            "reward": round(reward, 4),
            "stability_impact": stability_impact,
            "performance_efficiency": 1.0 / (1.0 + run_time_sec)
        }
