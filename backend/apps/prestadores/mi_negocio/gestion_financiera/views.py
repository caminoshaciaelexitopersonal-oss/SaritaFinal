# backend/apps/financiero/views.py
from rest_framework import viewsets
from .models import *; from .serializers import *
from apps.prestadores.mi_negocio.gestion_contable.views import ContabilidadBaseViewSet
class BankAccountViewSet(ContabilidadBaseViewSet): queryset = BankAccount.objects.all(); serializer_class = BankAccountSerializer
class CashTransactionViewSet(ContabilidadBaseViewSet): queryset = CashTransaction.objects.all(); serializer_class = CashTransactionSerializer
