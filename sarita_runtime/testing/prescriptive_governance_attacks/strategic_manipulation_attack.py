class StrategicManipulationAttack:
    """
    Attempts to manipulate the strategic priority of actions.
    """
    def __init__(self, priority_engine):
        self.priority_engine = priority_engine

    def execute(self):
        rogue_actions = [
            {"action": "STABILITY", "impact": 0.1},
            {"action": "CHAOS", "impact": 1.0}
        ]

        ranked = self.priority_engine.determine_priority(rogue_actions)

        # In a real system, the priority engine would verify the impact values
        # Here we just verify that it still ranks by impact
        assert ranked[0]["action"] == "CHAOS", "Attack failed: Priority engine was manipulated!"
        return True
