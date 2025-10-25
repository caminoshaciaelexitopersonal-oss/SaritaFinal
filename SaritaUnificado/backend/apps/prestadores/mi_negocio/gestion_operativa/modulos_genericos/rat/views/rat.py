# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/views/rat.py
from ...views.base import GenericViewSet
from ..models.rat import RegistroActividadTuristica
from ..serializers.rat import RegistroActividadTuristicaSerializer

class RegistroActividadTuristicaViewSet(GenericViewSet):
 
    queryset = RegistroActividadTuristica.objects.all()
    serializer_class = RegistroActividadTuristicaSerializer
