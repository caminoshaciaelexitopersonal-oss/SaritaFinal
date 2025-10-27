from rest_framework.routers import DefaultRouter
from .views import ValoracionViewSet

router = DefaultRouter()
router.register(r'', ValoracionViewSet, basename='valoracion')

urlpatterns = router.urls
