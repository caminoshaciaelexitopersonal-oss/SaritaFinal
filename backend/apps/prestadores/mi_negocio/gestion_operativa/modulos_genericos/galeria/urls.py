from rest_framework.routers import DefaultRouter
from .views import GaleriaViewSet

router = DefaultRouter()
router.register(r'', GaleriaViewSet, basename='galeria')

urlpatterns = router.urls
