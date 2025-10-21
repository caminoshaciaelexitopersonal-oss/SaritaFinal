from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.clientes import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'email', 'telefono', 'notas']
