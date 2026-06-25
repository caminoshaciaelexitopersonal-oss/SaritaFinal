from .universe_identity_generator import UniverseIdentityGenerator
from .evolutionary_law_builder import EvolutionaryLawBuilder
from .universe_genome_builder import UniverseGenomeBuilder

class UniverseBirthEngine:
    def __init__(self):
        self.identity_gen = UniverseIdentityGenerator()
        self.law_builder = EvolutionaryLawBuilder()
        self.genome_builder = UniverseGenomeBuilder()
        self.active_universes = {}

    def birth_universe(self, parent_laws=None):
        identity = self.identity_gen.generate_identity()
        laws = self.law_builder.build_laws(parent_laws=parent_laws)
        genome = self.genome_builder.build_genome(laws)

        universe = {
            "identity": identity,
            "laws": laws,
            "genome": genome,
            "age": 0,
            "status": "active"
        }
        self.active_universes[identity["id"]] = universe
        return universe
