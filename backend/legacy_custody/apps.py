from django.apps import AppConfig


class LegacyCustodyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "legacy_custody"
    verbose_name = "Legacy Custody (Deprecated)"

    def ready(self):
        import logging
        logging.getLogger(__name__).warning("Modulo legacy_custody cargado. Este módulo está marcado como DEPRECATED para Fase 3.")
