from rest_framework import serializers
from .models import Empleado, ConceptoNomina, Nomina, DetalleNomina

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'
        read_only_fields = ('perfil',)

class ConceptoNominaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConceptoNomina
        fields = '__all__'

class DetalleNominaSerializer(serializers.ModelSerializer):
    concepto = ConceptoNominaSerializer(read_only=True)
    class Meta:
        model = DetalleNomina
        fields = ('id', 'concepto', 'valor_calculado')

class NominaSerializer(serializers.ModelSerializer):
    detalles = DetalleNominaSerializer(many=True, read_only=True)
    class Meta:
        model = Nomina
        fields = ('id', 'fecha_inicio', 'fecha_fin', 'estado', 'total_ingresos', 'total_deducciones', 'neto_a_pagar', 'detalles')
        read_only_fields = ('perfil', 'total_ingresos', 'total_deducciones', 'neto_a_pagar', 'detalles')

class NominaProcesarSerializer(serializers.Serializer):
    fecha_inicio = serializers.DateField()
    fecha_fin = serializers.DateField()
    def validate(self, data):
        if data['fecha_inicio'] > data['fecha_fin']:
            raise serializers.ValidationError("La fecha de inicio no puede ser posterior a la fecha de fin.")
        return data
