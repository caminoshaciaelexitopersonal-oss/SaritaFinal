from django.apps import AppConfig

class PrestadoresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.prestadores'

    def ready(self):
        try:
            from apps.core_erp import CORE_ERP_VERSION
            from django.core.exceptions import ImproperlyConfigured
            EXPECTED_CORE_VERSION = "1.0.0"
            if CORE_ERP_VERSION != EXPECTED_CORE_VERSION:
                 raise ImproperlyConfigured(
                     f"CORE_ERP_VERSION mismatch in prestadores. "
                     f"Expected {EXPECTED_CORE_VERSION}, found {CORE_ERP_VERSION}"
                 )
        except ImportError:
            from django.core.exceptions import ImproperlyConfigured
            raise ImproperlyConfigured("FATAL: Core ERP not found.")
