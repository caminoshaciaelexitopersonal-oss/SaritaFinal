class ExperimentalDesignEngine:
    """
    Guides the choice of experimental designs (A/B, Factorial, Randomized, Longitudinal) based on variables.
    """
    def __init__(self):
        pass

    def recommend_design(self, independent_vars: list, dependent_vars: list, longitudinal: bool = False) -> str:
        if longitudinal:
            return "LONGITUDINAL_DESIGN"
        if len(independent_vars) > 1:
            return "FACTORIAL_DESIGN"
        if len(independent_vars) == 1:
            return "AB_TESTING_DESIGN"
        return "COMPLETELY_RANDOMIZED_DESIGN"
