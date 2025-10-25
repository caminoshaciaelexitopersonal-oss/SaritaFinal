# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_especializados/views/agencias.py
from ...modulos_genericos.views.base import GenericViewSet
from apps.prestadores.models import PaqueteTuristico, Itinerario
from ..serializers.agencias import PaqueteTuristicoSerializer, ItinerarioSerializer

class PaqueteTuristicoViewSet(GenericViewSet):
    queryset = PaqueteTuristico.objects.all()
    serializer_class = PaqueteTuristicoSerializer

class ItinerarioViewSet(GenericViewSet):
    queryset = Itinerario.objects.all()
    serializer_class = ItinerarioSerializer

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'perfil_prestador'):
            return Itinerario.objects.filter(paquete__perfil=user.perfil_prestador)
        return Itinerario.objects.none()

    def perform_create(self, serializer):
        paquete = serializer.validated_data.get('paquete')
        if paquete.perfil == self.request.user.perfil_prestador:
            serializer.save()
        else:
            raise serializers.ValidationError("No tiene permiso para añadir un itinerario a este paquete.")
