from rest_framework import serializers
from .models import CuentaBancaria, TransaccionBancaria

class CuentaBancariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentaBancaria
        fields = ['id', 'banco', 'numero_cuenta', 'tipo_cuenta', 'saldo_actual', 'titular']
        read_only_fields = ('saldo_actual',)

    def create(self, validated_data):
        validated_data['perfil'] = self.context['request'].user.perfil_prestador
        return super().create(validated_data)

class TransaccionBancariaSerializer(serializers.ModelSerializer):
    creado_por = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TransaccionBancaria
        fields = ['id', 'cuenta', 'fecha', 'tipo', 'monto', 'descripcion', 'creado_por', 'creado_en']
        read_only_fields = ('creado_en',)

    def validate_cuenta(self, value):
        # Asegurarse que la cuenta bancaria pertenece al perfil del usuario
        if value.perfil != self.context['request'].user.perfil_prestador:
            raise serializers.ValidationError("La cuenta bancaria seleccionada no pertenece a su perfil.")
        return value
