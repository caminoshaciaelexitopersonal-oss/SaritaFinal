from .architecture_genome_builder import ArchitectureGenomeBuilder
from .architecture_identity_generator import ArchitectureIdentityGenerator
import time

class ArchitectureBirthEngine:
    """
    Orchestrates the birth of new architectures.
    """
    def __init__(self):
        self.genome_builder = ArchitectureGenomeBuilder()
        self.identity_gen = ArchitectureIdentityGenerator()

    def initiate_birth(self, parent=None):
        parent_id = parent["identity"]["id"] if parent else None
        parent_genome = parent["genome"] if parent else None

        identity = self.identity_gen.generate_id(parent_id)
        genome = self.genome_builder.build_genome(parent_genome)

        return {
            "identity": identity,
            "genome": genome,
            "generation": (parent["generation"] + 1) if parent else 0,
            "born_at": time.time(),
            "status": "ACTIVE"
        }
