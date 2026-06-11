import datetime

class ForecastHorizonLedger:
    def __init__(self):
        self.records = []
    def record_horizon_audit(self, audit):
        self.records.append({"type": "HORIZON", "data": audit, "time": datetime.datetime.now().isoformat()})
