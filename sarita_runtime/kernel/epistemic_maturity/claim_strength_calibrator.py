class ClaimStrengthCalibrator:
    """Calibrates claim strength to align with actual uncertainty."""
    def calibrate_claim(self, claim, is_overconfident):
        if is_overconfident:
            return {"claim": claim["id"], "was_adjusted": True, "new_confidence": 0.85}
        return {"claim": claim["id"], "was_adjusted": False, "new_confidence": claim["confidence"]}
