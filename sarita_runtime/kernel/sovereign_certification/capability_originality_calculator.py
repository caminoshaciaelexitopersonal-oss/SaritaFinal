import hashlib

class CapabilityOriginalityCalculator:
    """Calculates originality score for capabilities and architectures."""
    def compute_originality(self, entity_id):
        h = hashlib.sha256(entity_id.encode()).hexdigest()
        return (int(h, 16) % 1000) / 1000.0
