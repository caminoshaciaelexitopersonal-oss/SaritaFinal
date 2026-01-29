from django.db import models

class CuentaBancaria(models.Model):
    perfil_ref_id = models.UUIDField()
    banco = models.CharField(max_length=100)
    numero_cuenta = models.CharField(max_length=50, unique=True)
    tipo_cuenta = models.CharField(max_length=50)
    saldo_actual = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    activa = models.BooleanField(default=True)

    class Meta:
        app_label = 'admin_financiera'
        verbose_name = "Cuenta Bancaria (Admin)"

class TransaccionBancaria(models.Model):
    cuenta = models.ForeignKey(CuentaBancaria, on_delete=models.CASCADE, related_name='admin_transacciones')
    fecha = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2)
    descripcion = models.CharField(max_length=255)

    class Meta:
        app_label = 'admin_financiera'
        verbose_name = "Transacción Bancaria (Admin)"

class OrdenPago(models.Model):
    class EstadoPago(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        PAGADA = 'PAGADA', 'Pagada'
        CANCELADA = 'CANCELADA', 'Cancelada'

    perfil_ref_id = models.UUIDField()
    cuenta_bancaria_ref_id = models.UUIDField()
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=18, decimal_places=2)
    concepto = models.CharField(max_length=255)
    estado = models.CharField(max_length=20, choices=EstadoPago.choices, default=EstadoPago.PENDIENTE)

    class Meta:
        app_label = 'admin_financiera'
        verbose_name = "Orden de Pago (Admin)"
