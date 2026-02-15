from django.urls import path, include
from api.views import PlaceholderView

app_name = 'mi_negocio'

from .gestion_operativa.views import ProcesoOperativoViewSet, TareaOperativaViewSet, OrdenOperativaViewSet, IncidenteOperativoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'operativa/procesos', ProcesoOperativoViewSet, basename='proceso-operativo')
router.register(r'operativa/tareas', TareaOperativaViewSet, basename='tarea-operativa')
router.register(r'operativa/ordenes', OrdenOperativaViewSet, basename='orden-operativa')
router.register(r'operativa/incidencias', IncidenteOperativoViewSet, basename='incidente-operativo')

urlpatterns = [
    path('', include(router.urls)),
    # Módulos principales con su propio enrutamiento interno
    path('operativa/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.urls')),
    path('comercial/', include('apps.prestadores.mi_negocio.gestion_comercial.urls')),
    path('financiera/', include('apps.prestadores.mi_negocio.gestion_financiera.urls')),

    # Módulo contable es una agrupación de otros módulos
    path('contable/contabilidad/', include('apps.prestadores.mi_negocio.gestion_contable.contabilidad.urls')),
    path('contable/activos-fijos/', include('apps.prestadores.mi_negocio.gestion_contable.activos_fijos.urls')),
    path('contable/nomina/', include('apps.prestadores.mi_negocio.gestion_contable.nomina.urls')),

    # Gestión Archivística
    path('archivistica/', include('apps.prestadores.mi_negocio.gestion_archivistica.urls')),

    # Seguridad y Salud en el Trabajo (SG-SST)
    path('operativa/sst/', include('apps.prestadores.mi_negocio.gestion_operativa.sg_sst.urls')),
]
