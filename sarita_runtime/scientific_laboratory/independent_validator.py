from .peer_review_engine import PeerReviewEngine
from .external_validation_engine import ExternalValidationEngine
from .blind_validation_engine import BlindValidationEngine
from .double_blind_engine import DoubleBlindValidationEngine
from .replication_engine import ReplicationEngine

class UnifiedIndependentValidator:
    """
    Sovereign Independent Validator (Phase 133).
    The centralized gateway that manages external validations, blind reviews,
    double-blind trials, and standalone replication of experimental trials.
    """
    def __init__(self):
        self.peer_review = PeerReviewEngine()
        self.external_validation = ExternalValidationEngine()
        self.blind_validation = BlindValidationEngine()
        self.double_blind = DoubleBlindValidationEngine()
        self.replication = ReplicationEngine()

    def perform_full_independent_validation(self, raw_evidence: dict, trial_callable) -> dict:
        """
        Coordinates full replication and external verification.
        """
        ext_res = self.external_validation.validate_external_evidence(raw_evidence)
        rep_res = self.replication.replicate_experiment(
            base_results={"mean_score": sum(raw_evidence.values()) / len(raw_evidence) if raw_evidence else 0.95},
            action_callable=trial_callable
        )

        return {
            "external_validation": ext_res,
            "replication": rep_res,
            "rigor_verified": ext_res["valid"] and rep_res["replicated"]
        }
