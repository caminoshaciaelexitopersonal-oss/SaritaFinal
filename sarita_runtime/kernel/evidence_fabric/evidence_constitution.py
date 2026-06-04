import hashlib
import json
import time

class EvidenceConstitution:
    """
    Sovereign Evidence Constitution (Phase 77).
    Defines the mandatory fields and structure for all material evidence.
    """
    MANDATORY_FIELDS = {
        "decision_id",
        "vertex_id",
        "epoch_id",
        "telemetry_hash",
        "ownership_hash",
        "execution_hash",
        "ledger_hash",
        "parent_hash",
        "timestamp"
    }

    @staticmethod
    def validate_vertex_evidence(vertex_data: dict):
        """Ensures the evidence meets constitutional requirements."""
        missing = EvidenceConstitution.MANDATORY_FIELDS - set(vertex_data.keys())
        if missing:
            raise ValueError(f"Evidence Constitutional Violation: Missing fields {missing}")
        return True

    @staticmethod
    def calculate_subsystem_hash(data: dict):
        """Generates a stable hash for a specific evidence subsystem."""
        serialized = json.dumps(data, sort_keys=True)
        return hashlib.sha256(serialized.encode()).hexdigest()
