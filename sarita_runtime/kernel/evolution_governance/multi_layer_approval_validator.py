class MultiLayerApprovalValidator:
    """Validates multi-layer approval requirements."""
    def validate_approval(self, consensus, is_certified):
        return consensus["reached"] and is_certified
