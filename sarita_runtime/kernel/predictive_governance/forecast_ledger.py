import datetime

class ForecastLedger:
    def __init__(self):
        self.records = []
    def record_prediction(self, p_type, prediction):
        self.records.append({"type": p_type, "data": prediction, "time": datetime.datetime.now().isoformat()})
    def record_multiverse_forecast(self, forecast):
        self.records.append({"type": "MULTIVERSE", "data": forecast, "time": datetime.datetime.now().isoformat()})
