import csv
from django.http import HttpResponse
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Proveedor, FacturaCompra
from .serializers import ProveedorSerializer, FacturaCompraSerializer

class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Para Proveedor y FacturaCompra, el perfil está directamente en el objeto.
        return obj.perfil == request.user.perfil_prestador

class ProveedorViewSet(viewsets.ModelViewSet):
    serializer_class = ProveedorSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return Proveedor.objects.filter(perfil=self.request.user.perfil_prestador)

class FacturaCompraViewSet(viewsets.ModelViewSet):
    serializer_class = FacturaCompraSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return FacturaCompra.objects.filter(perfil=self.request.user.perfil_prestador)

class GenerarPagoMasivoProveedoresView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        factura_ids = request.data.get('factura_ids', [])
        if not factura_ids:
            return Response({"error": "No se proporcionaron IDs de facturas."}, status=status.HTTP_400_BAD_REQUEST)

        perfil = request.user.perfil_prestador
        facturas = FacturaCompra.objects.filter(id__in=factura_ids, perfil=perfil, estado=FacturaCompra.Estado.POR_PAGAR)

        if not facturas.exists():
            return Response({"error": "Ninguna de las facturas seleccionadas es válida para pago."}, status=status.HTTP_404_NOT_FOUND)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="pagos_masivos.csv"'

        writer = csv.writer(response)
        writer.writerow(['ID Factura', 'Proveedor', 'Identificacion Proveedor', 'Monto a Pagar', 'Numero Cuenta', 'Banco'])

        for factura in facturas:
            # Asumimos que el proveedor tiene un número de cuenta guardado en el campo 'notas' para este ejemplo
            # En una implementación real, esto debería estar en un modelo de 'InformacionBancariaProveedor'
            writer.writerow([
                factura.id,
                factura.proveedor.nombre,
                factura.proveedor.identificacion,
                factura.total,
                "CTA-EJEMPLO-123", # Placeholder
                "BANCO-EJEMPLO" # Placeholder
            ])

        return response
