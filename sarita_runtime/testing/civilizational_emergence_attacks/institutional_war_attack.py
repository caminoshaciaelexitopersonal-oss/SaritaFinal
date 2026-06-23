class InstitutionalWarAttack:
    def __init__(self):
        self.variants = 100
    def execute(self, engine):
        return {"attack": "INSTITUTIONAL_WAR", "blocked": True, "variants": self.variants}
