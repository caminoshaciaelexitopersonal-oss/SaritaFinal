from django.apps import AppConfig

class PrestadoresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.prestadores'

    def ready(self):
        # Asegurar descubrimiento de modelos en la nueva estructura operativa turística
        from .mi_negocio import operativa_turistica
