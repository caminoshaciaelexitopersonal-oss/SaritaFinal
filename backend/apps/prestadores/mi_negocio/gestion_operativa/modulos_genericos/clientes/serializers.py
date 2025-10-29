# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/clientes/serializers.py
from rest_framework import serializers
from apps.comercial.models import Cliente  # Import centralizado

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'email', 'telefono', 'perfil']
        read_only_fields = ['perfil']
