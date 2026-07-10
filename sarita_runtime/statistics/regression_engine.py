from .variance_engine import VarianceEngine

class RegressionEngine:
    """
    Computes simple ordinary least squares linear regression.
    """
    def __init__(self):
        self.variance_eng = VarianceEngine()

    def fit_linear_regression(self, x: list, y: list) -> dict:
        if len(x) != len(y) or len(x) < 2:
            return {"slope": 0.0, "intercept": 0.0, "r_squared": 0.0}

        mean_x = self.variance_eng.calculate_mean(x)
        mean_y = self.variance_eng.calculate_mean(y)

        num = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))
        den = sum((x[i] - mean_x) ** 2 for i in range(len(x)))

        if den == 0.0:
            slope = 0.0
        else:
            slope = num / den

        intercept = mean_y - slope * mean_x

        # Calculate R^2
        y_pred = [slope * xi + intercept for xi in x]
        ss_tot = sum((yi - mean_y) ** 2 for yi in y)
        ss_res = sum((y[i] - y_pred[i]) ** 2 for i in range(len(y)))

        r_squared = 1.0 - (ss_res / ss_tot) if ss_tot > 0.0 else 0.0

        return {
            "slope": round(slope, 4),
            "intercept": round(intercept, 4),
            "r_squared": round(r_squared, 4)
        }
