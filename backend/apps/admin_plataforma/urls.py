
from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = 'admin_plataforma'

# futuro: router = DefaultRouter()
# futuro: router.register(r'planes', PlanesViewSet, basename='planes')

 
from backend.apps.admin_plataforma.views import SaritaProfileView, PlanViewSet, SuscripcionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'planes', PlanViewSet, basename='plan')
router.register(r'suscripciones', SuscripcionViewSet, basename='suscripcion')

urlpatterns = [
    path('profile/', SaritaProfileView.as_view(), name='sarita-profile'),
    path('', include(router.urls)),
 
]
