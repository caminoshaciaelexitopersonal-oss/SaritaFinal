import datetime

class PrescriptionLedger:
    def __init__(self):
        self.records = []
    def record_prescription(self, p_type, prescription):
        self.records.append({"type": p_type, "data": prescription, "time": datetime.datetime.now().isoformat()})
    def record_gpui(self, result):
        self.records.append({"type": "GPUI", "data": result, "time": datetime.datetime.now().isoformat()})

class InterventionLedger:
    def __init__(self):
        self.records = []
    def record_intervention(self, intervention):
        self.records.append({"data": intervention, "time": datetime.datetime.now().isoformat()})

class DecisionLedger:
    def __init__(self):
        self.records = []
    def record_decision(self, result):
        self.records.append({"data": result, "time": datetime.datetime.now().isoformat()})

class FutureArchitectureLedger:
    def __init__(self):
        self.records = []
    def record_future_design(self, result):
        self.records.append({"data": result, "time": datetime.datetime.now().isoformat()})

class PolicyLedger:
    def __init__(self):
        self.records = []
    def record_policy_batch(self, result):
        self.records.append({"data": result, "time": datetime.datetime.now().isoformat()})
