from .variance_engine import VarianceEngine
from .uncertainty_engine import UncertaintyEngine
from .confidence_interval_engine import ConfidenceIntervalEngine
from .effect_size_engine import EffectSizeEngine
from .correlation_engine import CorrelationEngine
from .regression_engine import RegressionEngine
from .significance_engine import SignificanceEngine
from .hypothesis_testing_engine import HypothesisTestingEngine
from .sensitivity_engine import SensitivityEngine
from .robustness_engine import RobustnessEngine
from .reproducibility_engine import StatisticsReproducibilityEngine

class UnifiedStatisticalEngine:
    """
    Sovereign Statistical Engine (Phase 133).
    The centralized math provider that calculates stats indicators across all system indices.
    """
    def __init__(self):
        self.variance = VarianceEngine()
        self.uncertainty = UncertaintyEngine()
        self.confidence_interval = ConfidenceIntervalEngine()
        self.effect_size = EffectSizeEngine()
        self.correlation = CorrelationEngine()
        self.regression = RegressionEngine()
        self.significance = SignificanceEngine()
        self.hypothesis_testing = HypothesisTestingEngine()
        self.sensitivity = SensitivityEngine()
        self.robustness = RobustnessEngine()
        self.reproducibility = StatisticsReproducibilityEngine()

    def generate_statistical_report(self, data: list, baseline_data: list = None) -> dict:
        """
        Calculates all required statistical metrics for a dataset.
        """
        if not data:
            return {}

        mean = self.variance.calculate_mean(data)
        variance = self.variance.calculate_variance(data)
        std_dev = self.variance.calculate_std_dev(data)
        std_err = self.uncertainty.calculate_standard_error(data)
        ci = self.confidence_interval.calculate_95_ci(data)
        entropy = self.uncertainty.calculate_entropy([x / max(1.0, sum(data)) for x in data])

        report = {
            "mean": round(mean, 4),
            "median": round(sorted(data)[len(data)//2], 4) if data else 0.0,
            "variance": round(variance, 4),
            "std_dev": round(std_dev, 4),
            "std_err": round(std_err, 4),
            "confidence_interval_95": ci,
            "entropy": round(entropy, 4)
        }

        if baseline_data:
            t_test = self.hypothesis_testing.run_t_test(data, baseline_data)
            effect = self.effect_size.calculate_cohens_d(data, baseline_data)
            correlation = self.correlation.calculate_pearson(data[:min(len(data), len(baseline_data))], baseline_data[:min(len(data), len(baseline_data))])
            reproducibility = self.reproducibility.calculate_reproducibility(data[:min(len(data), len(baseline_data))], baseline_data[:min(len(data), len(baseline_data))])

            report.update({
                "t_stat": t_test["t_stat"],
                "p_value": t_test["p_value"],
                "stat_significant": t_test["significant"],
                "cohens_d_effect_size": effect,
                "correlation": correlation,
                "reproducibility_score": reproducibility
            })

        return report
