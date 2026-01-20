
from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = 'admin_plataforma'

# futuro: router = DefaultRouter()
# futuro: router.register(r'planes', PlanesViewSet, basename='planes')

from .views import SaritaProfileView

urlpatterns = [
    path('profile/', SaritaProfileView.as_view(), name='sarita-profile'),
    # futuro: path('', include(router.urls)),
]
