from django.apps import AppConfig


class SaritaAgentsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.sarita_agents"

    def ready(self):
        try:
            from .agents.general.sarita.coroneles.comercial.registration import register_commercial_hierarchy
            register_commercial_hierarchy()
        except ImportError:
            pass
