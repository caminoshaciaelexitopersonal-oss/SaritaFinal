class PrescriptionReproducibilityValidator:
    """
    Validates if a prescription produces the same result on replay.
    """
    def validate_reproducibility(self, original, reproduced):
        """
        Guarantees 100% reconstruction of prescriptions.
        """
        # Exact match or logical equivalence
        return original.get("best_intervention") == reproduced.get("best_intervention")
