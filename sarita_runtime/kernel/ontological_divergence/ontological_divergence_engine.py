from .concept_creation_engine import ConceptCreationEngine
from .ontology_mutation_engine import OntologyMutationEngine
from .reality_model_generator import RealityModelGenerator
from .category_emergence_tracker import CategoryEmergenceTracker
from .ontological_conflict_resolver import OntologicalConflictResolver

class OntologicalDivergenceEngine:
    def __init__(self):
        self.concept_engine = ConceptCreationEngine()
        self.mutator = OntologyMutationEngine()
        self.reality_gen = RealityModelGenerator()
        self.tracker = CategoryEmergenceTracker()
        self.resolver = OntologicalConflictResolver()
        self.universe_ontologies = {} # universe_id -> concepts

    def evolve_ontology(self, universe_id):
        if universe_id not in self.universe_ontologies:
            self.universe_ontologies[universe_id] = {}
            # Initial concepts
            for _ in range(5):
                c = self.concept_engine.create_concept(universe_id)
                self.universe_ontologies[universe_id][c["id"]] = c

        # Mutation
        self.universe_ontologies[universe_id] = self.mutator.mutate_ontology(self.universe_ontologies[universe_id])

        # New concept emergence
        if len(self.universe_ontologies[universe_id]) < 50:
            c = self.concept_engine.create_concept(universe_id)
            self.universe_ontologies[universe_id][c["id"]] = c

        return self.reality_gen.generate_model(universe_id, self.universe_ontologies[universe_id])

    def get_divergence_metrics(self):
        # Calculate cross-universe conflict/divergence
        univ_ids = list(self.universe_ontologies.keys())
        if len(univ_ids) < 2:
            return 0.0

        total_conflict = 0.0
        count = 0
        for i in range(len(univ_ids)):
            for j in range(i + 1, len(univ_ids)):
                res = self.resolver.resolve_conflict(
                    self.universe_ontologies[univ_ids[i]],
                    self.universe_ontologies[univ_ids[j]]
                )
                total_conflict += res["conflict_intensity"]
                count += 1
        return round(total_conflict / count, 4) if count > 0 else 0.0
