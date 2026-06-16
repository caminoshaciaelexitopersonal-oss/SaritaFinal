class GlobalAdaptiveUniversalityIndex:
    """
    Main engine for the Global Adaptive Universality Index (GAUI).
    Scale: 0.0000 -> 1.0000
    """
    def __init__(self, calculator, ledger):
        self.calculator = calculator
        self.ledger = ledger

    def calculate_gaui(self, data):
        """
        Calculates GAUI as the mean of its adaptive sub-metrics.
        """
        metrics = self.calculator.calculate_metrics(data)
        gaui_value = sum(metrics.values()) / len(metrics)

        result = {
            "gaui_score": gaui_value,
            "metrics": metrics,
            "timestamp": "2024-06-11T19:00:00Z"
        }

        if self.ledger:
            self.ledger.record_gaui(result)

        return result
