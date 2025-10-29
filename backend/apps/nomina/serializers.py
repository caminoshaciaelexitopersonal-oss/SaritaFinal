from rest_framework import serializers
from .models import Empleado, ConceptoNomina, Nomina, DetalleNomina

class EmpleadoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Empleado.
    """
    class Meta:
        model = Empleado
        fields = '__all__'
        read_only_fields = ('perfil',)


class ConceptoNominaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo ConceptoNomina.
    """
    class Meta:
        model = ConceptoNomina
        fields = '__all__'


class DetalleNominaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo DetalleNomina.
    """
    concepto = ConceptoNominaSerializer(read_only=True)

    class Meta:
        model = DetalleNomina
        fields = ('id', 'concepto', 'valor_calculado')


class NominaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Nomina.
    """
    detalles = DetalleNominaSerializer(many=True, read_only=True)

    class Meta:
        model = Nomina
        fields = (
            'id', 'fecha_inicio', 'fecha_fin', 'estado',
            'total_ingresos', 'total_deducciones', 'neto_a_pagar',
            'detalles'
        )
        read_only_fields = ('perfil', 'total_ingresos', 'total_deducciones', 'neto_a_pagar', 'detalles')


class NominaProcesarSerializer(serializers.Serializer):
    """
    Serializador para la acción de procesar una nómina.
    Valida las fechas de inicio y fin.
    """
    fecha_inicio = serializers.DateField()
    fecha_fin = serializers.DateField()

    def validate(self, data):
        """
        Valida que la fecha de inicio no sea posterior a la fecha de fin.
        """
        if data['fecha_inicio'] > data['fecha_fin']:
            raise serializers.ValidationError("La fecha de inicio no puede ser posterior a la fecha de fin.")
        return data
