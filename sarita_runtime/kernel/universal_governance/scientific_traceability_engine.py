class ScientificTraceabilityEngine:
    """
    Main engine for managing scientific traceability across SARITA.
    """
    def __init__(self, tracker, builder, ledger):
        self.tracker = tracker
        self.builder = builder
        self.ledger = ledger

    def audit_entity(self, entity_id):
        """
        Performs a full scientific audit of a specific entity.
        """
        lineage = self.tracker.get_lineage(entity_id)
        if not lineage:
            return {
                "status": "REJECTED",
                "reason": "NO_ORIGIN_DATA",
                "score": 0.0000
            }

        chain = self.builder.build_chain(entity_id)
        is_complete = self.builder.validate_chain_integrity(chain)

        score = 1.0000 if is_complete else 0.5000

        result = {
            "entity_id": entity_id,
            "status": "CERTIFIED" if is_complete else "INCOMPLETE",
            "chain": chain,
            "traceability_score": score
        }

        if self.ledger:
            self.ledger.record_audit(result)

        return result

    def get_global_traceability_index(self, audited_entities):
        """
        Calculates the global scientific traceability index based on audited entities.
        """
        if not audited_entities:
            return 0.0000

        total_score = sum(self.audit_entity(eid)["traceability_score"] for eid in audited_entities)
        return total_score / len(audited_entities)
