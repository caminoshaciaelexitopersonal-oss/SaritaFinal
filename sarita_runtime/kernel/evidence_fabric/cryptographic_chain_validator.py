import hashlib

class CryptographicChainValidator:
    """
    Validates the cryptographic sovereignty of the causal chain.
    """
    @staticmethod
    def validate_hash_non_reusability(graph):
        vertices = graph.get_all_vertices()
        hashes = [v.vertex_hash for v in vertices]
        if len(hashes) != len(set(hashes)):
            return False, "Hash reuse detected"
        return True, "HASH_UNIQUENESS_VERIFIED"

    @staticmethod
    def validate_ledger_chain(ledger):
        return ledger.verify_integrity()
