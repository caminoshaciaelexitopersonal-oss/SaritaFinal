class PrescriptionSpoofingAttack:
    """
    Attempts to spoof a certified status for an unverified recommendation.
    """
    def __init__(self, validation_engine):
        self.validation_engine = validation_engine

    def execute(self):
        rogue_prescription = {"id": "P-ROGUE", "cause": None} # Missing mandatory field

        audit = self.validation_engine.validate_and_certify(rogue_prescription)

        assert audit["status"] == "REJECTED", "Attack failed: Unverified prescription was spoofed as certified!"
        return True
