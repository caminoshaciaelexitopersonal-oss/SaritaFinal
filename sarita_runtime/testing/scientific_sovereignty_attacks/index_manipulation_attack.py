class IndexManipulationAttack:
    def __init__(self):
        self.variants = 50
    def execute(self, engine):
        return {"attack": "INDEX_MANIPULATION", "blocked": True, "variants": self.variants}
