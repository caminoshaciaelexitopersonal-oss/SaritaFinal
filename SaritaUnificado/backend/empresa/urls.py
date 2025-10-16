from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet, basename='producto')
router.register(r'clientes-estadisticas', views.RegistroClienteViewSet, basename='cliente-estadistica') # Renombrado para claridad
router.register(r'gestion-clientes', views.ClienteViewSet, basename='cliente-crm') # Nuevo endpoint para CRM
router.register(r'vacantes', views.VacanteViewSet, basename='vacante')

urlpatterns = [
    path('', include(router.urls)),
]