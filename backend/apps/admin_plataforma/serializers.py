
from rest_framework import serializers
from backend.apps.admin_plataforma.models import Plan, Suscripcion
from backend.apps.common.serializers.polymorphic_owner import PolymorphicOwnerSerializerMixin
from backend.apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = [
            'id', 'nombre', 'descripcion', 'precio',
            'frecuencia', 'tipo_usuario_objetivo', 'is_active'
        ]

class SuscripcionSerializer(serializers.ModelSerializer):
    plan = PlanSerializer(read_only=True)
    plan_id = serializers.PrimaryKeyRelatedField(
        queryset=Plan.objects.all(), source='plan', write_only=True
    )
    cliente_id = serializers.PrimaryKeyRelatedField(
        queryset=ProviderProfile.objects.all(), source='cliente', write_only=True
    )

    class Meta:
        model = Suscripcion
        fields = [
            'id', 'plan', 'plan_id', 'cliente_id', 'fecha_inicio', 'fecha_fin',
            'is_active'
        ]
        read_only_fields = ('is_active', 'fecha_fin')
