# backend/apps/activos/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivoFijoViewSet

router = DefaultRouter()
router.register(r'activos-fijos', ActivoFijoViewSet, basename='activofijo')

urlpatterns = [
    path('', include(router.urls)),
]
