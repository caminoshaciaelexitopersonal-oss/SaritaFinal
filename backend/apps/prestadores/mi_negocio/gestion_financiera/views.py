from rest_framework import viewsets, permissions
from .models import CuentaBancaria, TransaccionBancaria
from .serializers import CuentaBancariaSerializer, TransaccionBancariaSerializer
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.permissions import IsOwner
from django.core.exceptions import ValidationError

class CuentaBancariaViewSet(viewsets.ModelViewSet):
    serializer_class = CuentaBancariaSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return CuentaBancaria.objects.filter(perfil=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        serializer.save(perfil=self.request.user.perfil_prestador)


class TransaccionBancariaViewSet(viewsets.ModelViewSet):
    serializer_class = TransaccionBancariaSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        # Asegurar que solo se listen transacciones de cuentas que pertenecen al perfil del usuario
        return TransaccionBancaria.objects.filter(cuenta__perfil=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        cuenta = serializer.validated_data['cuenta']

        # Validar que la cuenta bancaria pertenece al perfil del usuario autenticado
        if cuenta.perfil != self.request.user.perfil_prestador:
            raise ValidationError("No tiene permiso para realizar transacciones en esta cuenta.")

        # La lógica de actualización de saldo y validaciones está en el modelo.
        # Simplemente guardamos la transacción, asignando el usuario actual.
        serializer.save(creado_por=self.request.user)
