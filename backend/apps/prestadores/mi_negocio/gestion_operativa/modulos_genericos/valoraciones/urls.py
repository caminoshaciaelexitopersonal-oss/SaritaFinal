from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.views import ValoracionViewSet

router = DefaultRouter()
router.register(r'valoraciones', ValoracionViewSet, basename='valoracion')

urlpatterns = [
    path('', include(router.urls)),
]
