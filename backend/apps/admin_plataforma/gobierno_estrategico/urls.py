from django.urls import path
from .views import GovernanceSummaryView, ComparativeAnalysisView, ProviderRankingView, GlobalAuditLogView

urlpatterns = [
    path('summary/', GovernanceSummaryView.as_view(), name='governance-summary'),
    path('comparative/', ComparativeAnalysisView.as_view(), name='governance-comparative'),
    path('ranking/', ProviderRankingView.as_view(), name='governance-ranking'),
    path('audit/', GlobalAuditLogView.as_view(), name='governance-audit'),
]
