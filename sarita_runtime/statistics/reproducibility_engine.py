from .variance_engine import VarianceEngine

class StatisticsReproducibilityEngine:
    """
    Evaluates precision repeatability between independent experiment trial runs.
    """
    def __init__(self):
        self.variance_eng = VarianceEngine()

    def calculate_reproducibility(self, run1_data: list, run2_data: list) -> float:
        """
        Calculates reproducibility coefficient.
        Returns near 1.0 if both runs are highly consistent.
        """
        if len(run1_data) != len(run2_data) or not run1_data:
            return 0.0
        m1 = self.variance_eng.calculate_mean(run1_data)
        m2 = self.variance_eng.calculate_mean(run2_data)

        diffs = [abs(run1_data[i] - run2_data[i]) for i in range(len(run1_data))]
        avg_diff = self.variance_eng.calculate_mean(diffs)

        avg_val = (abs(m1) + abs(m2)) / 2.0
        if avg_val == 0.0:
            return 1.0

        score = 1.0 - (avg_diff / avg_val)
        return round(max(0.0, min(1.0, score)), 4)
