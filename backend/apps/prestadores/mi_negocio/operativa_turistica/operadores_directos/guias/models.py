from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from decimal import Decimal
import uuid

from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import TenantAwareModel
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.productos_servicios.models import Product

class Skill(TenantAwareModel):
    """
    Representa una competencia, certificación o idioma que un guía puede tener.
    """
    class SkillType(models.TextChoices):
        SPECIALIZATION = 'SPECIALIZATION', _('Especialización')
        CERTIFICATION = 'CERTIFICATION', _('Certificación')
        LANGUAGE = 'LANGUAGE', _('Idioma')

    nombre = models.CharField(_("Nombre de la Competencia"), max_length=150)
    skill_type = models.CharField(_("Tipo"), max_length=20, choices=SkillType.choices)

    def __str__(self):
        return self.nombre

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class GuiaTuristico(TenantAwareModel):
    """
    Representa a un guía humano vinculado al prestador.
    """
    class Nivel(models.TextChoices):
        JUNIOR = 'JUNIOR', _('Junior')
        SENIOR = 'SENIOR', _('Senior')
        ESPECIALIZADO = 'ESPECIALIZADO', _('Especializado')

    class Estado(models.TextChoices):
        ACTIVO = 'ACTIVO', _('Activo')
        SUSPENDIDO = 'SUSPENDIDO', _('Suspendido')
        VENCIDO_DOCUMENTAL = 'VENCIDO_DOCUMENTAL', _('Vencido por Documentación')

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil_guia'
    )
    identificacion = models.CharField(max_length=50, unique=True)
    nivel = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.JUNIOR)
    idiomas = models.JSONField(default=list, help_text=_("Lista de idiomas que habla el guía"))
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.ACTIVO)

    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return f"{self.usuario.get_full_name()} ({self.identificacion})"

    class Meta(TenantAwareModel.Meta):
        verbose_name = "Guía Turístico"
        verbose_name_plural = "Guías Turísticos"
        app_label = 'prestadores'

class CertificacionGuia(TenantAwareModel):
    """
    Control documental de las certificaciones del guía.
    """
    class EstadoValidacion(models.TextChoices):
        PENDIENTE = 'PENDIENTE', _('Pendiente')
        VALIDADO = 'VALIDADO', _('Validado')
        RECHAZADO = 'RECHAZADO', _('Rechazado')
        VENCIDO = 'VENCIDO', _('Vencido')

    guia = models.ForeignKey(GuiaTuristico, on_delete=models.CASCADE, related_name='certificaciones')
    tipo_certificacion = models.CharField(max_length=100)
    entidad_emisora = models.CharField(max_length=150)
    issue_date = models.DateField()
    fecha_vencimiento = models.DateField()
    documento_adjunto_ref_id = models.UUIDField(null=True, blank=True) # Ref a Gestión Archivística
    estado_validacion = models.CharField(
        max_length=20,
        choices=EstadoValidacion.choices,
        default=EstadoValidacion.PENDIENTE
    )

    def is_valid(self):
        from django.utils import timezone
        return self.estado_validacion == self.EstadoValidacion.VALIDADO and self.fecha_vencimiento >= timezone.now().date()

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class LocalRutaTuristica(TenantAwareModel):
    """
    Ruta turística local operada por el prestador.
    Puede estar vinculada a una RutaTuristica global de la app api.
    """
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    ruta_global_ref_id = models.UUIDField(null=True, blank=True)
    duracion_estimada_horas = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class Itinerario(models.Model):
    """
    Pasos o paradas de una ruta.
    """
    ruta = models.ForeignKey(LocalRutaTuristica, on_delete=models.CASCADE, related_name='itinerarios')
    orden = models.PositiveIntegerField()
    actividad = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    tiempo_estimado_minutos = models.PositiveIntegerField()

    class Meta:
        ordering = ['orden']
        app_label = 'prestadores'

class GrupoTuristico(TenantAwareModel):
    """
    Grupo de turistas para un servicio.
    """
    nombre = models.CharField(max_length=100, blank=True)
    numero_turistas = models.PositiveIntegerField()
    contacto_principal = models.CharField(max_length=255)
    observaciones = models.TextField(blank=True)

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class ServicioGuiado(TenantAwareModel):
    """
    Ejecución de una ruta para un grupo con un guía.
    """
    class Estado(models.TextChoices):
        PROGRAMADO = 'PROGRAMADO', _('Programado')
        CONFIRMADO = 'CONFIRMADO', _('Confirmado')
        EN_CURSO = 'EN_CURSO', _('En Curso')
        FINALIZADO = 'FINALIZADO', _('Finalizado')
        CANCELADO = 'CANCELADO', _('Cancelado')
        LIQUIDADO = 'LIQUIDADO', _('Liquidado')

    ruta = models.ForeignKey(LocalRutaTuristica, on_delete=models.PROTECT)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    grupo = models.ForeignKey(GrupoTuristico, on_delete=models.PROTECT)
    guia_asignado = models.ForeignKey(GuiaTuristico, on_delete=models.SET_NULL, null=True, related_name='servicios')

    precio_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    comision_guia = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PROGRAMADO)

    # Vinculación ERP/Gobernanza
    operacion_comercial_ref_id = models.UUIDField(null=True, blank=True)
    governance_intention_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.ruta.nombre} - {self.fecha} {self.hora_inicio}"

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class LiquidacionGuia(TenantAwareModel):
    """
    Registro de pago de comisiones al guía.
    """
    guia = models.ForeignKey(GuiaTuristico, on_delete=models.CASCADE, related_name='liquidaciones')
    periodo_inicio = models.DateField()
    periodo_fin = models.DateField()
    monto_total = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_liquidacion = models.DateTimeField(auto_now_add=True)

    asiento_contable_ref_id = models.UUIDField(null=True, blank=True)

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class IncidenciaServicio(TenantAwareModel):
    """
    Registro de problemas durante un servicio guiado.
    """
    class Gravedad(models.TextChoices):
        BAJA = 'BAJA', _('Baja')
        MEDIA = 'MEDIA', _('Media')
        ALTA = 'ALTA', _('Alta')
        CRITICA = 'CRITICA', _('Crítica')

    servicio = models.ForeignKey(ServicioGuiado, on_delete=models.CASCADE, related_name='incidencias')
    descripcion = models.TextField()
    gravedad = models.CharField(max_length=20, choices=Gravedad.choices, default=Gravedad.BAJA)
    resuelto = models.BooleanField(default=False)
    staff_reporta = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta(TenantAwareModel.Meta):
        app_label = 'prestadores'

class TourDetail(models.Model):
    """
    Detalles que convierten un Product en un Tour.
    """
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='tour_details'
    )
    required_skills = models.ManyToManyField(
        Skill,
        blank=True,
        help_text=_("Competencias requeridas para que un guía pueda realizar este tour.")
    )

    def __str__(self):
        return f"Detalles de Tour para: {self.product.nombre}"

    class Meta:
        app_label = 'prestadores'
