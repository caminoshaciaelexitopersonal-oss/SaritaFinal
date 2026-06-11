import datetime

class UncertaintyLedger:
    def __init__(self):
        self.records = []
    def record_uncertainty_audit(self, report):
        self.records.append({"type": "UNCERTAINTY", "data": report, "time": datetime.datetime.now().isoformat()})
