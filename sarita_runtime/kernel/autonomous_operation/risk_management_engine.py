from .failure_prediction_engine import FailurePredictionEngine
from .rollback_manager import RollbackManager
from .safe_execution_validator import SafeExecutionValidator

class RiskManagementEngine:
    """
    Risk evaluation and prevention system that halts high-risk executions.
    """
    def __init__(self):
        self.failure_engine = FailurePredictionEngine()
        self.rollback_manager = RollbackManager()
        self.validator = SafeExecutionValidator(self.failure_engine)

    def assess_risk(self, decision_node: dict) -> dict:
        """
        Calculates criticality, reversibility and blocks unsafe modifications.
        """
        impact = decision_node.get("impact", 0.5)
        risk_val = decision_node.get("risk", 0.5)

        # Criticality = impact * risk
        criticality = impact * risk_val

        # Reversibility: we define everything as reversible because of RollbackManager,
        # but higher risks reduce the confidence of complete reversibility.
        reversibility = 1.0 - (risk_val * 0.3)

        task_stub = {
            "risk": risk_val,
            "complexity": impact,
            "dependencies": decision_node.get("alternatives", [])
        }

        val_res = self.validator.validate_safety(task_stub)

        # Block if criticality is extremely high (>0.80) and fail probability is too high
        is_blocked = (criticality > 0.80 and val_res["failure_probability"] > 0.70)

        return {
            "criticality": round(criticality, 4),
            "reversibility": round(reversibility, 4),
            "failure_probability": val_res["failure_probability"],
            "safe": val_res["safe"] and not is_blocked,
            "reason": val_res["reason"] or ("Blocked due to excessive criticality" if is_blocked else "")
        }
