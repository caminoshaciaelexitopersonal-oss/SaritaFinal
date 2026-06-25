import random

class OntologyMutationEngine:
    def mutate_ontology(self, concepts):
        mutated = concepts.copy()
        for c_id in mutated:
            if random.random() < 0.1:
                mutated[c_id]["complexity"] = round(max(0.0, min(1.0, mutated[c_id]["complexity"] + random.uniform(-0.1, 0.1))), 4)
        return mutated
