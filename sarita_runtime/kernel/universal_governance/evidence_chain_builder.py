class EvidenceChainBuilder:
    """
    Reconstructs the full evidence chain from raw data to final certification.
    """
    def __init__(self, origin_tracker):
        self.origin_tracker = origin_tracker

    def build_chain(self, entity_id):
        """
        Reconstructs the lineage:
        Report -> Theorem -> Law -> Experiment -> Hypothesis -> Universes
        """
        lineage = self.origin_tracker.get_lineage(entity_id)
        if not lineage:
            return None

        chain = {
            "entity_id": entity_id,
            "traceability_id": lineage.get("traceability_id"),
            "steps": [
                {"stage": "HYPOTHESIS", "id": lineage.get("hypothesis_id")},
                {"stage": "EXPERIMENT", "id": lineage.get("experiment_id")},
                {"stage": "LAW", "id": lineage.get("law_id")},
                {"stage": "THEOREM", "id": lineage.get("theorem_id")},
                {"stage": "CERTIFICATION", "id": lineage.get("certificate_id")}
            ]
        }
        return chain

    def validate_chain_integrity(self, chain):
        """
        Verifies that there are no gaps in the evidence chain.
        """
        if not chain:
            return False

        for step in chain["steps"]:
            # Every stage must have a non-null ID for total traceability
            if step["id"] is None:
                return False
        return True
