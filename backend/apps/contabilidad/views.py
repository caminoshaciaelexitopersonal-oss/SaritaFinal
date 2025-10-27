# backend/apps/contabilidad/views.py
from rest_framework import viewsets, permissions
from .models import *; from .serializers import *
class ContabilidadBaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self): return self.queryset.filter(perfil=self.request.user.perfil_prestador)
    def perform_create(self, serializer): serializer.save(perfil=self.request.user.perfil_prestador)
class ChartOfAccountViewSet(ContabilidadBaseViewSet): queryset = ChartOfAccount.objects.all(); serializer_class = ChartOfAccountSerializer
class JournalEntryViewSet(ContabilidadBaseViewSet): queryset = JournalEntry.objects.all(); serializer_class = JournalEntrySerializer
class CurrencyViewSet(viewsets.ReadOnlyModelViewSet): queryset = Currency.objects.all(); serializer_class = CurrencySerializer
