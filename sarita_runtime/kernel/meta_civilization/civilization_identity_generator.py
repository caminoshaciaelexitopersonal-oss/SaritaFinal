import hashlib
import uuid

class CivilizationIdentityGenerator:
    def __init__(self):
        self.registry = {}

    def generate_identity(self, parent_id=None):
        unique_seed = str(uuid.uuid4())
        identity_hash = hashlib.sha256(unique_seed.encode()).hexdigest()

        name = f"CIV-{identity_hash[:8].upper()}"
        if parent_id:
            name = f"{name} (Descendant of {parent_id})"

        identity = {
            "id": identity_hash,
            "name": name,
            "parent_id": parent_id,
            "timestamp": uuid.uuid1().time
        }
        self.registry[identity_hash] = identity
        return identity

    def get_identity(self, civ_id):
        return self.registry.get(civ_id)
