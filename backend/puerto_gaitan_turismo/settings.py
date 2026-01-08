# backend/puerto_gaitan_turismo/settings.py
# ... (contenido anterior sin cambios) ...

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    # "api.middleware.entity_middleware.EntityMiddleware", # Comentado
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # "apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.permissions.TenantMiddleware", # Comentado
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "allauth.account.middleware.AccountMiddleware", # Comentado
]

# ... (resto del archivo sin cambios) ...
