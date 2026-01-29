from django.apps import AppConfig

class PresupuestoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.admin_plataforma.gestion_contable.presupuesto'

    def ready(self):
        import apps.admin_plataforma.gestion_contable.presupuesto.signals
