import base64

class SecretsGovernor:
    def __init__(self):
        self._mock_vault = {
            "DB_PASS": "encoded_pass_123",
            "OPENAI_KEY": "sk-secret-xyz"
        }

    def get_secret(self, key, tenant_id=None):
        # In real scenario, calls HashiCorp Vault with tenant_id isolation
        secret = self._mock_vault.get(key)
        if not secret:
            raise Exception(f"Secret {key} not found.")
        print(f"Secret {key} retrieved for tenant {tenant_id}")
        return secret

    def rotate_secret(self, key, new_value):
        self._mock_vault[key] = new_value
        print(f"Secret {key} rotated successfully.")

if __name__ == "__main__":
    sg = SecretsGovernor()
    print(sg.get_secret("OPENAI_KEY", "tenant-1"))
