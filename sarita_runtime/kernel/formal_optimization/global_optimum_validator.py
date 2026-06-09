class GlobalOptimumValidator:
    """
    Validates if a solution is the global optimum for the current constitutional state.
    """
    def validate_global_optimum(self, winner, alternatives):
        # A solution is a global optimum if no other alternative has a strictly better score.
        return all(winner.get("gcoi", 0) >= a.get("gcoi", 0) for a in alternatives)
