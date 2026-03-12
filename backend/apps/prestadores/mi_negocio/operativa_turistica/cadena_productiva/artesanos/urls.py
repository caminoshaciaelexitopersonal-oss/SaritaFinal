from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RawMaterialViewSet, WorkshopOrderViewSet, ProductionLogViewSet

router = DefaultRouter()
router.register(r'materiales', RawMaterialViewSet, basename='artesano-material')
router.register(r'ordenes', WorkshopOrderViewSet, basename='artesano-orden')
router.register(r'produccion', ProductionLogViewSet, basename='artesano-produccion')

urlpatterns = [
    path('', include(router.urls)),
]
