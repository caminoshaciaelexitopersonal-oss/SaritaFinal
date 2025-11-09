import uuid
from django.db import models
from django.conf import settings
from apps.companies.models import Company

# --- MODELOS BASE DE ROBUSTEZ ---

class BaseModel(models.Model):
    """
    Modelo base abstracto que añade campos de auditoría comunes.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

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
    provider = models.ForeignKey('perfil.ProviderProfile', on_delete=models.CASCADE, related_name="%(class)s_items")
    objects = TenantManager()
    objects_unfiltered = models.Manager()

    class Meta:
        abstract = True


# --- MODELOS DE PERFIL Y CATEGORÍA ---

class CategoriaPrestador(BaseModel):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, help_text="Versión del nombre amigable para URLs")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría de Prestador"
        verbose_name_plural = "Categorías de Prestadores"


class ProviderProfile(BaseModel):
    """
    EL INQUILINO (TENANT).
    Representa a una empresa prestadora de servicios. No hereda de TenantAwareModel.
    Refactorizado desde el modelo original 'Perfil'.
    """
    class ProviderTypes(models.TextChoices):
        RESTAURANT = 'RESTAURANT', 'Restaurante'
        HOTEL = 'HOTEL', 'Hotel'
        AGENCY = 'AGENCY', 'Agencia de Viajes'
        GUIDE = 'GUIDE', 'Guía Turístico'
        TRANSPORT = 'TRANSPORT', 'Transportadora Turística'
        # Añadimos otros tipos para compatibilidad
        BAR_DISCO = 'BAR_DISCO', 'Bar o Discoteca'
        ARTISAN = 'ARTISAN', 'Artesano'

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil_prestador'
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='perfiles'
    )
    nombre_comercial = models.CharField(max_length=255, verbose_name="Nombre Comercial")
    provider_type = models.CharField(max_length=20, choices=ProviderTypes.choices, default=ProviderTypes.HOTEL)

    # Mantenemos otros campos relevantes del modelo original 'Perfil'
    telefono_principal = models.CharField(max_length=50, blank=True)
    email_comercial = models.EmailField(max_length=255, blank=True)
    direccion = models.CharField(max_length=255, blank=True)

    is_verified = models.BooleanField(default=False, help_text="Verificado por el Super Admin")

    def __str__(self):
        return self.nombre_comercial
