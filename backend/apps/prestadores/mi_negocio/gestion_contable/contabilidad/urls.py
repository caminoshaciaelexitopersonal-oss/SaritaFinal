from rest_framework.routers import DefaultRouter
from .views import CostCenterViewSet, ChartOfAccountViewSet, JournalEntryViewSet

router = DefaultRouter()
router.register(r'cost-centers', CostCenterViewSet, basename='cost-center')
router.register(r'chart-of-accounts', ChartOfAccountViewSet, basename='chart-of-account')
router.register(r'journal-entries', JournalEntryViewSet, basename='journal-entry')

urlpatterns = router.urls
