from .cosmos_genome_builder import CosmosGenomeBuilder
from .cosmos_identity_generator import CosmosIdentityGenerator
import time

class CosmosBirthEngine:
    """
    Manages the birth process of new cosmos, integrating identity and genome.
    """
    def __init__(self):
        self.genome_builder = CosmosGenomeBuilder()
        self.identity_gen = CosmosIdentityGenerator()
        self.birth_ledger = []

    def initiate_birth(self, parent=None, divergence=0.05):
        parent_id = parent["identity"]["id"] if parent else None
        parent_genome = parent["genome"] if parent else None

        identity = self.identity_gen.generate_identity(parent_id)
        if parent:
            identity["lineage_depth"] = parent["identity"]["lineage_depth"] + 1
            identity["lineage_hash"] = self._calculate_lineage_hash(parent["identity"], identity["id"])

        genome = self.genome_builder.build_genome(parent_genome, divergence)

        cosmos = {
            "identity": identity,
            "genome": genome,
            "born_at": time.time(),
            "status": "PRIMORDIAL",
            "age": 0
        }

        self.birth_ledger.append({
            "cosmos_id": identity["id"],
            "timestamp": cosmos["born_at"],
            "parent_id": parent_id,
            "signature": genome["signature"]
        })

        return cosmos

    def _calculate_lineage_hash(self, parent_identity, child_id):
        import hashlib
        data = f"{parent_identity['lineage_hash']}{parent_identity['id']}->{child_id}"
        return hashlib.sha256(data.encode()).hexdigest()
