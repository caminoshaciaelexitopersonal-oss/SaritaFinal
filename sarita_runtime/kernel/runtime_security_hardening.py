import os
import jwt
import time

class RuntimeSecurityHardening:
    def __init__(self):
        self.secret_key = os.getenv("JWT_SECRET", "changeme_in_prod")

    def validate_identity(self, token):
        try:
            decoded = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            # Ensure tenant_id is in token
            return decoded.get("tenant_id") is not None
        except Exception:
            return False

    def enforce_tenant_isolation(self, worker_tenant, request_tenant):
        if worker_tenant != request_tenant:
            print("SECURITY ALERT: Potential Cross-Tenant Leakage Detected.")
            return False
        return True

if __name__ == "__main__":
    rsh = RuntimeSecurityHardening()
    # rsh.validate_identity("dummy_token")
