class GlobalPrescriptiveQualityIndex:
    """
    Main engine for the Global Prescriptive Quality Index (GPQI).
    Scale: 0.0000 -> 1.0000
    """
    def __init__(self, calculator, ledger):
        self.calculator = calculator
        self.ledger = ledger

    def calculate_gpqi(self, data):
        """
        Calculates GPQI as the mean of its specialized sub-metrics.
        """
        metrics = self.calculator.calculate_metrics(data)
        gpqi_value = sum(metrics.values()) / len(metrics)

        result = {
            "gpqi_score": gpqi_value,
            "metrics": metrics,
            "timestamp": "2024-06-11T17:00:00Z"
        }

        if self.ledger:
            self.ledger.record_gpqi(result)

        return result
