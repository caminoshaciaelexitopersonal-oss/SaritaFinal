from rest_framework import viewsets, permissions, serializers
from rest_framework.pagination import PageNumberPagination
from .models import CategoriaActivo, ActivoFijo, CalculoDepreciacion
from .serializers import CategoriaActivoSerializer, ActivoFijoSerializer, CalculoDepreciacionSerializer
from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import JournalEntry, Transaction, ChartOfAccount

class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # El perfil se encuentra en el objeto principal o a través de una relación
        if hasattr(obj, 'perfil'):
            return obj.perfil == request.user.perfil_prestador
        if hasattr(obj, 'activo'):
            return obj.activo.perfil == request.user.perfil_prestador
        return False

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CategoriaActivoViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaActivoSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return CategoriaActivo.objects.filter(perfil=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        serializer.save(perfil=self.request.user.perfil_prestador)

class ActivoFijoViewSet(viewsets.ModelViewSet):
    serializer_class = ActivoFijoSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return ActivoFijo.objects.filter(perfil=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        serializer.save(perfil=self.request.user.perfil_prestador)

class CalculoDepreciacionViewSet(viewsets.ModelViewSet):
    serializer_class = CalculoDepreciacionSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]
    pagination_class = StandardResultsSetPagination
    http_method_names = ['get', 'post', 'head', 'options'] # Solo permitir crear y listar

    def get_queryset(self):
        return CalculoDepreciacion.objects.filter(activo__perfil=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        depreciacion = serializer.save(creado_por=self.request.user)
        activo = depreciacion.activo
        perfil = activo.perfil

        # --- Creación del Asiento Contable de la Depreciación ---
        try:
            # Estas cuentas deberían ser configurables
            cuenta_gasto_dep = ChartOfAccount.objects.get(code__startswith='5160', perfil=perfil)
            cuenta_dep_acum = ChartOfAccount.objects.get(code__startswith='1592', perfil=perfil)
        except ChartOfAccount.DoesNotExist:
            raise serializers.ValidationError(
                "No se encontraron las cuentas contables requeridas para la depreciación (Gasto '5160' o Dep. Acumulada '1592')."
            )

        journal_entry = JournalEntry.objects.create(
            perfil=perfil,
            entry_date=depreciacion.fecha,
            description=f"Depreciación de {activo.nombre}",
            entry_type="DEPRECIACION",
            user=self.request.user,
            origin_document=depreciacion
        )

        # Débito a Gasto por Depreciación
        Transaction.objects.create(journal_entry=journal_entry, account=cuenta_gasto_dep, debit=depreciacion.monto)
        # Crédito a Depreciación Acumulada
        Transaction.objects.create(journal_entry=journal_entry, account=cuenta_dep_acum, credit=depreciacion.monto)
