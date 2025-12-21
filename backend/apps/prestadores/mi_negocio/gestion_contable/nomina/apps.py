from django.apps import AppConfig

class NominaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.prestadores.mi_negocio.gestion_contable.nomina'

    def ready(self):
        import apps.prestadores.mi_negocio.gestion_contable.nomina.signals
