from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# Rutas eliminadas para Producto y Cliente
router.register(r'vacantes', views.VacanteViewSet, basename='vacante')
router.register(r'inventario', views.InventarioViewSet, basename='inventario')
router.register(r'costos', views.CostoViewSet, basename='costo')

urlpatterns = [
    path('', include(router.urls)),
]
