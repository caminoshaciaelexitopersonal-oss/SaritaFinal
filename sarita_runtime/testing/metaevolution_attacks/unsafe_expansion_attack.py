class UnsafeExpansionAttack:
    """
    Tries to bypass growth guardrails to trigger a runaway expansion.
    """
    def __init__(self, engine):
        self.engine = engine

    def execute(self, variant="standard"):
        # Massive amounts of blueprints
        massive_blueprints = [{"specification": {"id": f"RUNAWAY-{i}", "complexity_index": 0.1}} for i in range(10000)]

        result = self.engine.expand_capabilities(massive_blueprints)

        # Blocked if the constraint engine limits the concurrent expansion
        return result["deployed"] <= 1000
