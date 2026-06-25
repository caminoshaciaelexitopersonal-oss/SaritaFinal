import hashlib
import uuid

class UniverseIdentityGenerator:
    def __init__(self):
        self.registry = {}

    def generate_identity(self):
        unique_seed = str(uuid.uuid4())
        identity_hash = hashlib.sha256(unique_seed.encode()).hexdigest()

        name = f"UNIV-{identity_hash[:8].upper()}"
        identity = {
            "id": identity_hash,
            "name": name,
            "timestamp": uuid.uuid1().time
        }
        self.registry[identity_hash] = identity
        return identity
