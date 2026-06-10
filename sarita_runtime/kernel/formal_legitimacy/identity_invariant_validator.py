class IdentityInvariantValidator:
    """
    Ensures Identity Continuity (Ontological Stability).
    """
    def validate(self, proposed_state: dict) -> (bool, str):
        original_identity_hash = proposed_state.get("original_identity_hash")
        current_identity_hash = proposed_state.get("current_identity_hash")

        if original_identity_hash != current_identity_hash:
            return False, "Identity drift detected: Root identity hash mismatch."

        return True, "Identity invariant preserved."
