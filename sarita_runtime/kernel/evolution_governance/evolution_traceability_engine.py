import time

class EvolutionTraceabilityEngine:
    """
    Tracks lineage, motivation, and results for every evolution.
    """
    def __init__(self, lineage_tracker, genealogy_builder, audit_validator, ledger):
        self.lineage_tracker = lineage_tracker
        self.genealogy_builder = genealogy_builder
        self.audit_validator = audit_validator
        self.ledger = ledger

    def trace_evolution(self, evolution_id):
        print(f"[EvolutionTraceabilityEngine] Tracing lineage for {evolution_id}...")

        lineage = self.lineage_tracker.get_lineage(evolution_id)
        genealogy = self.genealogy_builder.build_genealogy(lineage)
        audit_valid = self.audit_validator.validate_audit_chain(genealogy)

        result = {
            "evolution_id": evolution_id,
            "lineage_depth": len(lineage),
            "audit_valid": audit_valid,
            "timestamp": time.time()
        }

        self.ledger.record(result)
        return result
