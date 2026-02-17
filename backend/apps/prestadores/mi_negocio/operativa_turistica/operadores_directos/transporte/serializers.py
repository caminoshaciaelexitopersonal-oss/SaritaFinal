from rest_framework import serializers
from .models import (
    Vehicle, VehicleCertification, Conductor, TransportRoute,
    ScheduledTrip, TransportBooking, PassengerManifest,
    TripLiquidation, TransportIncident
)

class VehicleCertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCertification
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    certifications = VehicleCertificationSerializer(many=True, read_only=True)
    class Meta:
        model = Vehicle
        fields = '__all__'

class ConductorSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField(source='usuario.get_full_name')
    class Meta:
        model = Conductor
        fields = '__all__'

class TransportRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportRoute
        fields = '__all__'

class PassengerManifestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerManifest
        fields = '__all__'

class TransportBookingSerializer(serializers.ModelSerializer):
    passengers = PassengerManifestSerializer(many=True, read_only=True)
    class Meta:
        model = TransportBooking
        fields = '__all__'

class ScheduledTripSerializer(serializers.ModelSerializer):
    ruta_nombre = serializers.ReadOnlyField(source='ruta.nombre')
    vehiculo_placa = serializers.ReadOnlyField(source='vehiculo.placa')
    conductor_nombre = serializers.ReadOnlyField(source='conductor.usuario.get_full_name')
    bookings = TransportBookingSerializer(many=True, read_only=True)

    class Meta:
        model = ScheduledTrip
        fields = '__all__'

class TripLiquidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripLiquidation
        fields = '__all__'

class TransportIncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportIncident
        fields = '__all__'
