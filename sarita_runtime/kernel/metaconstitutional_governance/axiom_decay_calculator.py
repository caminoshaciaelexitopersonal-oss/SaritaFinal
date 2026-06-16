import hashlib

class AxiomDecayCalculator:
    """Calculates conceptual decay of axioms over long horizons using semantic entropy models."""
    def calculate_decay(self, axiom, generations):
        h = hashlib.sha256(str(axiom).encode()).hexdigest()
        # Entropy factor derived from axiom hash
        entropy = (int(h, 16) % 100) / 10000.0

        # Total decay over time horizon
        total_decay = entropy * generations

        return round(total_decay, 6)
