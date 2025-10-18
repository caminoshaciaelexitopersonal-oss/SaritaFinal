from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet, basename='producto')
router.register(r'gestion-clientes', views.ClienteViewSet, basename='cliente-crm')
router.register(r'vacantes', views.VacanteViewSet, basename='vacante')
router.register(r'inventario', views.InventarioViewSet, basename='inventario')
router.register(r'costos', views.CostoViewSet, basename='costo')

urlpatterns = [
    path('', include(router.urls)),
]