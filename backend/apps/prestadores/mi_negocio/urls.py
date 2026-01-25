from django.urls import path, include
from api.views import PlaceholderView

app_name = 'mi_negocio'

urlpatterns = [
    # Módulos principales con su propio enrutamiento interno
    path('operativa/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.urls')),
    path('comercial/', include('apps.prestadores.mi_negocio.gestion_comercial.urls')),
    path('financiera/', include('apps.prestadores.mi_negocio.gestion_financiera.urls')),

    # Módulo contable es una agrupación de otros módulos
    path('contable/contabilidad/', include('apps.prestadores.mi_negocio.gestion_contable.contabilidad.urls')),
    path('contable/activos-fijos/', include('apps.prestadores.mi_negocio.gestion_contable.activos_fijos.urls')),

    # Gestión Archivística
    path('archivistica/', include('apps.prestadores.mi_negocio.gestion_archivistica.urls')),
]
