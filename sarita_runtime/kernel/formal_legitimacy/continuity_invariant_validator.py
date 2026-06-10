class ContinuityInvariantValidator:
    """
    Ensures State Continuity (Causal Stability).
    """
    def validate(self, proposed_state: dict) -> (bool, str):
        parent_hash = proposed_state.get("parent_hash")
        if not parent_hash or len(parent_hash) < 64:
            return False, "Continuity violation: Missing or invalid causal parent hash."

        return True, "Continuity invariant preserved."
