from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SaritaProfileView, PlanViewSet, SuscripcionViewSet
from apps.audit.views import ForensicSecurityLogViewSet

app_name = 'admin_plataforma'

router = DefaultRouter()
router.register(r'planes', PlanViewSet, basename='plan')
router.register(r'suscripciones', SuscripcionViewSet, basename='suscripcion')
router.register(r'audit/forensic-logs', ForensicSecurityLogViewSet, basename='forensic-log')

urlpatterns = [
    path('profile/', SaritaProfileView.as_view(), name='sarita-profile'),

 
    # ERP SISTÉMICO - ACOPLAMIENTO FUNCIONAL TOTAL FASE 1
    # Todos los módulos ahora importan de apps.prestadores y usan SystemicERPViewSetMixin
    path('operativa/', include('apps.admin_plataforma.gestion_operativa.modulos_genericos.urls')),
    path('comercial/', include('apps.admin_plataforma.gestion_comercial.urls')),
    path('archivistica/', include('apps.admin_plataforma.gestion_archivistica.urls')),
    path('financiera/', include('apps.admin_plataforma.gestion_financiera.urls')),
    path('contabilidad/', include('apps.admin_plataforma.gestion_contable.contabilidad.urls')),
    path('defense-predictive/', include('apps.defense_predictive.urls')),
    path('defense-deception/', include('apps.defense_deception.urls')),
 

    path('', include(router.urls)),
]
