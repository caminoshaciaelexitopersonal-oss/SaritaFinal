# backend/apps/core_erp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('integrity/status/', views.SystemIntegrityStatusView.as_view(), name='integrity-status'),
    path('integrity/run/', views.RunCertificationView.as_view(), name='integrity-run'),
]
