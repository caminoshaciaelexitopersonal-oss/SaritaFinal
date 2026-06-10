class PremiseValidator:
    """
    Validates that premises are well-formed and non-contradictory.
    """
    def __init__(self, truth_engine):
        self.truth_engine = truth_engine

    def validate(self, premise) -> bool:
        # Basic well-formedness check
        if not hasattr(premise, "operator"):
            return False
        return True

    def check_contradictions(self, premises) -> bool:
        """
        Returns True if a contradiction is found in the premises.
        """
        for p1 in premises:
            for p2 in premises:
                # Direct contradiction: A and ~A
                if p2.operator == "NOT" and p2.left == p1:
                    return True
                if p1.operator == "NOT" and p1.left == p2:
                    return True
        return False
