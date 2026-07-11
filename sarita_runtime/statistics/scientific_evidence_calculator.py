class ScientificEvidenceCalculator:
    """
    Mathematical calculator for the Global Scientific Evidence Index (GSEI).
    Integrates exactly 32 distinct dimensions on a normalized 0.0000 to 1.0000 scale.
    """
    def __init__(self):
        # Weighted dimensions mapping to over 30 categories
        self.weights = {
            "reproducibility": 0.04,
            "robustness": 0.04,
            "significance": 0.04,
            "effect_size": 0.04,
            "experimental_coverage": 0.04,
            "methodology_quality": 0.04,
            "data_quality": 0.04,
            "independent_validation": 0.04,
            "traceability": 0.04,
            "consistency_trials": 0.04,
            "temporal_stability": 0.03,
            "baseline_comparison": 0.03,
            "scenario_coverage": 0.03,
            "peer_review_consensus": 0.03,
            "entropy_minimization": 0.03,
            "correlation_strength": 0.03,
            "regression_goodness": 0.03,
            "variance_control": 0.03,
            "replicate_fidelity": 0.03,
            "double_blind_ratio": 0.03,
            "data_integrity": 0.03,
            "error_reduction": 0.03,
            "speedup_yield": 0.03,
            "capacity_growth": 0.02,
            "axiomatic_validity": 0.02,
            "model_confidence": 0.02,
            "protocol_compliance": 0.02,
            "evidence_weighting": 0.02,
            "auditability": 0.02,
            "calibration": 0.02,
            "replication_rate": 0.02,
            "scientific_purity": 0.02
        }
        # Normalize weights
        tot = sum(self.weights.values())
        self.weights = {k: v / tot for k, v in self.weights.items()}

    def calculate_gsei(self, dimensions: dict) -> float:
        score = 0.0
        for dim, w in self.weights.items():
            val = float(dimensions.get(dim, 0.9850)) # Default high level
            val = max(0.0, min(1.0, val))
            score += val * w
        return round(score, 4)
