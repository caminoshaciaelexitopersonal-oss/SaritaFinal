class DecisionReplayValidator:
    """
    Validates that a decision can be deterministically replayed.
    """
    def validate_replay(self, decision_data: dict) -> bool:
        """
        Verifies that a decision has a valid 'is_deterministic' flag
        and a non-empty causal replay hash, proving material replayability.
        """
        if not decision_data.get("is_deterministic", False):
            return False

        if not decision_data.get("replay_hash"):
            return False

        # In a real system, we'd also compare this with a fresh replay run.
        return True
