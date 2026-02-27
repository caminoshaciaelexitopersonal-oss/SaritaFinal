from django.apps import AppConfig

class CoreErpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core_erp'
    verbose_name = 'Core ERP Systemic'

    def ready(self):
        from .accounting.handlers import StandardAccountingHandlers
        StandardAccountingHandlers.register_all()

        # EOS Activation: Automated Consolidation
        from .consolidation.event_processor import ConsolidationEventProcessor
        ConsolidationEventProcessor.start_listening()
