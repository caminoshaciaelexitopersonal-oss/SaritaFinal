class BiasDetector:
    """
    Analyzes historical experimental records and datasets to detect systemic bias or p-hacking tendencies.
    """
    def __init__(self):
        pass

    def detect_p_hacking(self, p_values: list) -> dict:
        if not p_values:
            return {"bias_detected": False, "p_hacking_risk": "NONE"}

        critical_zone = [p for p in p_values if 0.03 <= p < 0.05]
        safe_zone = [p for p in p_values if 0.0 <= p < 0.03]

        ratio = len(critical_zone) / max(1, len(safe_zone))

        if len(p_values) >= 5 and ratio > 1.5:
            return {
                "bias_detected": True,
                "p_hacking_risk": "HIGH",
                "message": "Excess of p-values near the 0.05 threshold indicates potential p-hacking."
            }

        return {
            "bias_detected": False,
            "p_hacking_risk": "LOW",
            "message": "p-values are naturally distributed."
        }
