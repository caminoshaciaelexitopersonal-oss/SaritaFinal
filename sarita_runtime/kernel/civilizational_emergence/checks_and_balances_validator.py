class ChecksAndBalancesValidator:
    def validate_separation(self, branches):
        # Ensures no single branch is performing all operations
        return len(set(branches)) >= 3
