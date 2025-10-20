from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categorias-con-productos', views.CategoriaConProductosViewSet, basename='categoria-con-productos')
router.register(r'categorias-menu', views.CategoriaMenuViewSet, basename='categoria-menu')
router.register(r'productos-menu', views.ProductoMenuViewSet, basename='producto-menu')
router.register(r'mesas', views.MesaViewSet, basename='mesa')
router.register(r'pedidos', views.PedidoViewSet, basename='pedido')

urlpatterns = [
    path('', include(router.urls)),
]