class ConstitutionalFeedbackEngine:
    """
    Integrates historical outcome data into the constitutional evolution process.
    """
    def __init__(self, analyzer, learning_validator):
        self.analyzer = analyzer
        self.learning_validator = learning_validator

    def provide_feedback(self, reform_id, historical_data):
        outcome = self.analyzer.analyze_outcome(reform_id, historical_data)

        return {
            "reform_id": reform_id,
            "outcome_category": outcome, # IMPROVED / WORSENED / STABLE
            "is_learning_valid": self.learning_validator.validate(reform_id, outcome)
        }
