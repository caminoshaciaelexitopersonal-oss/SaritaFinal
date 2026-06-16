from sarita_runtime.kernel.predictive_governance.forecast_error_analyzer import ForecastErrorAnalyzer
from sarita_runtime.kernel.predictive_governance.prediction_confidence_validator import PredictionConfidenceValidator
from sarita_runtime.kernel.predictive_governance.prospective_reproducibility_engine import ProspectiveReproducibilityEngine

class PredictionAccuracyEngine:
    """
    Engine for auditing the accuracy of predictions.
    """
    def __init__(self, error_analyzer, confidence_validator, reproducibility_engine, ledger):
        self.error_analyzer = error_analyzer
        self.confidence_validator = confidence_validator
        self.reproducibility_engine = reproducibility_engine
        self.ledger = ledger

    def audit_accuracy(self, prediction, actual_outcome):
        """
        Demuestra precisión, estabilidad y confianza estadística.
        """
        error = self.error_analyzer.analyze_error(prediction, actual_outcome)
        confidence = self.confidence_validator.validate_confidence(prediction)
        is_reproducible = self.reproducibility_engine.verify_prospective_reproducibility(prediction)

        audit = {
            "prediction_error": error,
            "confidence_level": confidence,
            "reproducibility_status": is_reproducible,
            "accuracy_score": 1.0 - error
        }

        if self.ledger:
            self.ledger.record_accuracy_audit(audit)

        return audit
