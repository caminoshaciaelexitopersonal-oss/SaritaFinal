# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_especializados/views/guias.py
from ...modulos_genericos.views.base import GenericViewSet
from apps.prestadores.models import Ruta, HitoRuta, Equipamiento
from ..serializers.guias import RutaSerializer, HitoRutaSerializer, EquipamientoSerializer

class RutaViewSet(GenericViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer

class HitoRutaViewSet(GenericViewSet):
    queryset = HitoRuta.objects.all()
    serializer_class = HitoRutaSerializer

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'perfil_prestador'):
            return HitoRuta.objects.filter(ruta__perfil=user.perfil_prestador)
        return HitoRuta.objects.none()

    def perform_create(self, serializer):
        ruta = serializer.validated_data.get('ruta')
        if ruta.perfil == self.request.user.perfil_prestador:
            serializer.save()
        else:
            raise serializers.ValidationError("No tiene permiso para añadir hitos a esta ruta.")

class EquipamientoViewSet(GenericViewSet):
    queryset = Equipamiento.objects.all()
    serializer_class = EquipamientoSerializer
