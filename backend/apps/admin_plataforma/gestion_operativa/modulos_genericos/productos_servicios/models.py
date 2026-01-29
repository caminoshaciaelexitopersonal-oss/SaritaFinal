import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from ..perfil.models import TenantAwareModel, CategoriaPrestador as OperationalTag

class Product(TenantAwareModel):
    id_publico = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Tipo(models.TextChoices):
        PRODUCTO = 'PRODUCTO', _('Producto')
        SERVICIO = 'SERVICIO', _('Servicio')

    nombre = models.CharField(_("Nombre"), max_length=200)
    descripcion = models.TextField(_("Descripción"), blank=True)
    tipo = models.CharField(
        _("Tipo"),
        max_length=10,
        choices=Tipo.choices,
        default=Tipo.PRODUCTO
    )
    base_price = MoneyField(_("Precio Base"), max_digits=19, decimal_places=2, default_currency='COP')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"[ADMIN] {self.nombre}"

    class Meta:
        verbose_name = "Producto/Servicio (Plataforma)"
        verbose_name_plural = "Productos/Servicios (Plataforma)"
        app_label = 'admin_operativa'
