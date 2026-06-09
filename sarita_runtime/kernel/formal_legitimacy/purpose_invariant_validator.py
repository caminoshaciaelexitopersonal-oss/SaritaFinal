class PurposeInvariantValidator:
    """
    Ensures Purpose Alignment (Teleological Stability).
    """
    def validate(self, proposed_state: dict) -> (bool, str):
        foundational_purpose = proposed_state.get("foundational_purpose")
        proposed_purpose = proposed_state.get("proposed_purpose")

        # In a real system, we'd check if proposed_purpose is a subset of foundational_purpose
        if proposed_purpose not in foundational_purpose:
            return False, f"Purpose violation: {proposed_purpose} deviates from foundational intent."

        return True, "Purpose invariant preserved."
