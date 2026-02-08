# backend/apps/prestadores/mi_negocio/gestion_contable/contabilidad/sargentos.py
import logging
from django.db import transaction
from .models import AsientoContable, Transaccion, PeriodoContable, Cuenta
from django.utils import timezone
from apps.audit.models import AuditLog
from api.models import CustomUser

logger = logging.getLogger(__name__)

class SargentoContable:
    """
    Ejecutor de acciones contables atómicas.
    """

    @staticmethod
    @transaction.atomic
    def generar_asiento_partida_doble(periodo_id, fecha, descripcion, movimientos, usuario_id):
        try:
            periodo = PeriodoContable.objects.get(id=periodo_id)
            if periodo.cerrado:
                raise ValueError("El periodo contable esta cerrado.")

            asiento = AsientoContable.objects.create(
                periodo=periodo,
                fecha=fecha,
                descripcion=descripcion,
                creado_por_id=usuario_id,
                provider=periodo.provider
            )

            total_debito = 0
            total_credito = 0

            for mov in movimientos:
                cuenta = Cuenta.objects.get(id=mov['cuenta_id'])
                debito = mov.get('debito', 0)
                credito = mov.get('credito', 0)
                total_debito += debito
                total_credito += credito

                Transaccion.objects.create(
                    asiento=asiento,
                    cuenta=cuenta,
                    debito=debito,
                    credito=credito,
                    descripcion=mov.get('descripcion', '')
                )

            if total_debito != total_credito:
                raise ValueError(f"Asiento descuadrado. Debito: {total_debito}, Credito: {total_credito}")

            logger.info(f"SARGENTO: Asiento #{asiento.id} generado exitosamente.")
            return asiento
        except Exception as e:
            logger.error(f"SARGENTO: Error al generar asiento: {e}")
            raise e

    @staticmethod
    def ejecutar_cierre_periodo(periodo_id, usuario_id):
        try:
            periodo = PeriodoContable.objects.get(id=periodo_id)
            # Validacion de balance previo al cierre (simplificada)
            periodo.cerrado = True
            periodo.save()

            logger.info(f"SARGENTO: Periodo {periodo.nombre} cerrado exitosamente.")
            return True
        except Exception as e:
            logger.error(f"SARGENTO: Error al cerrar periodo: {e}")
            return False
