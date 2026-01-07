from .models import OrdenPago, CuentaBancaria
from ..gestion_contable.nomina.models import Empleado
from ..gestion_contable.empresa.models import Tercero
from decimal import Decimal
from django.utils import timezone

class PagoService:
    @staticmethod
    def crear_orden_pago_empleado(perfil, cuenta_bancaria: CuentaBancaria, empleado: Empleado, monto: Decimal, concepto: str):
        return OrdenPago.objects.create(
            perfil=perfil,
            cuenta_bancaria_origen=cuenta_bancaria,
            beneficiario_empleado=empleado,
            fecha_pago=timezone.now().date(),
            monto=monto,
            concepto=concepto,
            estado=OrdenPago.EstadoPago.PAGADA
        )
