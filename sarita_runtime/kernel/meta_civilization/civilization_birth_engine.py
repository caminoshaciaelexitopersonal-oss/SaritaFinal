from .civilization_identity_generator import CivilizationIdentityGenerator
from .civilization_genome_builder import CivilizationGenomeBuilder

class CivilizationBirthEngine:
    def __init__(self):
        self.identity_gen = CivilizationIdentityGenerator()
        self.genome_builder = CivilizationGenomeBuilder()
        self.active_civilizations = {}

    def birth_initial_civilization(self):
        identity = self.identity_gen.generate_identity()
        genome = self.genome_builder.build_genome()

        civ = {
            "identity": identity,
            "genome": genome,
            "status": "emerging",
            "age": 0
        }
        self.active_civilizations[identity["id"]] = civ
        return civ

    def birth_from_parent(self, parent_id):
        if parent_id not in self.active_civilizations:
            raise ValueError(f"Parent civilization {parent_id} not found.")

        parent = self.active_civilizations[parent_id]
        identity = self.identity_gen.generate_identity(parent_id=parent_id)
        genome = self.genome_builder.build_genome(parent_genome=parent["genome"])

        civ = {
            "identity": identity,
            "genome": genome,
            "status": "emerging",
            "age": 0
        }
        self.active_civilizations[identity["id"]] = civ
        return civ

    def get_civilization(self, civ_id):
        return self.active_civilizations.get(civ_id)

    def list_active(self):
        return list(self.active_civilizations.values())
