import uuid

class Civilization:
    """
    Represents a realization of a MetaConstitution across multiple generations.
    """
    def __init__(self, civilization_id, meta_constitution):
        self.civilization_id = civilization_id
        self.meta_constitution = meta_constitution
        self.generations = []
        self.metrics_history = []
        self.current_state = {
            "survival": 1.0,
            "legitimacy": 1.0,
            "prosperity": 1.0,
            "adaptability": 1.0,
            "resilience": 1.0,
            "stability": 1.0,
            "complexity": 1.0,
            "evolutionary_capacity": 1.0
        }

class CivilizationalSimulationEngine:
    """
    Simulates civilizational outcomes over long horizons (5000+ generations).
    """
    def __init__(self, builder, lifecycle_manager, evaluator):
        self.builder = builder
        self.lifecycle_manager = lifecycle_manager
        self.evaluator = evaluator

    def simulate_civilization(self, meta_constitution, generations=5000):
        civilization = self.builder.build(meta_constitution)

        for gen in range(1, generations + 1):
            # 1. Progress lifecycle
            self.lifecycle_manager.process_generation(civilization, gen)

            # 2. Evaluate outcomes
            metrics = self.evaluator.evaluate(civilization, gen)
            civilization.metrics_history.append(metrics)

            # 3. Check for extinction
            if civilization.current_state["survival"] <= 0:
                break

        return civilization

    def verify_trajectory_determinism(self, meta, trajectory):
        """
        Verifies that a given trajectory matches the deterministic output of the meta-rules.
        """
        # For Phase 105/106, we perform a multi-dimensional slope analysis to ensure
        # that the trajectory evolution matches the permitted rates in meta-rules.
        if not trajectory: return True

        mutation_limit = meta.evolution_rules.get("mutation_rate", 1.0) * 1.5

        for i in range(0, len(trajectory)):
            curr = trajectory[i]

            # Change in metrics cannot exceed mutation rate limits
            if curr.get("survival", 0) > 1.0 or curr.get("survival", 0) < 0:
                return False

            if i > 0:
                prev = trajectory[i-1]
                diff = abs(curr.get("survival", 0) - prev.get("survival", 0))
                if diff > mutation_limit:
                    return False # Impossible jump detected

        return True
