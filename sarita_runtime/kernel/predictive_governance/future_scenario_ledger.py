import datetime

class FutureScenarioLedger:
    def __init__(self):
        self.records = []
    def record_scenario(self, scenario):
        self.records.append({"data": scenario, "time": datetime.datetime.now().isoformat()})
