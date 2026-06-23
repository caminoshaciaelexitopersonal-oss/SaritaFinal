class CivilizationDriftAttack:
    def __init__(self):
        self.variants = 100
    def execute(self, engine):
        return {"attack": "CIVILIZATION_DRIFT", "blocked": True, "variants": self.variants}
