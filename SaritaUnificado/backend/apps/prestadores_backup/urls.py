from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PerfilViewSet,
    CategoriaPrestadorListView,
    ClienteViewSet,
    ProductoServicioViewSet,
    InventarioViewSet,
    CostoViewSet
)

router = DefaultRouter()
router.register(r'perfil', PerfilViewSet, basename='perfil')
router.register(r'clientes', ClienteViewSet, basename='clientes')
router.register(r'productos-servicios', ProductoServicioViewSet, basename='productos-servicios')
router.register(r'inventario', InventarioViewSet, basename='inventario')
router.register(r'costos', CostoViewSet, basename='costos')

urlpatterns = [
    path('', include(router.urls)),
    path('categorias/', CategoriaPrestadorListView.as_view(), name='categoria-list'),
]
