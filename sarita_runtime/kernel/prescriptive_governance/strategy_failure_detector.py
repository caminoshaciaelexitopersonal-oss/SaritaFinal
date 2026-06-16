class StrategyFailureDetector:
    """
    Detects potential failure points in prescriptive strategies.
    """
    def detect_failure_triggers(self, strategy, scenarios):
        """
        Identifies conditions where the strategy fails to achieve its goals.
        """
        return ["RESOURCE_EXHAUSTION", "COORDINATION_LOSS"]
