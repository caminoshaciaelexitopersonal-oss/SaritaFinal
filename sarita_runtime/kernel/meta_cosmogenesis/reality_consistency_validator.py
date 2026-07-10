class RealityConsistencyValidator:
    """
    Validates if a generated reality architecture is internally consistent.
    """
    def validate(self, architecture):
        # Basic rules:
        # - High contradiction tolerance requires non-classical logic.
        # - High information bottleneck might conflict with rapid temporal flow.

        score = 1.0
        logic = architecture["logic"]["type"]
        tolerance = architecture["logic"]["contradiction_tolerance"]

        if logic == "CLASSICAL" and tolerance > 0.1:
            score -= 0.3 # Consistency penalty

        return max(0.0, min(1.0, score))
