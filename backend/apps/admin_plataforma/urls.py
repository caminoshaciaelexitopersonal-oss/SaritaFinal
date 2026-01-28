from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SaritaProfileView, PlanViewSet, SuscripcionViewSet

app_name = 'admin_plataforma'

router = DefaultRouter()
router.register(r'planes', PlanViewSet, basename='plan')
router.register(r'suscripciones', SuscripcionViewSet, basename='suscripcion')

urlpatterns = [
    path('profile/', SaritaProfileView.as_view(), name='sarita-profile'),

    # BLOQUEO TÉCNICO - FASE 1:
    # Las siguientes rutas están comentadas para evitar el RuntimeError de colisión de modelos.
    # Los modelos en gestion_operativa/gestion_comercial en admin_plataforma tienen el mismo
    # app_label que en prestadores, lo que impide que Django registre ambos simultáneamente.
    # Ref: INFORME_ACOPLAMIENTO_ERP.md

    # path('operativa/', include('apps.admin_plataforma.gestion_operativa.modulos_genericos.urls')),
    # path('comercial/', include('apps.admin_plataforma.gestion_comercial.urls')),

    path('', include(router.urls)),
]
