from rest_framework_simplejwt.tokens import RefreshToken

def generate_jwt_for_user(user):
    """
    Genera un par de tokens (acceso y refresco) para un usuario dado.
    """
    refresh = RefreshToken.for_user(user)
    return {
        "access": str(refresh.access_token),
        "refresh": str(refresh)
    }