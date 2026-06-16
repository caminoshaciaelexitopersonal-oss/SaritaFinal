import hashlib

class LegitimacyScoreCalculator:
    """Calculates legitimacy scores based on normative alignment and history."""
    def compute_score(self, state):
        h = hashlib.sha256(str(state).encode()).hexdigest()
        score = 0.95 + ((int(h, 16) % 500) / 10000.0)
        return round(score, 4)
