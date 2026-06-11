class GlobalUniversalProspectiveIndex:
    """
    Main engine for calculating the Global Universal Prospective Index (GUPI).
    Scale: 0.0000 -> 1.0000
    """
    def __init__(self, calculator, ledger):
        self.calculator = calculator
        self.ledger = ledger

    def calculate_gupi(self, prospective_data):
        """
        Calculates the GUPI from multiple prospective sub-metrics.
        """
        metrics = self.calculator.calculate_metrics(prospective_data)

        # GUPI is the average of its sub-metrics
        gupi_value = sum(metrics.values()) / len(metrics)

        result = {
            "gupi": gupi_value,
            "metrics": metrics,
            "timestamp": "2024-06-11T15:20:00Z"
        }

        if self.ledger:
            self.ledger.record_gupi(result)

        return result
