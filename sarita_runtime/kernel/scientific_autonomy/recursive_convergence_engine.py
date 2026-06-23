from .fixed_point_detector import FixedPointDetector
from .oscillation_analyzer import OscillationAnalyzer
from .epistemic_equilibrium_estimator import EpistemicEquilibriumEstimator
from .convergence_certifier import ConvergenceCertifier

class RecursiveConvergenceEngine:
    def __init__(self):
        self.detector = FixedPointDetector()
        self.analyzer = OscillationAnalyzer()
        self.estimator = EpistemicEquilibriumEstimator()
        self.certifier = ConvergenceCertifier()

    def evaluate_convergence(self, trajectory):
        fixed_point = self.detector.detect_fixed_point(trajectory)
        oscillating = self.analyzer.analyze_oscillation(trajectory)
        equilibrium = self.estimator.estimate_equilibrium(trajectory)
        certified = self.certifier.certify_convergence(fixed_point, oscillating)

        return {
            "converged": fixed_point,
            "oscillating": oscillating,
            "equilibrium_point": equilibrium,
            "certified": certified
        }
