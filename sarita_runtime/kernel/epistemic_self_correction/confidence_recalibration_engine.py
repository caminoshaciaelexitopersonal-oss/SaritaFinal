from .confidence_recalibration_ledger import ConfidenceRecalibrationLedger
from .confidence_decay_calculator import ConfidenceDecayCalculator
from .certainty_reassessment_engine import CertaintyReassessmentEngine
from .trust_boundary_validator import TrustBoundaryValidator

class ConfidenceRecalibrationEngine:
    def __init__(self):
        self.ledger = ConfidenceRecalibrationLedger()
        self.decay_calculator = ConfidenceDecayCalculator()
        self.reassessment_engine = CertaintyReassessmentEngine()
        self.boundary_validator = TrustBoundaryValidator()

    def recalibrate(self, context, current_confidence, timestamp, anomalies=0):
        decayed = self.decay_calculator.calculate_decay(current_confidence, timestamp)
        new_confidence = self.reassessment_engine.reassess(decayed, anomalies)

        self.ledger.record_recalibration(
            context=context,
            old_confidence=current_confidence,
            new_confidence=new_confidence
        )

        trusted = self.boundary_validator.validate_boundary(new_confidence)
        return new_confidence, trusted
