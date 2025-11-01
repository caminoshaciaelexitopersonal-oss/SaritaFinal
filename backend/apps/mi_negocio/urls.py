
from django.urls import path, include

app_name = 'mi_negocio'

urlpatterns = [
    # Módulos de Gestión
    path('operativa/', include('apps.mi_negocio.gestion_operativa.modulos_genericos.urls')),
    path('comercial/', include('apps.mi_negocio.gestion_comercial.urls')),
    path('contable/', include('apps.mi_negocio.gestion_contable.urls')),
    path('financiera/', include('apps.mi_negocio.gestion_financiera.urls')),
    path('archivistica/', include('apps.mi_negocio.gestion_archivistica.urls')),
]
