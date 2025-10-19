from rest_framework import serializers
from ..modelos.clientes import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'email', 'telefono', 'notas', 'fecha_creacion']
        read_only_fields = ['id', 'fecha_creacion', 'prestador']