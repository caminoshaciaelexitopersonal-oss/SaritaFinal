from rest_framework.routers import DefaultRouter
from .presentation.views import BusinessReportsViewSet

router = DefaultRouter()
router.register(r'reports', BusinessReportsViewSet, basename='business-reports')

urlpatterns = router.urls
