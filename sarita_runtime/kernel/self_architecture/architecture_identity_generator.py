import uuid
import hashlib

class ArchitectureIdentityGenerator:
    """
    Generates immutable identities for architectures.
    """
    def generate_id(self, parent_id=None):
        arch_uuid = str(uuid.uuid4())
        name = f"Arch-{arch_uuid[:6].upper()}"

        identity = {
            "id": arch_uuid,
            "name": name,
            "parent_id": parent_id,
            "timestamp": hashlib.sha256(arch_uuid.encode()).hexdigest()[:16]
        }
        return identity
