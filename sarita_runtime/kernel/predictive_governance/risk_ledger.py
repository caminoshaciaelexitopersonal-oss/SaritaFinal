import datetime

class RiskLedger:
    def __init__(self):
        self.records = []
    def record_risk_assessment(self, assessment):
        self.records.append({"data": assessment, "time": datetime.datetime.now().isoformat()})
