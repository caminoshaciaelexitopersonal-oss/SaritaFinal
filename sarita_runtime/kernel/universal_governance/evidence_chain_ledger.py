import json
import datetime

class EvidenceChainLedger:
    def __init__(self, ledger_path="sarita_runtime/kernel/universal_governance/evidence_chain_ledger.json"):
        self.ledger_path = ledger_path
        self.records = []

    def record_chain(self, chain):
        record = {
            "timestamp": datetime.datetime.now().isoformat(),
            "event": "EVIDENCE_CHAIN_MATERIALIZATION",
            "chain": chain
        }
        self.records.append(record)
        self._persist()

    def _persist(self):
        with open(self.ledger_path, "w") as f:
            json.dump(self.records, f, indent=4)
