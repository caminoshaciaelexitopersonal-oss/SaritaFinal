from .confidence_of_confidence_calculator import ConfidenceOfConfidenceCalculator
from .uncertainty_of_uncertainty_engine import UncertaintyOfUncertaintyEngine

class RecursiveConfidenceEngine:
    def __init__(self):
        self.meta_conf_calc = ConfidenceOfConfidenceCalculator()
        self.meta_unc_calc = UncertaintyOfUncertaintyEngine()

    def get_recursive_metrics(self, confidence, sigma, evidence_data):
        meta_conf = self.meta_conf_calc.calculate_meta_confidence(confidence, evidence_data["consistency"])
        meta_unc = self.meta_unc_calc.calculate_meta_uncertainty(sigma, evidence_data["variance"])
        return {"meta_confidence": meta_conf, "meta_uncertainty": meta_unc}
