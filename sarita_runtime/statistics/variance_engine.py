import math

class VarianceEngine:
    """
    Computes sample and population mean, variance, and standard deviation.
    """
    def __init__(self):
        pass

    def calculate_mean(self, data: list) -> float:
        if not data:
            return 0.0
        return sum(data) / len(data)

    def calculate_variance(self, data: list, sample: bool = True) -> float:
        if len(data) < 2:
            return 0.0
        mean = self.calculate_mean(data)
        sq_diffs = [(x - mean) ** 2 for x in data]
        denom = len(data) - 1 if sample else len(data)
        return sum(sq_diffs) / denom

    def calculate_std_dev(self, data: list, sample: bool = True) -> float:
        return math.sqrt(self.calculate_variance(data, sample))
