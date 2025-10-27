# backend/apps/financiero/views.py
from rest_framework import viewsets
from .models import *; from .serializers import *
from apps.contabilidad.views import ContabilidadBaseViewSet
class BankAccountViewSet(ContabilidadBaseViewSet): queryset = BankAccount.objects.all(); serializer_class = BankAccountSerializer
class CashTransactionViewSet(ContabilidadBaseViewSet): queryset = CashTransaction.objects.all(); serializer_class = CashTransactionSerializer
