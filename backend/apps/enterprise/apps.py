from django.apps import AppConfig

class EnterpriseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.enterprise'
    verbose_name = 'Enterprise Operating System Core'

    def ready(self):
        # Registration of Enterprise-level listeners
        from .application.policy_service import PolicyEvaluationService
        PolicyEvaluationService.register_handlers()
