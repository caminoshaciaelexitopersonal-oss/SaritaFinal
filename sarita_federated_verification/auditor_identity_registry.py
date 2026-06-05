import hashlib

class AuditorIdentityRegistry:
    """
    Maintains a registry of independent auditor identities and their public keys.
    """
    def __init__(self):
        self.identities = {} # auditor_id -> {public_key, domain, status}

    def register_auditor(self, auditor_id: str, public_key: str, domain: str):
        self.identities[auditor_id] = {
            "public_key": public_key,
            "domain": domain,
            "status": "active",
            "fingerprint": hashlib.sha256(public_key.encode()).hexdigest()
        }

    def get_auditor(self, auditor_id: str):
        return self.identities.get(auditor_id)

    def revoke_auditor(self, auditor_id: str):
        if auditor_id in self.identities:
            self.identities[auditor_id]["status"] = "revoked"
