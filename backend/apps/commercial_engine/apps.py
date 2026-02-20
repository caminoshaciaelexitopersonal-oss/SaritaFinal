from django.apps import AppConfig

class CommercialEngineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.commercial_engine'
    verbose_name = 'Commercial Engine (SaaS)'

    def ready(self):
        from .kpi_engine import KpiEngine
        KpiEngine.initialize()
