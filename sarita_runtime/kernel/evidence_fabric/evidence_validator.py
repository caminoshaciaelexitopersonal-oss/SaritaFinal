from sarita_runtime.kernel.evidence_fabric.evidence_constitution import EvidenceConstitution

class EvidenceValidator:
    """
    Validates material evidence against the constitution.
    """
    def __init__(self):
        pass

    def validate(self, evidence: dict):
        try:
            return EvidenceConstitution.validate_vertex_evidence(evidence)
        except ValueError:
            return False

    def check_lineage(self, current_vertex: dict, previous_vertex: dict):
        """Verifies that the causal chain is continuous."""
        if current_vertex.get("parent_hash") != previous_vertex.get("ledger_hash"):
            return False, "Causal lineage break detected"
        return True, "LINEAGE_VERIFIED"
