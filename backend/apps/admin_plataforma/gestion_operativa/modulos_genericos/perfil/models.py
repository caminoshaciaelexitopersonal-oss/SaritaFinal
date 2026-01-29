from django.db import models
from django.conf import settings

class BaseModel(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CategoriaPrestador(BaseModel):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'admin_operativa'
        verbose_name = "Categoría de Operación (Admin)"

class ProviderProfile(BaseModel):
    """
    Perfil de la Organización para el ERP del Super Admin.
    Representa a la 'Plataforma Sarita' como entidad operativa.
    """
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='admin_perfil_context'
    )
    nombre_negocio = models.CharField(max_length=255, default="Plataforma Sarita")
    nit = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nombre_negocio

    class Meta:
        app_label = 'admin_operativa'
        verbose_name = "Perfil de Plataforma"

class TenantAwareModel(BaseModel):
    organization = models.ForeignKey(
        ProviderProfile,
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_records'
    )

    class Meta:
        abstract = True
