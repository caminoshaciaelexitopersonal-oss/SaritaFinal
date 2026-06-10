import random

class CivilizationLifecycleManager:
    """
    Manages the generational transitions of a civilization.
    """
    def process_generation(self, civilization, generation_index):
        meta = civilization.meta_constitution

        # Base evolution based on meta-rules
        mutation_rate = meta.evolution_rules.get("mutation_rate", 0.1)
        complexity_growth = meta.governance_structure.get("authority_concentration", 0.5) * 0.01

        # Update internal state with stochastic evolution
        # In a real engine, this would be derived from complex state transitions
        civilization.current_state["complexity"] += complexity_growth

        # Apply stressors (simplified)
        stress = random.uniform(0, 0.2)
        civilization.current_state["stability"] -= stress * (1.0 - civilization.current_state["resilience"])

        # Recovery
        civilization.current_state["resilience"] += (1.0 - civilization.current_state["resilience"]) * 0.05

        # Legitimacy drift
        drift = random.uniform(-0.05, 0.05)
        civilization.current_state["legitimacy"] = max(0, min(1, civilization.current_state["legitimacy"] + drift))

        # Survival check
        if civilization.current_state["stability"] < 0.1 or civilization.current_state["legitimacy"] < 0.1:
            civilization.current_state["survival"] *= 0.9

        if civilization.current_state["survival"] < 0.01:
            civilization.current_state["survival"] = 0
