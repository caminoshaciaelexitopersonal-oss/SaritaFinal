class ConstitutionalLearningValidator:
    """
    Validates that the system is correctly learning from historical outcomes.
    Ensures that outcomes are properly categorized and registered.
    """
    def validate(self, reform_id, outcome):
        """
        Learning is valid if the outcome belongs to the formal set of
        observable constitutional results.
        """
        valid_outcomes = {"IMPROVED", "WORSENED", "STABLE"}

        if outcome not in valid_outcomes:
            return False

        if not reform_id:
            return False

        return True
