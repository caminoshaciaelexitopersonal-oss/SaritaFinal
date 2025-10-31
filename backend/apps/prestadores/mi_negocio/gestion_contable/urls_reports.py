# backend/apps/contabilidad/urls_reports.py
from django.urls import path; from . import views_reports
urlpatterns = [path('libro-diario/', views_reports.ReportBaseView.as_view())] # Placeholder
