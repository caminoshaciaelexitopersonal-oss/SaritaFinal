class NormativeAlignmentValidator:
    """Validates normative alignment with foundational principles."""
    def validate_alignment(self, state):
        return state.get("alignment_score", 1.0) > 0.95
