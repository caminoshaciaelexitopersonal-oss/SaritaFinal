from rest_framework.routers import DefaultRouter
from .views import EstadisticaViewSet

router = DefaultRouter()
router.register(r'', EstadisticaViewSet, basename='estadistica')

urlpatterns = router.urls
