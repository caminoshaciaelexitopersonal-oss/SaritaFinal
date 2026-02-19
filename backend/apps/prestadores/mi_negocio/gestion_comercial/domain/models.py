# backend/apps/prestadores/mi_negocio/gestion_comercial/domain/models.py
from django.db import models
from django.db.models import Sum
from django.conf import settings
from decimal import Decimal
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile, TenantAwareModel

class OperacionComercial(TenantAwareModel):
    class Estado(models.TextChoices):
        BORRADOR = 'BORRADOR', 'Borrador'
        CONFIRMADA = 'CONFIRMADA', 'Confirmada'
        COMERCIAL_CONFIRMADA = 'COMERCIAL_CONFIRMADA', 'Comercial Confirmada'
        FACTURADA = 'FACTURADA', 'Facturada'
        ANULADA = 'ANULADA', 'Anulada'

    class TipoOperacion(models.TextChoices):
        VENTA = 'VENTA', 'Venta de Productos/Servicios'
        CONTRATO = 'CONTRATO', 'Contrato'

    perfil_ref_id = models.UUIDField(null=True, blank=True) # Mantenido para retrocompatibilidad
    cliente_ref_id = models.UUIDField()
    tipo_operacion = models.CharField(max_length=20, choices=TipoOperacion.choices, default=TipoOperacion.VENTA)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.BORRADOR)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    impuestos = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_confirmacion = models.DateTimeField(null=True, blank=True)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    documento_archivistico_ref_id = models.UUIDField(null=True, blank=True)

    def recalcular_totales(self):
        totales = self.items.aggregate(total=Sum('subtotal'))
        self.subtotal = totales['total'] or 0
        self.total = self.subtotal # Simplificado
        self.save()

class ItemOperacionComercial(models.Model):
    operacion = models.ForeignKey(OperacionComercial, on_delete=models.CASCADE, related_name='items')
    producto_ref_id = models.UUIDField()
    descripcion = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

from apps.core_erp.base.base_models import BaseInvoice

class FacturaVenta(BaseInvoice, TenantAwareModel):
    class Estado(models.TextChoices):
        EMITIDA = 'EMITIDA', 'Emitida'
        PAGADA = 'PAGADA', 'Pagada'
        ANULADA = 'ANULADA', 'Anulada'

    class EstadoDIAN(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        ACEPTADA = 'ACEPTADA', 'Aceptada'
        RECHAZADA = 'RECHAZADA', 'Rechazada'

    operacion = models.OneToOneField(OperacionComercial, on_delete=models.PROTECT, related_name='factura')
    perfil_ref_id = models.UUIDField(null=True, blank=True)
    cliente_ref_id = models.UUIDField()
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    impuestos = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    estado_dian = models.CharField(max_length=20, choices=EstadoDIAN.choices, default=EstadoDIAN.PENDIENTE)
    cufe = models.CharField(max_length=255, null=True, blank=True)
    dian_response_log = models.JSONField(null=True, blank=True)
    documento_archivistico_ref_id = models.UUIDField(null=True, blank=True)

    def recalcular_totales(self):
        totales = self.items.aggregate(total=Sum('subtotal'))
        self.subtotal = totales['total'] or 0
        self.total_amount = self.subtotal
        self.save()

class ItemFactura(models.Model):
    factura = models.ForeignKey(FacturaVenta, on_delete=models.CASCADE, related_name='items')
    producto_ref_id = models.UUIDField()
    descripcion = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
    impuestos = models.DecimalField(max_digits=12, decimal_places=2, default=0)

class ReciboCaja(models.Model):
    perfil_ref_id = models.UUIDField()
    cuenta_bancaria_ref_id = models.UUIDField()
    factura = models.ForeignKey(FacturaVenta, on_delete=models.CASCADE, related_name='recibos_caja')
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)

class ContratoComercial(models.Model):
    class EstadoContrato(models.TextChoices):
        BORRADOR = 'BORRADOR', 'Borrador'
        FIRMADO = 'FIRMADO', 'Firmado'
        VIGENTE = 'VIGENTE', 'Vigente'
        FINALIZADO = 'FINALIZADO', 'Finalizado'
        INCUMPLIDO = 'INCUMPLIDO', 'Incumplido'

    operacion = models.OneToOneField(OperacionComercial, on_delete=models.CASCADE, related_name='contrato_formal')
    perfil_ref_id = models.UUIDField()
    cliente_ref_id = models.UUIDField()
    terminos_y_condiciones = models.TextField()
    fecha_firma = models.DateTimeField(null=True, blank=True)
    hash_firma_digital = models.CharField(max_length=64, null=True, blank=True)
    estado = models.CharField(max_length=20, choices=EstadoContrato.choices, default=EstadoContrato.BORRADOR)
    evidencia_archivistica_ref_id = models.UUIDField(null=True, blank=True)

class OrdenOperativa(models.Model):
    class EstadoOrden(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        EN_PROCESO = 'EN_PROCESO', 'En Proceso'
        COMPLETADA = 'COMPLETADA', 'Completada'
        CANCELADA = 'CANCELADA', 'Cancelada'

    contrato = models.ForeignKey(ContratoComercial, on_delete=models.CASCADE, related_name='ordenes_operativas')
    perfil_ref_id = models.UUIDField()
    descripcion_servicio = models.TextField()
    fecha_programada = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=EstadoOrden.choices, default=EstadoOrden.PENDIENTE)
    responsable_ref_id = models.UUIDField(null=True, blank=True)

# --- MODELOS FACTURACIÓN ELECTRÓNICA DIAN (FASE INTEGRAL) ---

class DianResolution(TenantAwareModel):
    numero_resolucion = models.CharField(max_length=100)
    prefijo = models.CharField(max_length=10)
    desde = models.PositiveIntegerField()
    hasta = models.PositiveIntegerField()
    consecutivo_actual = models.PositiveIntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    es_vigente = models.BooleanField(default=True)

    class Meta(TenantAwareModel.Meta):
        verbose_name = "Resolución DIAN"
        verbose_name_plural = "Resoluciones DIAN"

class DianCertificate(TenantAwareModel):
    nombre = models.CharField(max_length=255)
    archivo_p12 = models.FileField(upload_to='certificates/dian/')
    password_encrypted = models.CharField(max_length=512) # Almacenado encriptado
    fecha_vencimiento = models.DateField()
    es_activo = models.BooleanField(default=True)

    class Meta(TenantAwareModel.Meta):
        verbose_name = "Certificado Digital DIAN"

class DianSoftwareConfig(TenantAwareModel):
    class Ambiente(models.TextChoices):
        PRUEBAS = 'PRUEBAS', 'Pruebas / Habilitación'
        PRODUCCION = 'PRODUCCION', 'Producción'

    software_id = models.UUIDField()
    pin = models.CharField(max_length=10)
    ambiente = models.CharField(max_length=20, choices=Ambiente.choices, default=Ambiente.PRUEBAS)
    test_set_id = models.CharField(max_length=255, null=True, blank=True) # Para habilitación

    class Meta(TenantAwareModel.Meta):
        verbose_name = "Configuración Software DIAN"

class DianStatusLog(models.Model):
    factura = models.ForeignKey(FacturaVenta, on_delete=models.CASCADE, related_name='dian_logs')
    timestamp = models.DateTimeField(auto_now_add=True)
    request_xml = models.TextField()
    response_xml = models.TextField()
    estado_v_previa = models.JSONField() # Resultado de validación previa
    success = models.BooleanField()
    error_detail = models.TextField(null=True, blank=True)
