import os
import json
import shutil

class EvidenceConsolidationEngine:
    """
    Consolidates all historical evidence into a single index.
    Phase 129.15.
    """
    def consolidate(self, inventory):
        evidence_index = {
            "audits": inventory.get("audits", []),
            "proofs": [f for f in os.listdir(".") if "PROOF" in f or "CERTIFICATION" in f],
            "indices": inventory.get("indices", []),
            "total_count": 0
        }
        evidence_index["total_count"] = len(evidence_index["audits"]) + len(evidence_index["proofs"])

        with open("global_evidence_index.json", "w") as f:
            json.dump(evidence_index, f, indent=2)
        return evidence_index

class LegacyCertificationMigrator:
    """
    Archives per-phase certifications to a historical repository.
    Phase 129.16.
    """
    def migrate_to_history(self, history_dir="sarita_runtime/kernel/historical_certifications/"):
        if not os.path.exists(history_dir):
            os.makedirs(history_dir)

        count = 0
        for f in os.listdir("."):
            if "SARITA_PHASE_" in f or "CERTIFICATION" in f and "GLOBAL" not in f:
                # In a real scenario we would move the file.
                # For this task we copy to ensure we don't break subsequent steps.
                shutil.copy(f, os.path.join(history_dir, f))
                count += 1
        return count
