class VerificationLineageLedger:
    """
    Registers the 'who verified who' lineage to prevent circular or recursive trust loops.
    """
    def __init__(self):
        self.lineage = []

    def register_verification(self, verifier_id: str, subject_id: str, verdict: bool):
        self.lineage.append({
            "verifier": verifier_id,
            "subject": subject_id,
            "verdict": verdict,
            "timestamp": time.time()
        })
import time
