from rest_framework import mixins, viewsets
from .base import GenericViewSet
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.configuraciones_ajustes import ConfiguracionPrestador
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.serializers.configuraciones_ajustes import ConfiguracionPrestadorSerializer

class ConfiguracionPrestadorViewSet(mixins.RetrieveModelMixin,
                                      mixins.UpdateModelMixin,
                                      viewsets.GenericViewSet):
    """
    API endpoint para gestionar la Configuración del prestador.
    """
    queryset = ConfiguracionPrestador.objects.all()
    serializer_class = ConfiguracionPrestadorSerializer
    permission_classes = GenericViewSet.permission_classes

    def get_object(self):
        """
        Devuelve la instancia de configuración única para el perfil del usuario.
        Se crea si no existe.
        """
        config, created = ConfiguracionPrestador.objects.get_or_create(perfil=self.request.user.perfil_prestador)
        return config
