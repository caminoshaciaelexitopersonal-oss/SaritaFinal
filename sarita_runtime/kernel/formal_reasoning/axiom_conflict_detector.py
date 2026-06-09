class AxiomConflictDetector:
    """
    Specifically detects conflicts between axioms.
    """
    def __init__(self, detector):
        self.detector = detector

    def check_conflict(self, axioms, new_axiom):
        return self.detector.find_contradictions(axioms + [new_axiom])
