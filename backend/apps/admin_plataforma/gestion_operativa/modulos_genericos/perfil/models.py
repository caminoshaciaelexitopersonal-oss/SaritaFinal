import uuid
from django.db import models
from django.utils import timezone
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import BaseModel, ProviderProfile

# --- MODELOS BASE DE ROBUSTEZ (para esta app) ---

from ..permissions import get_current_tenant

class TenantQuerySet(models.QuerySet):
    def for_tenant(self, tenant):
        return self.filter(provider=tenant)

class TenantManager(models.Manager):
    """
    Manager que AUTOMÁTICAMENTE filtra cada consulta por el inquilino activo.
    """
    def get_queryset(self):
        queryset = TenantQuerySet(self.model, using=self._db)
        tenant = get_current_tenant()
        if tenant:
            return queryset.for_tenant(tenant)
        # Principio de fallo seguro: si no hay inquilino, no devolver nada.
        return queryset.none()

class TenantAwareModel(BaseModel):
    """
    Modelo base abstracto para todos los datos que pertenecen a un inquilino.
    """
    provider = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name="%(class)s_items")
    objects = TenantManager()
    objects_unfiltered = models.Manager()

    class Meta:
        abstract = True
