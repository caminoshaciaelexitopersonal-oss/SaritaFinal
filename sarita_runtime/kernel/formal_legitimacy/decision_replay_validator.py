class DecisionReplayValidator:
    """
    Validates that a decision can be deterministically replayed.
    """
    def validate_replay(self, decision_data: dict) -> bool:
        # In a real system, this would use the RuntimeReplayEngine
        # and compare the resulting state with the decision_data.
        return decision_data.get("is_deterministic", False)
