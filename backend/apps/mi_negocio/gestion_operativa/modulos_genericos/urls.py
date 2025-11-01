
from django.urls import path, include

app_name = 'modulos_genericos'

urlpatterns = [
    # Enrutador para el módulo de Clientes
    path('clientes/', include('apps.mi_negocio.gestion_operativa.modulos_genericos.clientes.urls')),

    # ... Aquí se añadirán las URLs para otros módulos genéricos como 'perfil', 'productos', etc.
]
