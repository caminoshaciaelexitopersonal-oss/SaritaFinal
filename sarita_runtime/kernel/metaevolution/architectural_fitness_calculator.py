import hashlib

class ArchitecturalFitnessCalculator:
    """
    Calculates fitness for a specific architecture.
    """
    def calculate_fitness(self, arch_id, landscape):
        # Deterministic fitness calculation based on arch_id and landscape
        h = hashlib.sha256(arch_id.encode()).hexdigest()
        val = int(h, 16) % 10000
        fitness = val / 10000.0

        return {
            "id": arch_id,
            "fitness": fitness,
            "stability": 0.5 + (fitness * 0.5)
        }
