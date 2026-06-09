class ExistenceValidationEngine:
    """
    Validates SARITA's existence against its formal justifications.
    """
    def validate_existence(self, justifications: dict, current_metrics: dict):
        total_valid = 0
        for key in justifications:
            if current_metrics.get(key, 0) > 0.5:
                total_valid += 1
        return total_valid / len(justifications) if justifications else 1.0
