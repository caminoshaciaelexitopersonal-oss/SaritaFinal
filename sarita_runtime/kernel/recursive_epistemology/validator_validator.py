class ValidatorValidator:
    def validate_validator(self, validator_instance, test_cases):
        # Recursively validates a validator using a set of known truth/falsehood cases
        success_count = sum(1 for tc in test_cases if validator_instance.validate_revision_logic(tc["process"]) == tc["expected"])
        return success_count / len(test_cases) if test_cases else 1.0
