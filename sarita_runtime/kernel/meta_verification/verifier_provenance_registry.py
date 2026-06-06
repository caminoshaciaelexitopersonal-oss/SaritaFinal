import hashlib

class VerifierProvenanceRegistry:
    """
    Maintains a record of the origins and characteristics of each registered verifier.
    """
    def __init__(self):
        self.provenance_data = {} # verifier_id -> {origin, author, domain, implementation, language}

    def register_verifier(self, verifier_id: str, data: dict):
        required = ["origin", "author", "domain", "implementation", "language"]
        if not all(k in data for k in required):
            raise ValueError("Incomplete provenance data")

        self.provenance_data[verifier_id] = {
            **data,
            "fingerprint": hashlib.sha256(str(data).encode()).hexdigest()
        }

    def get_provenance(self, verifier_id: str):
        return self.provenance_data.get(verifier_id)
