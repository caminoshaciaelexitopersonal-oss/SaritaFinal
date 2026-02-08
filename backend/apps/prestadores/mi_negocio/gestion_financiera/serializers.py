from rest_framework import serializers
from .models import CuentaBancaria, OrdenPago, TesoreriaCentral, EstadoResultados, BalanceGeneral, FlujoEfectivo, CambiosPatrimonio, ReservaFinanciera, ProyeccionFinanciera, RiesgoFinanciero

class TesoreriaCentralSerializer(serializers.ModelSerializer):
    class Meta:
        model = TesoreriaCentral
        fields = '__all__'

class EstadoResultadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoResultados
        fields = '__all__'

class BalanceGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = BalanceGeneral
        fields = '__all__'

class FlujoEfectivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlujoEfectivo
        fields = '__all__'

class CambiosPatrimonioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CambiosPatrimonio
        fields = '__all__'

class ReservaFinancieraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaFinanciera
        fields = '__all__'

class ProyeccionFinancieraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProyeccionFinanciera
        fields = '__all__'

class RiesgoFinancieroSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiesgoFinanciero
        fields = '__all__'

class CuentaBancariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentaBancaria
        fields = '__all__'

class OrdenPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenPago
        fields = '__all__'
