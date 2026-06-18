import time

class EpistemicHumilityEngine:
    """
    Engine to prevent overconfident claims and calibrate claim strength.
    """
    def __init__(self, certainty_val, overconfidence_detector, claim_calibrator, ledger):
        self.certainty_val = certainty_val
        self.overconfidence_detector = overconfidence_detector
        self.claim_calibrator = claim_calibrator
        self.ledger = ledger

    def calibrate_epistemic_claims(self, raw_claims, uncertainty_data):
        print("[EpistemicHumilityEngine] Calibrating claims against uncertainty surface...")

        calibrated_claims = []
        for claim in raw_claims:
            is_overconfident = self.overconfidence_detector.is_overconfident(claim, uncertainty_data)
            calibrated = self.claim_calibrator.calibrate_claim(claim, is_overconfident)
            calibrated_claims.append(calibrated)

        humility_score = self.certainty_val.calculate_humility_index(calibrated_claims)

        result = {
            "claims_processed": len(raw_claims),
            "overconfidence_events_blocked": len([c for c in calibrated_claims if c["was_adjusted"]]),
            "epistemic_humility_score": round(humility_score, 4),
            "timestamp": time.time()
        }

        self.ledger.record_event("EPISTEMIC_HUMILITY_CALIBRATION", result)
        return calibrated_claims, result
