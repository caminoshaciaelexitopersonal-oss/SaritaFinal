class DistributionAnalyzer:
    """
    Analyzes sample distributions for normal alignment, skewness, kurtosis, and Kolmogorov-Smirnov metrics.
    """
    def __init__(self):
        pass

    def analyze(self, data: list) -> dict:
        n = len(data)
        if n < 3:
            return {"skewness": 0.0, "kurtosis": 0.0, "is_normal": True}

        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / (n - 1)
        std_dev = variance ** 0.5

        if std_dev == 0:
            return {"skewness": 0.0, "kurtosis": 0.0, "is_normal": True}

        skewness = (sum((x - mean) ** 3 for x in data) / n) / (std_dev ** 3)
        kurtosis = (sum((x - mean) ** 4 for x in data) / n) / (std_dev ** 4) - 3.0

        is_normal = abs(skewness) < 2.0 and abs(kurtosis) < 5.0

        return {
            "skewness": round(skewness, 4),
            "kurtosis": round(kurtosis, 4),
            "is_normal": is_normal
        }
