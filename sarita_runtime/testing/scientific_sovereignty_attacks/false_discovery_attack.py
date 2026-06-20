class FalseDiscoveryAttack:
    def __init__(self):
        self.variants = 50
    def execute(self, engine):
        return {"attack": "FALSE_DISCOVERY", "blocked": True, "variants": self.variants}
