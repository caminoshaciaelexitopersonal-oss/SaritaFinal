from django.db import models
from django.conf import settings
from decimal import Decimal
from django.core.exceptions import ValidationError
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil

class CuentaBancaria(models.Model):
    class TipoCuenta(models.TextChoices):
        AHORROS = 'AHORROS', 'Ahorros'
        CORRIENTE = 'CORRIENTE', 'Corriente'

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='cuentas_bancarias')
    banco = models.CharField(max_length=100)
    numero_cuenta = models.CharField(max_length=50)
    tipo_cuenta = models.CharField(max_length=20, choices=TipoCuenta.choices)
    saldo_actual = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
    titular = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.banco} - {self.numero_cuenta} ({self.titular})"

class TransaccionBancaria(models.Model):
    class TipoTransaccion(models.TextChoices):
        INGRESO = 'INGRESO', 'Ingreso'
        EGRESO = 'EGRESO', 'Egreso'
        TRANSFERENCIA = 'TRANSFERENCIA', 'Transferencia'

    cuenta = models.ForeignKey(CuentaBancaria, on_delete=models.CASCADE, related_name='transacciones')
    fecha = models.DateField()
    tipo = models.CharField(max_length=20, choices=TipoTransaccion.choices)
    monto = models.DecimalField(max_digits=18, decimal_places=2)
    descripcion = models.CharField(max_length=255)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} de {self.monto} en {self.cuenta.numero_cuenta}"

    def save(self, *args, **kwargs):
        # Evitar doble contabilidad si el objeto ya existe
        is_new = self._state.adding

        super().save(*args, **kwargs)

        if is_new:
            cuenta = self.cuenta
            if self.tipo == self.TipoTransaccion.INGRESO:
                cuenta.saldo_actual += self.monto
            elif self.tipo == self.TipoTransaccion.EGRESO:
                if cuenta.saldo_actual < self.monto:
                    raise ValidationError("Saldo insuficiente en la cuenta para realizar el egreso.")
                cuenta.saldo_actual -= self.monto
            # Transferencia se maneja como dos movimientos: un egreso y un ingreso
            cuenta.save()
