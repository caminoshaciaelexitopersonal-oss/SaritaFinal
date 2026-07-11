class OutlierDetector:
    """
    Detects outliers using standard deviation thresholds and the Interquartile Range (IQR) method.
    """
    def __init__(self):
        pass

    def detect_outliers_z_score(self, data: list, threshold: float = 3.0) -> list:
        if len(data) < 2:
            return []
        mean = sum(data) / len(data)
        std_dev = (sum((x - mean) ** 2 for x in data) / (len(data) - 1)) ** 0.5
        if std_dev == 0:
            return []

        outliers = []
        for x in data:
            if abs(x - mean) / std_dev > threshold:
                outliers.append(x)
        return outliers

    def detect_outliers_iqr(self, data: list, factor: float = 1.5) -> list:
        if len(data) < 4:
            return []
        sorted_data = sorted(data)
        n = len(sorted_data)

        q1 = sorted_data[n // 4]
        q3 = sorted_data[(3 * n) // 4]
        iqr = q3 - q1

        lower_bound = q1 - factor * iqr
        upper_bound = q3 + factor * iqr

        return [x for x in data if x < lower_bound or x > upper_bound]
