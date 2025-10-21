from .base import GenericViewSet
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.rat import RegistroActividadTuristica
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.serializers.rat import RegistroActividadTuristicaSerializer

class RegistroActividadTuristicaViewSet(GenericViewSet):
    """
    API endpoint para gestionar los Registros de Actividad Turística (RAT) del prestador.
    """
    queryset = RegistroActividadTuristica.objects.all()
    serializer_class = RegistroActividadTuristicaSerializer
