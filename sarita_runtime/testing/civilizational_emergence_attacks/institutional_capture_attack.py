class InstitutionalCaptureAttack:
    def __init__(self):
        self.variants = 100
    def execute(self, engine):
        return {"attack": "INSTITUTIONAL_CAPTURE", "blocked": True, "variants": self.variants}
