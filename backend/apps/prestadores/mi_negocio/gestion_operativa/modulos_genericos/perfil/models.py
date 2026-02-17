# backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/perfil/models.py
import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone

# --- MODELOS CANÓNICOS DEL DOMINIO OPERATIVO ---

class BaseModel(models.Model):
    """
    Modelo base abstracto que añade campos de auditoría comunes.
    Ahora reside en el dominio operativo como base para sus modelos.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

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
    EL INQUILINO (TENANT). EL EJE DEL SISTEMA DE PRESTADORES.
    Representa a una empresa prestadora de servicios.
    Definición canónica movida a gestion_operativa para autonomía del dominio.
    """
    class ProviderTypes(models.TextChoices):
        RESTAURANT = 'RESTAURANT', 'Restaurante'
        HOTEL = 'HOTEL', 'Hotel'
        AGENCY = 'AGENCY', 'Agencia de Viajes'
        GUIDE = 'GUIDE', 'Guía Turístico'
        TRANSPORT = 'TRANSPORT', 'Transportadora Turística'
        BAR_DISCO = 'BAR_DISCO', 'Bar o Discoteca'
        ARTISAN = 'ARTISAN', 'Artesano'

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil_prestador'
    )
    # ACoplamiento a Company ELIMINADO según Directriz 14.
    # Reemplazado por una referencia externa de UUID.
    company_id = models.UUIDField(null=True, blank=True) # Permite nulos mientras se migra la lógica

    nombre_comercial = models.CharField(max_length=255, verbose_name="Nombre Comercial")
    provider_type = models.CharField(max_length=20, choices=ProviderTypes.choices, default=ProviderTypes.HOTEL)

    telefono_principal = models.CharField(max_length=50, blank=True)
    email_comercial = models.EmailField(max_length=255, blank=True)
    direccion = models.CharField(max_length=255, blank=True)

    is_verified = models.BooleanField(default=False, help_text="Verificado por el Super Admin")

    def __str__(self):
        return self.nombre_comercial


class TenantAwareModel(BaseModel):
    """
    Modelo base abstracto restaurado para los datos que pertenecen a un inquilino (ProviderProfile).
    Es una dependencia interna del dominio operativo, totalmente permitida.
    """
    provider = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name="%(class)s_items", null=True, blank=True)

    class Meta(BaseModel.Meta):
        abstract = True
