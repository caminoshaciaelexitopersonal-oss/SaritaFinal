class StrategicCapitalRegistry:
    """
    Registry of "Strategic Capital" (Trust, Stability, Legitimacy).
    """
    def __init__(self):
        self.capital = {
            "TRUST": 100.0,
            "STABILITY": 100.0,
            "LEGITIMACY": 100.0
        }

    def update_capital(self, domain: str, delta: float):
        if domain in self.capital:
            self.capital[domain] += delta
            return self.capital[domain]
        return 0.0
