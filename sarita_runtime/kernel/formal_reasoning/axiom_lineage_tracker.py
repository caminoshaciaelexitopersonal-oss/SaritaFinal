class AxiomLineageTracker:
    """
    Tracks the origin and usage of axioms in theorem derivations.
    """
    def __init__(self):
        self.lineage = {}

    def record_usage(self, axiom_id, theorem_id):
        if axiom_id not in self.lineage:
            self.lineage[axiom_id] = []
        self.lineage[axiom_id].append(theorem_id)

    def get_lineage(self, axiom_id):
        return self.lineage.get(axiom_id, [])
