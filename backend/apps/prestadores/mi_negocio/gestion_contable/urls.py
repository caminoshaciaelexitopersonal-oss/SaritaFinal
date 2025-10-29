from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.contabilidad.views import ChartOfAccountViewSet, JournalEntryViewSet, CostCenterViewSet

router = DefaultRouter()
router.register(r'plan-de-cuentas', ChartOfAccountViewSet, basename='chart-of-accounts')
router.register(r'asientos', JournalEntryViewSet, basename='journal-entries')
router.register(r'centros-de-costo', CostCenterViewSet, basename='cost-centers')

urlpatterns = [
    path('', include(router.urls)),
]
