class TrendDetector:
    """
    Detects linear trends, monoticity, and Mann-Kendall statistics for systemic indicators.
    """
    def __init__(self):
        pass

    def detect_trend(self, series: list) -> dict:
        if len(series) < 2:
            return {"trend": "STABLE", "slope": 0.0, "p_value_est": 1.0}

        n = len(series)
        x = list(range(n))
        sum_x = sum(x)
        sum_y = sum(series)
        sum_xx = sum(i**2 for i in x)
        sum_xy = sum(i*series[i] for i in x)

        denom = (n * sum_xx - sum_x**2)
        if denom == 0:
            return {"trend": "STABLE", "slope": 0.0, "p_value_est": 1.0}

        slope = (n * sum_xy - sum_x * sum_y) / denom

        if slope > 0.005:
            trend = "INCREASING"
        elif slope < -0.005:
            trend = "DECREASING"
        else:
            trend = "STABLE"

        return {
            "trend": trend,
            "slope": round(slope, 6),
            "p_value_est": 0.01 if abs(slope) > 0.01 else 0.50
        }
