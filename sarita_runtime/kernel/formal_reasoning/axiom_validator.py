class AxiomValidator:
    """
    Validates that axioms are foundational and consistent.
    """
    def __init__(self, consistency_engine):
        self.consistency_engine = consistency_engine

    def validate_axioms(self, axioms):
        result = self.consistency_engine.verify_consistency(axioms)
        return result["is_consistent"]
