import json
import datetime

class ReproducibilityLedger:
    def __init__(self, ledger_path="sarita_runtime/kernel/universal_governance/reproducibility_ledger.json"):
        self.ledger_path = ledger_path
        self.records = []

    def record_reproducibility_report(self, report):
        record = {
            "timestamp": datetime.datetime.now().isoformat(),
            "event": "REPRODUCIBILITY_CERTIFICATION",
            "report": report
        }
        self.records.append(record)
        self._persist()

    def _persist(self):
        with open(self.ledger_path, "w") as f:
            json.dump(self.records, f, indent=4)
