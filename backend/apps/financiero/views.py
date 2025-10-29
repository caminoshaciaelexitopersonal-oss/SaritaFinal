# backend/apps/financiero/views.py
from rest_framework import viewsets, permissions
from .models import BankAccount, CashTransaction
from .serializers import BankAccountSerializer, CashTransactionSerializer
from apps.contabilidad.views import ContabilidadBaseViewSet # Reutilizamos el BaseViewSet

class FinancieroBaseViewSet(ContabilidadBaseViewSet):
    """
    ViewSet base para los modelos financieros.
    Hereda la lógica de filtrado por perfil de ContabilidadBaseViewSet.
    """
    pass

class BankAccountViewSet(FinancieroBaseViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

class CashTransactionViewSet(FinancieroBaseViewSet):
    queryset = CashTransaction.objects.all()
    serializer_class = CashTransactionSerializer

    def perform_create(self, serializer):
        # La lógica de creación está en el serializador.
        # El BaseViewSet se encargará de añadir el perfil si es necesario,
        # pero en nuestro caso, el serializador ya lo hace.
        serializer.save()
