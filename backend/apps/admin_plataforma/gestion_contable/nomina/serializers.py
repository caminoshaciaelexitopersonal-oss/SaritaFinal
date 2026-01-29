from rest_framework import serializers
from apps.admin_plataforma.gestion_contable.nomina.models import Empleado, Contrato, Planilla, NovedadNomina, ConceptoNomina

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = ['id', 'fecha_inicio', 'fecha_fin', 'salario', 'cargo', 'activo']

class EmpleadoSerializer(serializers.ModelSerializer):
    contratos = ContratoSerializer(many=True, read_only=True)

    class Meta:
        model = Empleado
        fields = ['id', 'nombre', 'apellido', 'identificacion', 'fecha_nacimiento', 'direccion', 'telefono', 'email', 'contratos']

    def create(self, validated_data):
        validated_data['perfil'] = self.context['request'].user.perfil_prestador
        return super().create(validated_data)

class ConceptoNominaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConceptoNomina
        fields = ['id', 'codigo', 'descripcion', 'tipo']

class NovedadNominaSerializer(serializers.ModelSerializer):
    concepto = ConceptoNominaSerializer(read_only=True)
    concepto_id = serializers.PrimaryKeyRelatedField(queryset=ConceptoNomina.objects.all(), source='concepto', write_only=True)

    class Meta:
        model = NovedadNomina
        fields = ['id', 'empleado', 'concepto', 'concepto_id', 'valor', 'descripcion']

class PlanillaSerializer(serializers.ModelSerializer):
    novedades = NovedadNominaSerializer(many=True)

    class Meta:
        model = Planilla
        fields = ['id', 'periodo_inicio', 'periodo_fin', 'total_devengado', 'total_deduccion', 'total_neto', 'novedades']
        read_only_fields = ('total_devengado', 'total_deduccion', 'total_neto')

    def create(self, validated_data):
        novedades_data = validated_data.pop('novedades')
        validated_data['perfil'] = self.context['request'].user.perfil_prestador
        planilla = Planilla.objects.create(**validated_data)

        total_devengado = Decimal('0.00')
        total_deduccion = Decimal('0.00')

        for novedad_data in novedades_data:
            novedad = NovedadNomina.objects.create(planilla=planilla, **novedad_data)
            if novedad.concepto.tipo == ConceptoNomina.TipoConcepto.DEVENGADO:
                total_devengado += novedad.valor
            else:
                total_deduccion += novedad.valor

        planilla.total_devengado = total_devengado
        planilla.total_deduccion = total_deduccion
        planilla.total_neto = total_devengado - total_deduccion
        planilla.save()

        return planilla
