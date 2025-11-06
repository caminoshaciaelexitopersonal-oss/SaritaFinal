from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CostCenterViewSet, ChartOfAccountViewSet, JournalEntryViewSet, LibroMayorView, BalanceComprobacionView, ReportesFinancierosView

router = DefaultRouter()
router.register(r'cost-centers', CostCenterViewSet, basename='cost-center')
router.register(r'chart-of-accounts', ChartOfAccountViewSet, basename='chart-of-account')
router.register(r'journal-entries', JournalEntryViewSet, basename='journal-entry')

urlpatterns = router.urls + [
    path('reportes/libro-mayor/', LibroMayorView.as_view(), name='reporte-libro-mayor'),
    path('reportes/balance-comprobacion/', BalanceComprobacionView.as_view(), name='reporte-balance-comprobacion'),
    path('reportes/financieros/', ReportesFinancierosView.as_view(), name='reportes-financieros'),
]
