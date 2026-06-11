class PredictionTraceabilityValidator:
    """
    Validates the scientific traceability of predictions.
    """
    def validate_traceability(self, reconstruction):
        """
        Ensures no gaps exist in the prediction lineage.
        """
        return all(v is not None for v in reconstruction.values())
