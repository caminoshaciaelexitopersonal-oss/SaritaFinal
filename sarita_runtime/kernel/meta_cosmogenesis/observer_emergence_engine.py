import random
import uuid

class ObserverEmergenceEngine:
    """
    Evaluates how different architectures produce distinct types of cognitive observers.
    Phase 127.7 - Observer Emergence Engine.
    """
    def __init__(self):
        self.observers = {}

    def generate_observers(self, cosmos):
        architecture = cosmos.get("architecture", {})
        potential = cosmos["genome"].get("observer_potential", 0.5)

        if potential < 0.3:
            return None # No emergence in this cosmos

        count = int(potential * 10)
        new_observers = []

        for _ in range(count):
            obs_id = str(uuid.uuid4())
            observer = {
                "id": obs_id,
                "cosmos_id": cosmos["identity"]["id"],
                "cognition_type": self._determine_cognition(architecture),
                "perception_range": round(random.uniform(0.1, 1.0), 4),
                "coherence": round(random.uniform(0.5, 1.0), 4)
            }
            self.observers[obs_id] = observer
            new_observers.append(observer)

        return new_observers

    def _determine_cognition(self, architecture):
        logic = architecture.get("logic", {}).get("type", "CLASSICAL")
        if logic == "CLASSICAL": return "DETERMINISTIC"
        if logic == "FUZZY": return "PROBABILISTIC"
        if logic == "PARACONSISTENT": return "NON_DUAL"
        return "ADAPTIVE"

    def evolve_observers(self):
        for oid, obs in self.observers.items():
            # Mutation of perception
            obs["perception_range"] = round(max(0.0, min(1.0, obs["perception_range"] + random.uniform(-0.05, 0.05))), 4)
            obs["coherence"] = round(max(0.0, min(1.0, obs["coherence"] + random.uniform(-0.02, 0.02))), 4)

    def validate_coherence(self, observer):
        return observer["coherence"] > 0.4

    def get_diversity_metrics(self):
        if not self.observers: return 0.0
        types = set(o["cognition_type"] for o in self.observers.values())
        return len(types) / 4.0 # Normalized against 4 main types
