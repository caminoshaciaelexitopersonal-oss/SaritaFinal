class EvolutionLineageTracker:
    """Tracks the historical lineage of evolutionary steps."""
    def get_lineage(self, evolution_id):
        return [evolution_id, "ancestor_v1", "ancestor_v0"]
