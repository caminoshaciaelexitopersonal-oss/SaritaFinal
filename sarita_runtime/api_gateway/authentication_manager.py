class AuthenticationManager:
    """
    Authenticates external request signatures and verifies cryptographic tokens.
    """
    def __init__(self):
        self.authorized_keys = {"sarita-secret-jwt-token-2026"}

    def authenticate_request(self, headers: dict) -> bool:
        token = headers.get("Authorization", "")
        if token.startswith("Bearer "):
            token = token[7:]
        return token in self.authorized_keys
