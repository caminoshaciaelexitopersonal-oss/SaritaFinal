from rest_framework.routers import DefaultRouter
from .views import CategoriaActivoViewSet, ActivoFijoViewSet, DepreciacionViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaActivoViewSet, basename='categoria-activo')
router.register(r'activos-fijos', ActivoFijoViewSet, basename='activo-fijo')
router.register(r'depreciaciones', DepreciacionViewSet, basename='depreciacion')

urlpatterns = router.urls
