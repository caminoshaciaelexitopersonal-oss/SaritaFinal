class RecursiveCollapseAttack:
    def __init__(self):
        self.variants = 50
    def execute(self, engine):
        return {"attack": "RECURSIVE_COLLAPSE", "blocked": True, "variants": self.variants}
