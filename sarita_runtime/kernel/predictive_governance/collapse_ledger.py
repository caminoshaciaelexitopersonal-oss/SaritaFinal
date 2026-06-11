import datetime

class CollapseLedger:
    def __init__(self):
        self.records = []
    def record_collapse_assessment(self, assessment):
        self.records.append({"data": assessment, "time": datetime.datetime.now().isoformat()})
