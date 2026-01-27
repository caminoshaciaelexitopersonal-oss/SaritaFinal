from django.urls import path
from backend.balance_general import BalanceGeneralView
from backend.estado_resultados import EstadoResultadosView

urlpatterns = [
    path('balance-general/', BalanceGeneralView.as_view(), name='balance-general'),
    path('estado-resultados/', EstadoResultadosView.as_view(), name='estado-resultados'),
]
