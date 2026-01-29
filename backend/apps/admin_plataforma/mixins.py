from rest_framework import viewsets
from .services.gestion_plataforma_service import GestionPlataformaService

class SystemicERPViewSetMixin:
    """
    Mixin para asegurar que los ViewSets del Admin de Plataforma
    siempre filtren por el perfil de la organización central (Gobierno)
    dentro del dominio administrativo instanciado.
    """
    def get_queryset(self):
        perfil_gobierno = GestionPlataformaService.get_perfil_gobierno_context()
        queryset = super().get_queryset()

        if not perfil_gobierno:
            return queryset

        # En el dominio instanciado usamos 'organization' por defecto
        if hasattr(queryset.model, 'organization'):
            return queryset.filter(organization=perfil_gobierno)

        # Fallbacks para otros esquemas si existieran
        if hasattr(queryset.model, 'provider'):
            return queryset.filter(provider=perfil_gobierno)
        elif hasattr(queryset.model, 'perfil'):
            return queryset.filter(perfil=perfil_gobierno)

        return queryset
