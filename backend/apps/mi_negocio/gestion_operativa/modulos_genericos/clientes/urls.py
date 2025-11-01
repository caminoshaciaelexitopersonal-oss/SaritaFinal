
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet

router = DefaultRouter()
router.register(r'', ClienteViewSet, basename='cliente')

app_name = 'clientes'

urlpatterns = [
    path('', include(router.urls)),
]
