import datetime

class PredictiveAccuracyLedger:
    def __init__(self):
        self.records = []
    def record_accuracy_audit(self, audit):
        self.records.append({"type": "ACCURACY_AUDIT", "data": audit, "time": datetime.datetime.now().isoformat()})
    def record_temporal_decay(self, decay_report):
        self.records.append({"type": "TEMPORAL_DECAY", "data": decay_report, "time": datetime.datetime.now().isoformat()})
