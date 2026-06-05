import json
import hashlib

class EvidenceExportProtocol:
    """
    Standardized protocol for exporting kernel evidence to external auditors (Phase 87.5).
    """
    @staticmethod
    def create_evidence_package(graph, ledger):
        # 1. State Snapshot
        state = {
            "ownership": dict(graph.ownership),
            "pressure": graph.global_pressure
        }

        # 2. Causal Events
        events = [v.to_dict() for v in graph.get_all_vertices()]

        # 3. Cryptographic Signature
        package_body = json.dumps({"state": state, "events": events}, sort_keys=True)
        package_hash = hashlib.sha256(package_body.encode()).hexdigest()

        return {
            "version": "1.0",
            "package_hash": package_hash,
            "data": {
                "state": state,
                "events": events
            }
        }

class PortableAttestationBundle:
    """Standardized format for hardware attestations."""
    pass
