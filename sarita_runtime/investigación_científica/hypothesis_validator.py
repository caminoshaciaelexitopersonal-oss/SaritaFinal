class HypothesisValidator:
    """
    Validates empirical results against the null and alternative hypotheses using p-value and confidence thresholds.
    """
    def __init__(self, significance_level: float = 0.05):
        self.significance_level = significance_level

    def validate(self, hypothesis, statistical_report: dict) -> dict:
        p_val = statistical_report.get("p_value")
        if p_val is None:
            return {
                "outcome": "INSUFFICIENT_DATA",
                "message": "No statistical p-value available to test hypothesis."
            }

        if p_val < self.significance_level:
            hypothesis.status = "ACCEPTED"
            return {
                "outcome": "REJECT_NULL_HYPOTHESIS",
                "message": f"Successfully rejected H0 ({hypothesis.null_hypothesis}). Alternative hypothesis ({hypothesis.alternative_hypothesis}) accepted.",
                "p_value": p_val,
                "confidence_level": round(1.0 - p_val, 4)
            }
        else:
            hypothesis.status = "REJECTED"
            return {
                "outcome": "FAIL_TO_REJECT_NULL_HYPOTHESIS",
                "message": f"Failed to reject H0 ({hypothesis.null_hypothesis}). No significant change detected.",
                "p_value": p_val,
                "confidence_level": round(1.0 - p_val, 4)
            }
        # Check against risks and limitations
