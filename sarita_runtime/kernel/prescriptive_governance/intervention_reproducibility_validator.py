class InterventionReproducibilityValidator:
    """
    Validates if an intervention produces the same result on replay.
    """
    def validate_reproducibility(self, original_outcome, reproduced_outcome):
        """
        Compares original vs reproduced outcome for exact match.
        """
        if not original_outcome or not reproduced_outcome:
            return False

        return original_outcome == reproduced_outcome
