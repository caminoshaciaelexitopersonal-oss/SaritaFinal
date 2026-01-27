from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.views import (
    OrganizadorEventoViewSet,
    EventoViewSet,
    PromocionViewSet,
)

router = DefaultRouter()
router.register(r'organizadores', OrganizadorEventoViewSet, basename='organizador')
router.register(r'eventos', EventoViewSet, basename='evento')
router.register(r'promociones', PromocionViewSet, basename='promocion')

urlpatterns = [
    path('', include(router.urls)),
]
