class PurposeAlignmentValidator:
    """
    Validates if a proposed action or policy aligns with registered goals.
    """
    def validate_alignment(self, action: dict, goals: dict):
        # In a real implementation, this would use semantic analysis or formal proofs
        # For Phase 94, we check for explicit goal references or tag matching
        action_goal = action.get("serves_goal")
        if action_goal and action_goal in goals:
            return True, f"Aligned with {action_goal}"
        return False, "No explicit goal alignment detected"
