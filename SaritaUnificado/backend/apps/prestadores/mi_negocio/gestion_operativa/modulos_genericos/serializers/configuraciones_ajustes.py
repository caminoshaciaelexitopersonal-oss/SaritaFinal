from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.configuraciones_ajustes import ConfiguracionPrestador

class ConfiguracionPrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfiguracionPrestador
        fields = ['recibir_notificaciones_email', 'recibir_notificaciones_push', 'tema_interfaz']
