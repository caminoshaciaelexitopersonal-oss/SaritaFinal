import datetime

class ProspectiveCertificationLedger:
    def __init__(self):
        self.records = []
    def record_certification(self, cert):
        self.records.append({"data": cert, "time": datetime.datetime.now().isoformat()})
    def record_gupi(self, result):
        self.records.append({"type": "GUPI", "data": result, "time": datetime.datetime.now().isoformat()})
    def record_opportunity_assessment(self, assessment):
        self.records.append({"type": "OPPORTUNITY", "data": assessment, "time": datetime.datetime.now().isoformat()})
    def record_accuracy_audit(self, audit):
        self.records.append({"type": "ACCURACY", "data": audit, "time": datetime.datetime.now().isoformat()})
