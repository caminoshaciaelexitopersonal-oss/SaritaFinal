class TimeSeriesManager:
    """
    Analyzes, indexes, and maintains time-series states of internal indicators.
    """
    def __init__(self):
        pass

    def compute_moving_average(self, series: list, window: int) -> list:
        if not series or window <= 0:
            return []
        averages = []
        for i in range(len(series)):
            start_idx = max(0, i - window + 1)
            subset = series[start_idx:i+1]
            averages.append(sum(subset) / len(subset))
        return averages

    def detect_anomalies(self, series: list, threshold_z: float = 3.0) -> list:
        if len(series) < 2:
            return []
        mean = sum(series) / len(series)
        variance = sum((x - mean) ** 2 for x in series) / (len(series) - 1)
        std_dev = variance ** 0.5
        if std_dev == 0:
            return []

        anomalies = []
        for idx, val in enumerate(series):
            z = abs(val - mean) / std_dev
            if z > threshold_z:
                anomalies.append((idx, val, z))
        return anomalies
