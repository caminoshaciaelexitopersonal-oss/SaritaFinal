# backend/apps/activos/apps.py
from django.apps import AppConfig

class ActivosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.activos'

    def ready(self):
        import apps.activos.signals
