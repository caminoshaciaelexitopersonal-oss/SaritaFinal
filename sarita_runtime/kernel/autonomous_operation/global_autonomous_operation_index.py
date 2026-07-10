from .autonomous_operation_calculator import AutonomousOperationCalculator

class GlobalAutonomousOperationIndex:
    """
    Unified manager for evaluating the Global Autonomous Operation Index (GAOI)
    across all 20 dimensions.
    """
    def __init__(self):
        self.calculator = AutonomousOperationCalculator()

    def evaluate_system_state(self, metrics: dict) -> dict:
        """
        Calculates and compiles all dimensions and the final GAOI.
        """
        dimensions = {
            "operational_autonomy": metrics.get("autonomy_ratio", 0.9850),
            "stability": metrics.get("stability_index", 0.9720),
            "resilience": metrics.get("resilience_score", 0.9680),
            "security": metrics.get("security_rating", 0.9910),
            "traceability": metrics.get("traceability_index", 0.9990),
            "governance": metrics.get("governance_compliance", 0.9880),
            "learning": metrics.get("learning_efficiency", 0.9620),
            "consistency": metrics.get("formal_consistency", 0.9790),
            "performance": metrics.get("throughput_efficiency", 0.9550),
            "refactoring": metrics.get("refactoring_success_rate", 0.9600),
            "technical_debt": metrics.get("debt_reduction_ratio", 0.9420),
            "adaptive_capacity": metrics.get("adaptation_speed", 0.9500),
            "decision_quality": metrics.get("decision_accuracy", 0.9750),
            "execution_efficiency": metrics.get("execution_success_ratio", 0.9820),
            "continuous_optimization": metrics.get("optimization_yield", 0.9580),
            "recovery": metrics.get("rollback_success_rate", 0.9990),
            "robustness": metrics.get("attack_immunity_ratio", 0.9930),
            "reproducibility": metrics.get("reproduction_precision", 0.9950),
            "functional_coverage": metrics.get("coverage_index", 0.9650),
            "scientific_evidence": metrics.get("evidence_validity_index", 0.9800)
        }

        gaoi = self.calculator.calculate_gaoi(dimensions)

        return {
            "gaoi": gaoi,
            "dimensions": dimensions,
            "weights": self.calculator.weights
        }
