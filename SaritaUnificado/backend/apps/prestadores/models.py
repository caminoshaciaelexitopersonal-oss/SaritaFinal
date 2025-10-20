from django.db import models
from django.conf import settings

class CategoriaPrestador(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, help_text="Versión del nombre amigable para URLs")
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Categoría de Prestador"
        verbose_name_plural = "Categorías de Prestadores"

class Perfil(models.Model):
    """
    Modelo unificado para el perfil del prestador de servicios turísticos.
    """
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil_prestador'
    )
    nombre_comercial = models.CharField(max_length=255, verbose_name="Nombre Comercial")
    categoria = models.ForeignKey(CategoriaPrestador, on_delete=models.SET_NULL, null=True, blank=True)
    telefono_principal = models.CharField(max_length=50, blank=True)
    email_comercial = models.EmailField(max_length=255, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    latitud = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitud = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    descripcion_corta = models.TextField(blank=True)
    logo = models.ImageField(upload_to='logos_prestadores/', blank=True, null=True)
    sitio_web = models.URLField(max_length=255, blank=True)
    redes_sociales = models.JSONField(blank=True, null=True, default=dict)

    class EstadoChoices(models.TextChoices):
        PENDIENTE = 'Pendiente', 'Pendiente de Revisión'
        ACTIVO = 'Activo', 'Activo y Visible'
        RECHAZADO = 'Rechazado', 'Rechazado'
        INACTIVO = 'Inactivo', 'Inactivo por el Usuario'

    estado = models.CharField(
        max_length=20,
        choices=EstadoChoices.choices,
        default=EstadoChoices.PENDIENTE
    )
    puntuacion_total = models.PositiveIntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_comercial

    class Meta:
        verbose_name = "Perfil de Prestador"
        verbose_name_plural = "Perfiles de Prestadores"
from django.db import models
from django.utils.translation import gettext_lazy as _

class Cliente(models.Model):
    """
    Modelo para gestionar los clientes (CRM) de un prestador de servicios.
    """
    perfil = models.ForeignKey('Perfil', on_delete=models.CASCADE, related_name='clientes')
    nombre = models.CharField(_("Nombre del Cliente"), max_length=255)
    email = models.EmailField(_("Correo Electrónico"), max_length=255, unique=True, blank=True, null=True)
    telefono = models.CharField(_("Teléfono"), max_length=50, blank=True)
    notas = models.TextField(_("Notas Internas"), blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - Cliente de {self.perfil.nombre_negocio}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nombre']
from django.db import models
from django.utils.translation import gettext_lazy as _

class ProductoServicio(models.Model):
    """
    Modelo para gestionar los productos o servicios ofrecidos por un prestador.
    """
    perfil = models.ForeignKey('Perfil', on_delete=models.CASCADE, related_name='productos_servicios')
    nombre = models.CharField(_("Nombre del Producto/Servicio"), max_length=255)
    descripcion = models.TextField(_("Descripción"), blank=True, null=True)
    precio = models.DecimalField(_("Precio"), max_digits=12, decimal_places=2, default=0.00)

    class Tipo(models.TextChoices):
        PRODUCTO = 'PRODUCTO', _('Producto')
        SERVICIO = 'SERVICIO', _('Servicio')

    tipo = models.CharField(_("Tipo"), max_length=50, choices=Tipo.choices, default=Tipo.PRODUCTO)

    # Campos específicos para productos (inventario)
    cantidad_disponible = models.PositiveIntegerField(_("Cantidad Disponible"), default=1, help_text=_("Para servicios, usualmente es 1 o se deja en blanco."))
    unidad_medida = models.CharField(_("Unidad de Medida"), max_length=50, blank=True, help_text=_("Ej: unidades, kg, horas, etc."))

    activo = models.BooleanField(_("Activo"), default=True, help_text=_("Indica si el producto/servicio está disponible para la venta."))
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} - {self.perfil.nombre_negocio}"

    class Meta:
        verbose_name = "Producto o Servicio"
        verbose_name_plural = "Productos y Servicios"
        ordering = ['nombre']
from django.db import models
from django.utils.translation import gettext_lazy as _

class Inventario(models.Model):
    """
    Modelo para gestionar el inventario de un prestador.
    """
    perfil = models.ForeignKey('Perfil', on_delete=models.CASCADE, related_name='inventario')
    nombre_item = models.CharField(_("Nombre del Ítem"), max_length=255)
    descripcion = models.TextField(_("Descripción"), blank=True, null=True)
    cantidad = models.PositiveIntegerField(_("Cantidad Disponible"), default=0)
    unidad = models.CharField(_("Unidad de Medida"), max_length=50, help_text=_("Ej: unidades, kg, litros"))
    punto_reorden = models.PositiveIntegerField(_("Punto de Reorden"), default=0, help_text=_("Cantidad mínima antes de necesitar reabastecimiento"))
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_item} ({self.cantidad} {self.unidad})"

    class Meta:
        verbose_name = "Ítem de Inventario"
        verbose_name_plural = "Ítems de Inventario"
        ordering = ['nombre_item']
from django.db import models
from django.utils.translation import gettext_lazy as _

class Costo(models.Model):
    """
    Modelo para gestionar los costos operativos de un prestador.
    """
    perfil = models.ForeignKey('Perfil', on_delete=models.CASCADE, related_name='costos')
    concepto = models.CharField(_("Concepto del Costo"), max_length=255)
    monto = models.DecimalField(_("Monto"), max_digits=12, decimal_places=2)
    fecha = models.DateField(_("Fecha del Costo"))
    es_recurrente = models.BooleanField(_("¿Es Recurrente?"), default=False)

    class Tipo(models.TextChoices):
        FIJO = 'FIJO', _('Fijo')
        VARIABLE = 'VARIABLE', _('Variable')

    tipo_costo = models.CharField(_("Tipo de Costo"), max_length=50, choices=Tipo.choices, default=Tipo.VARIABLE)

    def __str__(self):
        return f"{self.concepto} - ${self.monto}"

    class Meta:
        verbose_name = "Costo Operativo"
        verbose_name_plural = "Costos Operativos"
        ordering = ['-fecha']
