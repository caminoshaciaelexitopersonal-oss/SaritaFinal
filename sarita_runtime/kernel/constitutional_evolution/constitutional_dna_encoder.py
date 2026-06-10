import hashlib
import json

class ConstitutionalDNAEncoder:
    """
    Encodes a constitutional genome into a unique DNA hash for comparison.
    """
    def encode_genome(self, genome):
        # Deterministic JSON representation of genes
        encoded_data = json.dumps(genome.genes, sort_keys=True, default=str)
        dna_hash = hashlib.sha256(encoded_data.encode()).hexdigest()
        return dna_hash
