from rest_framework.routers import DefaultRouter
from backend.views import InventoryItemViewSet

router = DefaultRouter()
router.register(r'items', InventoryItemViewSet, basename='item')

urlpatterns = router.urls
