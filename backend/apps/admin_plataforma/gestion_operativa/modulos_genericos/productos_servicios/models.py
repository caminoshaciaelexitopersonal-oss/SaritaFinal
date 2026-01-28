from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField

from ..perfil.models import TenantAwareModel
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import CategoriaPrestador as OperationalTag
from ..reservas.models import PoliticaCancelacion

class Product(TenantAwareModel):
    """
    Modelo genérico y polimórfico para cualquier 'cosa' vendible o reservable.
    Adaptado del modelo de referencia `tourism_core`.
    """
    class ProductNature(models.TextChoices):
        SERVICE = 'SERVICE', _('Servicio (Reservable)')
        GOOD = 'GOOD', _('Bien Físico (Comprable)')
        PACKAGE = 'PACKAGE', _('Paquete (Compuesto)')

    nombre = models.CharField(_("Nombre"), max_length=200)
    descripcion = models.TextField(_("Descripción"), blank=True)
    nature = models.CharField(_("Naturaleza"), max_length=10, choices=ProductNature.choices)
    base_price = MoneyField(_("Precio Base"), max_digits=19, decimal_places=2, default_currency='COP')
    stock = models.PositiveIntegerField(_("Stock/Capacidad"), default=1, help_text=_("Capacidad por evento, o unidades de un bien."))

    is_packageable = models.BooleanField(_("Es Empaquetable"), default=False, help_text=_("¿Puede este servicio ser parte de un paquete de agencia?"))
    operational_tags = models.ManyToManyField(OperationalTag, blank=True)
    cancellation_policy = models.ForeignKey(PoliticaCancelacion, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto/Servicio"
        verbose_name_plural = "Productos/Servicios"
        app_label = 'prestadores'
