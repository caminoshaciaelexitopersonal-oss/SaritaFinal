class CatastrophicChainAnalyzer:
    """
    Analyzes chains of events that lead to catastrophic extinction.
    """
    def analyze_chain(self, events: list):
        # Identify "unrecoverable" states
        for event in events:
            if event.get("impact") == "FATAL":
                return True, "Extinction chain detected: Fatal impact point."
        return False, "Chain is recoverable."
