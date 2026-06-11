import uuid

class ScientificOriginTracker:
    """
    Tracks and certifies the scientific origin of every entity in the governance engine.
    """
    def __init__(self, ledger=None):
        self.ledger = ledger
        self.origins = {}

    def track_origin(self, entity_id, origin_info):
        """
        Registers the scientific lineage for a given entity.
        """
        required_fields = [
            "origin_id",
            "experiment_id",
            "hypothesis_id",
            "law_id",
            "theorem_id",
            "certificate_id"
        ]

        # Ensure all required fields exist, even if None
        lineage = {field: origin_info.get(field) for field in required_fields}
        lineage["traceability_id"] = f"TRC-{uuid.uuid4().hex[:8].upper()}"

        self.origins[entity_id] = lineage

        if self.ledger:
            self.ledger.record_origin(entity_id, lineage)

        return lineage["traceability_id"]

    def get_lineage(self, entity_id):
        return self.origins.get(entity_id)

    def verify_lineage_completeness(self, entity_id):
        lineage = self.get_lineage(entity_id)
        if not lineage:
            return False
        # For a full scientific audit, we check if the essential path is present
        # depending on the entity type, but here we require at least an origin and experiment
        return lineage["origin_id"] is not None and lineage["experiment_id"] is not None
