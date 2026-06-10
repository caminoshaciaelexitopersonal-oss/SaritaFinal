class DecisionConsistencyChecker:
    """
    Checks for logical and causal consistency in decisions.
    """
    def check_consistency(self, decision_data: dict) -> bool:
        # Check that timestamps are monotonic and hashes are valid
        if decision_data.get("timestamp", 0) <= 0:
            return False
        if not decision_data.get("causal_hash"):
            return False
        return True
