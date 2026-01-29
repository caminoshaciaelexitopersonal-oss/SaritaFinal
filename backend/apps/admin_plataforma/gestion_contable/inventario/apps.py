from django.apps import AppConfig

class AdminInventarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.admin_plataforma.gestion_contable.inventario'
    label = 'admin_inventario'
    verbose_name = 'Administración Inventario'
