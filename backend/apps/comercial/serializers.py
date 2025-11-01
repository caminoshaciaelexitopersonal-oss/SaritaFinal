from rest_framework import serializers
from .models import Cliente, FacturaVenta

class FacturaVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaVenta
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'email', 'telefono']
        read_only_fields = ['perfil'] # El perfil se asignará automáticamente

    def validate_email(self, value):
        """
        Asegura que el email del cliente sea único para el prestador actual.
        """
        request = self.context.get('request')
        if request and hasattr(request.user, 'perfil_prestador'):
            perfil = request.user.perfil_prestador
            # Excluir el objeto actual en caso de una actualización (PATCH)
            instance = self.instance
            query = Cliente.objects.filter(perfil=perfil, email__iexact=value)
            if instance:
                query = query.exclude(pk=instance.pk)
            if query.exists():
                raise serializers.ValidationError("Ya existe un cliente con este correo electrónico.")
        return value
