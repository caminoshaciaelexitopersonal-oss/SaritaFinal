from rest_framework import viewsets
from .services.gestion_plataforma_service import GestionPlataformaService

class SystemicERPViewSetMixin:
    """
    Mixin para asegurar que los ViewSets del Admin de Plataforma
    siempre filtren por el perfil de la organización central (Gobierno).
    """
    def get_queryset(self):
        perfil_gobierno = GestionPlataformaService.get_perfil_gobierno()
        queryset = super().get_queryset()

        if not perfil_gobierno:
            return queryset

        # Filtramos por el perfil de gobierno, ignorando el tenant del usuario logueado
        # para que el Super Admin vea los datos de la plataforma.
        if hasattr(queryset.model, 'provider'):
            return queryset.filter(provider=perfil_gobierno)
        elif hasattr(queryset.model, 'perfil'):
            return queryset.filter(perfil=perfil_gobierno)
        elif hasattr(queryset.model, 'perfil_ref_id'):
            return queryset.filter(perfil_ref_id=perfil_gobierno.id)

        return queryset
