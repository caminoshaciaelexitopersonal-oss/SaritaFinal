"""
Django settings for puerto_gaitan_turismo project.
"""

import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar variables de entorno desde .env (para desarrollo local).
load_dotenv()

# --- Configuración de Seguridad y Entorno ---

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure--20v8f1jb-!a8l@l9-lnfqiebalcvq8rut^mj8@_m-uso36uop"
)

FIELD_ENCRYPTION_KEY = os.environ.get(
    "DJANGO_FIELD_ENCRYPTION_KEY",
    "pU4Wtwp-25i8a5v9M4wVw2H6jP5a_X-m3Nq8y7bK_cE="
).encode()

DEBUG = True

ALLOWED_HOSTS_str = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1,.localhost,testserver")
ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS_str.split(",")]

# --- CSRF y Seguridad ---
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    # Terceros
    "rest_framework",
    "rest_framework.authtoken",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.mfa",
    "dj_rest_auth",
    "corsheaders",
    "drf_spectacular",
    "anymail",
    "django_filters",
    "modeltranslation",
    # Mis Apps
    "api.apps.ApiConfig",
    "apps.core_erp.apps.CoreErpConfig",
    "apps.domain_business.apps.DomainBusinessConfig",
    "apps.prestadores.apps.PrestadoresConfig",

    # Módulos de "Mi Negocio"
    "apps.prestadores.mi_negocio.gestion_comercial.apps.GestionComercialConfig",
    "apps.prestadores.mi_negocio.gestion_financiera.apps.GestionFinancieraConfig",
    "apps.prestadores.mi_negocio.gestion_contable.empresa.apps.EmpresaConfig",
    "apps.prestadores.mi_negocio.gestion_contable.nomina.apps.NominaConfig",
    "apps.prestadores.mi_negocio.gestion_contable.cierres.apps.CierresConfig",

    # Submódulos de Contabilidad
    "apps.prestadores.mi_negocio.gestion_contable.activos_fijos.apps.ActivosFijosConfig",
    # "apps.prestadores.mi_negocio.gestion_contable.presupuesto.apps.PresupuestoConfig",
    "apps.prestadores.mi_negocio.gestion_contable.compras.apps.ComprasConfig",
    "apps.prestadores.mi_negocio.gestion_contable.contabilidad.apps.ContabilidadConfig",
    "apps.prestadores.mi_negocio.gestion_contable.inventario.apps.InventarioConfig",
    # "apps.prestadores.mi_negocio.gestion_contable.nomina.apps.NominaConfig",
    # "apps.prestadores.mi_negocio.gestion_contable.proyectos.apps.ProyectosConfig",

    # Módulos de "Mi Negocio" - Implementados
    "apps.prestadores.mi_negocio.facturacion.apps.FacturacionConfig", # Stub para F19
    # Nota: 'mi_negocio' es un módulo paraguas, no una app instalable.
    # Las apps de gestión_operativa ya están contenidas en 'prestadores'.
    "apps.companies.apps.CompaniesConfig",
    "apps.audit.apps.AuditConfig",
    "apps.prestadores.mi_negocio.gestion_archivistica.apps.GestionArchivisticaConfig",
    "apps.prestadores.mi_negocio.gestion_operativa.sg_sst.apps.SgsstConfig",

    # App para el panel de administración de la plataforma
    "apps.admin_plataforma.apps.AdminPlataformaConfig",
    "apps.admin_plataforma.gestion_financiera.apps.AdminGestionFinancieraConfig",
    "apps.admin_plataforma.gestion_archivistica.apps.AdminGestionArchivisticaConfig",
    "apps.admin_plataforma.gestion_contable.contabilidad.apps.AdminContabilidadConfig",
    "apps.admin_plataforma.gestion_contable.inventario.apps.AdminInventoryConfig",
    "apps.admin_plataforma.gestion_contable.compras.apps.AdminProcurementConfig",
    "apps.admin_plataforma.gestion_contable.activos_fijos.apps.AdminFixedAssetsConfig",
    "apps.admin_plataforma.gestion_contable.nomina.apps.AdminPayrollConfig",
    "apps.admin_plataforma.gestion_contable.empresa.apps.AdminCompanyConfig",
    "apps.admin_plataforma.gestion_contable.presupuesto.apps.AdminBudgetConfig",
    "apps.admin_plataforma.gestion_contable.proyectos.apps.AdminProjectsConfig",
    "apps.admin_plataforma.gestion_operativa.apps.AdminGestionOperativaConfig",
    "apps.comercial.apps.ComercialConfig",
    "apps.admin_control_tower.apps.AdminControlTowerConfig",
    "apps.control_tower.apps.ControlTowerConfig",
    "apps.enterprise.apps.EnterpriseConfig",
    "apps.global_holding.apps.GlobalHoldingConfig",
    "apps.capital_markets.apps.CapitalMarketsConfig",
    "apps.tokenization.apps.TokenizationConfig",
    "apps.global_orchestration.apps.GlobalOrchestrationConfig",
    "apps.institutional_layer.apps.InstitutionalLayerConfig",
    "apps.commercial_engine.apps.CommercialEngineConfig",
    "apps.usage_billing.apps.UsageBillingConfig",
    "apps.treasury_automation.apps.TreasuryAutomationConfig",
    "apps.treasury.apps.TreasuryConfig",
    "apps.capital_markets_layer.apps.CapitalMarketsLayerConfig",

    "apps.sadi_agent.apps.SadiAgentConfig",
    "apps.sarita_agents.apps.SaritaAgentsConfig",

    "apps.web_funnel.apps.WebFunnelConfig",
    "apps.decision_intelligence.apps.DecisionIntelligenceConfig",
    "apps.ecosystem_optimization.apps.EcosystemOptimizationConfig",
    "apps.finanzas.apps.FinanzasConfig",
    "apps.defense_predictive.apps.DefensePredictiveConfig",
    "apps.defense_deception.apps.DefenseDeceptionConfig",
    "apps.international_interop.apps.InternationalInteropConfig",
    "apps.peace_net.apps.PeaceNetConfig",
    "apps.operational_treaties.apps.OperationalTreatiesConfig",
    "apps.governance_live.apps.GovernanceLiveConfig",
    "apps.operational_intelligence.apps.OperationalIntelligenceConfig",
    "apps.autonomous_operations.apps.AutonomousOperationsConfig",
    "apps.corporate_structure.apps.CorporateStructureConfig",
    "apps.capital_architecture.apps.CapitalArchitectureConfig",
    "apps.strategic_treasury.apps.StrategicTreasuryConfig",
    "apps.expansion_engine.apps.ExpansionEngineConfig",
    "apps.economic_ecosystem.apps.EconomicEcosystemConfig",
    "apps.sovereign_infrastructure.apps.SovereignInfrastructureConfig",
    "apps.meta_economic_network.apps.MetaEconomicNetworkConfig",
    "apps.state_integration.apps.StateIntegrationConfig",
    "apps.transnational_governance.apps.TransnationalGovernanceConfig",
    "legacy_custody.apps.LegacyCustodyConfig",

    # "apps.downloads.apps.DownloadsConfig",

    "apps.cart.apps.CartConfig",
    "apps.orders.apps.OrdersConfig",
    "apps.payments.apps.PaymentsConfig",
    "apps.wallet.apps.WalletConfig",
    "apps.delivery.apps.DeliveryConfig",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "api.middleware.entity_middleware.EntityMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "apps.common.security_hardening.SecurityHardeningMiddleware",
    "apps.defense_deception.middleware.DeceptionMiddleware",
    "apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.permissions.TenantMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "puerto_gaitan_turismo.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "puerto_gaitan_turismo.wsgi.application"

# Database
# ------------------------------------------------------------------------
# Usa DATABASE_URL desde .env
# Formato: postgresql://USER:PASSWORD@HOST:PORT/DBNAME
# ------------------------------------------------------------------------
# --- Configuración Multibase (Fase 18: Aislamiento de Dominios) ---
if "DATABASE_URL" in os.environ:
    DATABASES = {
        "default": dj_database_url.config(conn_max_age=600, ssl_require=False)
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        },
        "wallet_db": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "wallet.sqlite3",
        },
        "delivery_db": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "delivery.sqlite3",
        },
    }

DATABASE_ROUTERS = ["puerto_gaitan_turismo.routers.DatabaseRouter"]

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "es-co"
TIME_ZONE = "America/Bogota"
USE_I18N = True
USE_TZ = True

# Traducciones con modeltranslation
gettext = lambda s: s
LANGUAGES = (
    ("es", gettext("Español")),
    ("en", gettext("English")),
)
MODELTRANSLATION_DEFAULT_LANGUAGE = "es"
MODELTRANSLATION_PREPOPULATE_LANGUAGE = "es"

# Archivos estáticos y media
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Modelo de usuario personalizado
AUTH_USER_MODEL = "api.CustomUser"

# Requerido por dj-rest-auth y allauth
SITE_ID = 1

# --- Configuración de Terceros ---

# DJ-REST-AUTH & DJANGO-ALLAUTH
REST_AUTH = {
    "USER_DETAILS_SERIALIZER": "api.serializers.CustomUserDetailSerializer",
    'LOGIN_SERIALIZER': 'api.serializers.CustomLoginSerializer',
    'REGISTER_SERIALIZER': 'api.serializers.CustomRegisterSerializer',
    'TOKEN_SERIALIZER': 'api.serializers.CustomTokenSerializer',
}

ACCOUNT_LOGIN_METHODS = ['email']
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'none'  # 'mandatory' en producción
ACCOUNT_SIGNUP_FIELDS = ['email', 'password1']
ACCOUNT_ADAPTER = "allauth.account.adapter.DefaultAccountAdapter"

# CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

AUTHENTICATION_BACKENDS = [
    "allauth.account.auth_backends.AuthenticationBackend",
    "django.contrib.auth.backends.ModelBackend",
]

# MFA
MFA_ENABLED = True
ACCOUNT_LOGIN_ON_MFA_PASSWORD_VERIFIED = False

# DRF
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Sarita API - Mi Negocio',
    'DESCRIPTION': 'API para los módulos del panel "Mi Negocio"',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # Limitar la generación del esquema a las rutas de mi-negocio
    'URL_PATTERNS': [
        r'^/api/v1/mi-negocio/',
    ],
    # Excluir explícitamente las rutas de la API pública que tienen problemas
    'URL_PATTERNS_EXCLUDE': [
        r'^/api/',
    ]
}

# Email con anymail
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    DEFAULT_FROM_EMAIL = "noreply@puertogaitan.gov.co"
    ADMINS = [("Admin", "admin@example.com")]
else:
    EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
    ANYMAIL = {"SENDGRID_API_KEY": os.environ.get("SENDGRID_API_KEY")}
    DEFAULT_FROM_EMAIL = os.environ.get(
        "DEFAULT_FROM_EMAIL", "noreply@puertogaitan.gov.co"
    )
    ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL")
    if ADMIN_EMAIL:
        ADMINS = [("Admin", ADMIN_EMAIL)]
    else:
        ADMINS = []

# --- CELERY ---
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

CELERY_BEAT_SCHEDULE = {
    'notarize-batch-every-hour': {
        'task': 'notarize_pending_documents_batch',
        'schedule': 3600.0,  # Ejecutar cada hora
    },
}

# --- Blockchain ---
POLYGON_RPC_URL = os.environ.get("POLYGON_RPC_URL")
SIGNER_PRIVATE_KEY = os.environ.get("SIGNER_PRIVATE_KEY")
NOTARY_CONTRACT_ADDRESS = os.environ.get("NOTARY_CONTRACT_ADDRESS")
NOTARY_CONTRACT_ABI = os.environ.get("NOTARY_CONTRACT_ABI")

# --- Application Secrets ---
GLOBAL_ENCRYPTION_PEPPER = os.environ.get("GLOBAL_ENCRYPTION_PEPPER")

# --- AWS ---
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME")

# --- SADI Agent ---
SADI_AGENT_LLM_MODEL = os.environ.get("SADI_AGENT_LLM_MODEL", "gpt-4-turbo")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# --- Configuración de Logging ---
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
CELERY_TASK_ALWAYS_EAGER = True
