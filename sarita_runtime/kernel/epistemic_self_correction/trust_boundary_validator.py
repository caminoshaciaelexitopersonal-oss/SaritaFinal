class TrustBoundaryValidator:
    def validate_boundary(self, confidence, threshold=0.1):
        # Triggers distrust when confidence falls below safety threshold
        return confidence > threshold
