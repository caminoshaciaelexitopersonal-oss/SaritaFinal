import hashlib
import random

class ConceptCreationEngine:
    def __init__(self):
        self.concepts = {}

    def create_concept(self, universe_id, base_concept=None):
        seed = f"{universe_id}:{base_concept}:{random.random()}"
        concept_id = hashlib.sha256(seed.encode()).hexdigest()[:12]

        concept = {
            "id": concept_id,
            "universe_id": universe_id,
            "complexity": random.uniform(0.1, 0.9),
            "coherence": random.uniform(0.5, 1.0)
        }
        self.concepts[concept_id] = concept
        return concept
