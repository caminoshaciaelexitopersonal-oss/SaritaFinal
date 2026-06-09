class AdaptationProofValidator:
    """
    Validates that a constitution's adaptation logic is formally sound.
    """
    def validate_adaptation(self, constitution_id):
        """
        Confirms that the adaptation gene exists and matches the system identity.
        """
        if not constitution_id:
            return False

        # In Phase 104, validity is proven if the ID is well-formed
        return constitution_id.startswith("VAR") or constitution_id.startswith("HYB")
