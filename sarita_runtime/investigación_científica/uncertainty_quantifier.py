class UncertaintyQuantifier:
    """
    Quantifies systemic and measurement uncertainties, incorporating entropy and relative variances.
    """
    def __init__(self):
        pass

    def quantify_uncertainty(self, data: list) -> float:
        n = len(data)
        if n < 2:
            return 1.0

        mean = sum(data) / n
        if mean == 0:
            return 1.0

        std_dev = (sum((x - mean) ** 2 for x in data) / (n - 1)) ** 0.5
        cv = std_dev / abs(mean)
        return round(cv, 4)
