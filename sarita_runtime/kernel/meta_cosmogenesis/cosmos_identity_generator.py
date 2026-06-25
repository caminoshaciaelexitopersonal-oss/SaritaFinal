import uuid
import hashlib

class CosmosIdentityGenerator:
    """
    Generates unique identities and tracking lineage for new cosmos.
    """
    def generate_identity(self, parent_id=None):
        cosmos_id = str(uuid.uuid4())
        name = f"Cosmos-{cosmos_id[:8]}"

        identity = {
            "id": cosmos_id,
            "name": name,
            "parent_id": parent_id,
            "lineage_depth": 0,
            "lineage_hash": ""
        }

        if parent_id:
            # We would typically fetch parent depth but for now we increment
            # in the birth engine.
            pass

        identity["identity_proof"] = self._generate_proof(identity)
        return identity

    def _generate_proof(self, identity):
        data = f"{identity['id']}-{identity['parent_id']}"
        return hashlib.sha256(data.encode()).hexdigest()
