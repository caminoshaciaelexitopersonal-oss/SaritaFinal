# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/views/rat.py
from .base import GenericViewSet
from apps.prestadores.models import RegistroActividadTuristica
from ..serializers.rat import RegistroActividadTuristicaSerializer

class RegistroActividadTuristicaViewSet(GenericViewSet):
 
    queryset = RegistroActividadTuristica.objects.all()
    serializer_class = RegistroActividadTuristicaSerializer
