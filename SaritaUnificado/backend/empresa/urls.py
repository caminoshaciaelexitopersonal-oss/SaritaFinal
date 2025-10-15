from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet, basename='producto')
router.register(r'clientes', views.RegistroClienteViewSet, basename='cliente')
router.register(r'vacantes', views.VacanteViewSet, basename='vacante')

urlpatterns = [
    path('', include(router.urls)),
]