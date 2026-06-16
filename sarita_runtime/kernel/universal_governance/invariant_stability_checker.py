class InvariantStabilityChecker:
    """
    Analyzes the stability of an invariant over time and across different configurations.
    """
    def check_stability(self, invariant_history):
        if not invariant_history:
            return 0.0000

        # Stability is measured as the inverse of variance in the invariant's validity
        valid_states = [state for state in invariant_history if state is True]
        stability = len(valid_states) / len(invariant_history)
        return stability
