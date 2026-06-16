import json
import datetime

class ScientificCertificationLedger:
    def __init__(self, ledger_path="sarita_runtime/kernel/universal_governance/scientific_certification_ledger.json"):
        self.ledger_path = ledger_path
        self.records = []

    def record_certification(self, entity_type, entity_id, certificate_id):
        record = {
            "timestamp": datetime.datetime.now().isoformat(),
            "event": "SCIENTIFIC_CERTIFICATION",
            "entity_type": entity_type,
            "entity_id": entity_id,
            "certificate_id": certificate_id
        }
        self.records.append(record)
        self._persist()

    def record_invariant_revalidation(self, report):
        self.records.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "event": "INVARIANT_REVALIDATION",
            "report": report
        })
        self._persist()

    def record_causality_audit(self, report):
        self.records.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "event": "CAUSALITY_AUDIT",
            "report": report
        })
        self._persist()

    def record_theorem_audit(self, report):
        self.records.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "event": "THEOREM_AUDIT",
            "report": report
        })
        self._persist()

    def record_gugi_audit(self, report):
        self.records.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "event": "GUGI_AUDIT",
            "report": report
        })
        self._persist()

    def _persist(self):
        with open(self.ledger_path, "w") as f:
            json.dump(self.records, f, indent=4)
