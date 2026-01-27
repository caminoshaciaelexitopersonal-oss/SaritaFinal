from django.urls import path
from backend.iva import ReporteIVAView

urlpatterns = [
    path('iva/', ReporteIVAView.as_view(), name='reporte-iva'),
]
