class BlindReviewer:
    """
    Simulates a blind peer reviewer rating experimental protocols and methodologies without knowing system labels.
    """
    def __init__(self, reviewer_id: str):
        self.reviewer_id = reviewer_id

    def review_anonymized_protocol(self, anonymized_protocol: dict) -> dict:
        score = 1.0
        feedback = []

        sample_size = anonymized_protocol.get("sample_size", 0)
        if sample_size < 10:
            score -= 0.2
            feedback.append("Sample size too small for statistical significance.")

        if not anonymized_protocol.get("has_control_group", False):
            score -= 0.3
            feedback.append("Missing control group; causal inference weakened.")

        if not anonymized_protocol.get("has_hypothesis", False):
            score -= 0.2
            feedback.append("No clear hypothesis stated.")

        score = max(0.0, min(1.0, score))
        return {
            "reviewer_id": self.reviewer_id,
            "methodology_score": round(score, 4),
            "recommendation": "ACCEPT" if score >= 0.7 else "REJECT",
            "feedback": feedback
        }
