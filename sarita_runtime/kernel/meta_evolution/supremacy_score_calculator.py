class SupremacyScoreCalculator:
    """
    Calculates the Global Civilizational Supremacy Index (GCSI).
    Scale: 0.0000 -> 1.0000
    """
    def calculate_gcsi(self, civilization):
        state = civilization.current_state

        # GCSI Submetrics
        lts = state.get("survival", 0)       # Long-Term Survival
        adapt = state.get("adaptability", 0) # Adaptation
        stab = state.get("stability", 0)     # Stability
        legit = state.get("legitimacy", 0)   # Legitimacy
        growth = state.get("prosperity", 0)   # Growth
        res = state.get("resilience", 0)     # Resilience
        ev_cap = state.get("evolutionary_capacity", 0) # Evolution Capacity

        # Sustainability (derived)
        sustainability = (lts + stab + res) / 3.0

        # Weighted sum for GCSI
        weights = {
            "lts": 0.20,
            "adapt": 0.15,
            "stab": 0.15,
            "legit": 0.15,
            "growth": 0.10,
            "res": 0.10,
            "ev_cap": 0.05,
            "sustainability": 0.10
        }

        gcsi = (
            lts * weights["lts"] +
            adapt * weights["adapt"] +
            stab * weights["stab"] +
            legit * weights["legit"] +
            growth * weights["growth"] +
            res * weights["res"] +
            ev_cap * weights["ev_cap"] +
            sustainability * weights["sustainability"]
        )

        return round(max(0.0000, min(1.0000, gcsi)), 4)
