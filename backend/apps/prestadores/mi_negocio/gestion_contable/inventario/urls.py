from rest_framework.routers import DefaultRouter
from .views import (
    CategoriaProductoViewSet,
    AlmacenViewSet,
    ProductoViewSet,
    MovimientoInventarioViewSet
)

router = DefaultRouter()
router.register(r'categorias', CategoriaProductoViewSet, basename='categoria-producto')
router.register(r'almacenes', AlmacenViewSet, basename='almacen')
router.register(r'productos', ProductoViewSet, basename='producto')
router.register(r'movimientos', MovimientoInventarioViewSet, basename='movimiento-inventario')

urlpatterns = router.urls
