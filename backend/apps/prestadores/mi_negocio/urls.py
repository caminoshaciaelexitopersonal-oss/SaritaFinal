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
    # path('contable/compras/', include('apps.prestadores.mi_negocio.gestion_contable.compras.urls')),
    # path('contable/inventario/', include('apps.prestadores.mi_negocio.gestion_contable.inventario.urls')),
    # path('contable/nomina/', include('apps.prestadores.mi_negocio.gestion_contable.nomina.urls')),
    # path('contable/cierres/', include('apps.prestadores.mi_negocio.gestion_contable.cierres.urls')),
    # path('contable/reportes/', include('apps.prestadores.mi_negocio.gestion_contable.reportes.urls')),
    # path('contable/impuestos/', include('apps.prestadores.mi_negocio.gestion_contable.impuestos.urls')),
    # path('contable/proyectos/', include('apps.prestadores.mi_negocio.gestion_contable.proyectos.urls')),
    # path('contable/presupuesto/', include('apps.prestadores.mi_negocio.gestion_contable.presupuesto.urls')),

    # Gestión Archivística
    path('archivistica/', include('apps.prestadores.mi_negocio.gestion_archivistica.urls')),
]
