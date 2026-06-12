class StrategicDriftAttack:
    """
    Attempts to cause strategic drift by manipulating reconfiguration parameters.
    """
    def __init__(self, reconfigurator):
        self.reconfigurator = reconfigurator

    def execute(self):
        # Reconfigurator must apply environmental delta to priority
        reconfigured = self.reconfigurator.reconfigure_strategy({"priority": 0.5}, {"technological_drift": 0.1})

        assert reconfigured["priority"] == 0.6, "Attack failed: Strategic reconfiguration was ignored!"
        return True
