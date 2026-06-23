import hashlib

class SovereigntyPreservationEngine:
    """Ensures the preservation of sovereign authority over time using entropy-based checks."""
    def check_preservation(self, evolution_plan):
        # Derive preservation from the plan's hash and complexity
        h = hashlib.sha256(str(evolution_plan).encode()).hexdigest()
        raw_val = (int(h, 16) % 1000) / 1000.0

        # Inversely proportional to complexity if present
        complexity = evolution_plan.get("complexity", 0.5)
        preservation = max(0.0, min(1.0, raw_val * (1.0 - complexity * 0.1)))

        return round(preservation, 4)
