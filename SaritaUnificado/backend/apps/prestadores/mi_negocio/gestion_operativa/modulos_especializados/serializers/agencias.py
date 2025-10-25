# backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_especializados/serializers/agencias.py
from rest_framework import serializers
from apps.prestadores.models import PaqueteTuristico, Itinerario, Habitacion, ProductoMenu, Ruta, Vehiculo
from .hoteles import HabitacionSerializer
from .restaurantes import ProductoMenuSerializer
from .guias import RutaSerializer
from .transporte import VehiculoSerializer

class PaqueteTuristicoSerializer(serializers.ModelSerializer):
    # Usamos slugs o IDs para las relaciones de escritura
    habitaciones_incluidas = serializers.PrimaryKeyRelatedField(many=True, queryset=Habitacion.objects.all(), write_only=True)
    comidas_incluidas = serializers.PrimaryKeyRelatedField(many=True, queryset=ProductoMenu.objects.all(), write_only=True)
    rutas_incluidas = serializers.PrimaryKeyRelatedField(many=True, queryset=Ruta.objects.all(), write_only=True)
    transporte_incluido = serializers.PrimaryKeyRelatedField(many=True, queryset=Vehiculo.objects.all(), write_only=True)

    # Usamos serializers anidados para las relaciones de lectura (detalle)
    habitaciones_detalle = HabitacionSerializer(source='habitaciones_incluidas', many=True, read_only=True)
    comidas_detalle = ProductoMenuSerializer(source='comidas_incluidas', many=True, read_only=True)
    rutas_detalle = RutaSerializer(source='rutas_incluidas', many=True, read_only=True)
    transporte_detalle = VehiculoSerializer(source='transporte_incluido', many=True, read_only=True)

    class Meta:
        model = PaqueteTuristico
        fields = [
            'id', 'nombre', 'descripcion', 'duracion_dias', 'precio_base',
            'foto_principal', 'activo', 'perfil',
            'habitaciones_incluidas', 'comidas_incluidas', 'rutas_incluidas', 'transporte_incluido', # Para escritura
            'habitaciones_detalle', 'comidas_detalle', 'rutas_detalle', 'transporte_detalle' # Para lectura
        ]
        read_only_fields = ['id']

    def validate(self, data):
        """
        Valida que los servicios añadidos pertenezcan al mismo prestador
        o a prestadores asociados (lógica de negocio futura).
        Por ahora, asumimos que pertenecen al mismo perfil.
        """
        perfil = self.context['request'].user.perfil_prestador

        for habitacion in data.get('habitaciones_incluidas', []):
            if habitacion.perfil != perfil:
                raise serializers.ValidationError(f"La habitación '{habitacion}' no pertenece a su negocio.")

        # Repetir validación para comidas, rutas, transporte...

        return data

class ItinerarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerario
        fields = ['id', 'paquete', 'dia', 'titulo_actividad', 'descripcion']
        read_only_fields = ['id']
