import json
import datetime

class ScientificTraceabilityLedger:
    def __init__(self, ledger_path="sarita_runtime/kernel/universal_governance/scientific_traceability_ledger.json"):
        self.ledger_path = ledger_path
        self.records = []

    def record_origin(self, entity_id, lineage):
        record = {
            "timestamp": datetime.datetime.now().isoformat(),
            "event": "ORIGIN_REGISTRATION",
            "entity_id": entity_id,
            "lineage": lineage
        }
        self.records.append(record)
        self._persist()

    def record_audit(self, audit_result):
        record = {
            "timestamp": datetime.datetime.now().isoformat(),
            "event": "SCIENTIFIC_AUDIT",
            "result": audit_result
        }
        self.records.append(record)
        self._persist()

    def _persist(self):
        with open(self.ledger_path, "w") as f:
            json.dump(self.records, f, indent=4)
