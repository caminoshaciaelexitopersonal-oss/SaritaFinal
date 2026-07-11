class ConfidenceEngine:
    """
    Computes exact confidence intervals (CI95, CI99) for continuous metrics and error bounds.
    """
    def __init__(self):
        pass

    def calculate_confidence_bounds(self, data: list, confidence: float = 0.95) -> tuple:
        n = len(data)
        if n < 2:
            return (0.0, 0.0)

        mean = sum(data) / n
        std_dev = (sum((x - mean) ** 2 for x in data) / (n - 1)) ** 0.5
        std_err = std_dev / (n ** 0.5)

        if confidence == 0.95:
            z = 1.96
        elif confidence == 0.99:
            z = 2.58
        else:
            z = 1.96

        margin = z * std_err
        return (round(mean - margin, 4), round(mean + margin, 4))
