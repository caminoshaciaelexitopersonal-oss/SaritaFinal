# backend/apps/prestadores/mi_negocio/gestion_contable/contabilidad/sargentos.py
import logging
from django.db import transaction
from .models import AsientoContable, Transaccion, PeriodoContable, Cuenta, PlanDeCuentas
from django.utils import timezone
from .services import StandardChartOfAccountsService
from apps.audit.models import AuditLog
from api.models import CustomUser

logger = logging.getLogger(__name__)

class SargentoContable:
    """
    Ejecutor de acciones contables atómicas.
    """

    @staticmethod
    @transaction.atomic
    def generar_asiento_partida_doble(periodo_id, date, description, movimientos, usuario_id, provider=None):
        try:
            if not periodo_id and provider:
                # Buscar o crear periodo vigente
                now = timezone.now()
                periodo, _ = PeriodoContable.objects.get_or_create(
                    provider=provider,
                    is_closed=False,
                    defaults={
                        "name": f"Periodo {now.year}-{now.month:02d}",
                        "start_date": now.replace(day=1, hour=0, minute=0, second=0, microsecond=0),
                        "end_date": (now.replace(day=28) + timezone.timedelta(days=4)).replace(day=1) - timezone.timedelta(days=1)
                    }
                )
                periodo_id = periodo.id

            periodo = PeriodoContable.objects.get(id=periodo_id)
            if periodo.is_closed:
                raise ValueError("El periodo contable esta cerrado.")

            asiento = AsientoContable.objects.create(
                periodo=periodo,
                date=date,
                description=description,
                creado_por_id=usuario_id,
                provider=periodo.provider
            )

            total_debit = 0
            total_credit = 0

            for mov in movimientos:
                if 'cuenta_id' in mov:
                    cuenta = Cuenta.objects.get(id=mov['cuenta_id'])
                elif 'cuenta_code' in mov:
                    # Buscar por código dentro del plan del provider
                    try:
                        cuenta = Cuenta.objects.get(
                            plan_de_cuentas__provider=periodo.provider,
                            code=mov['cuenta_code']
                        )
                    except Cuenta.DoesNotExist:
                        # Si no existe y es una cuenta estándar, podríamos intentar inicializar
                        if not PlanDeCuentas.objects.filter(provider=periodo.provider).exists():
                            StandardChartOfAccountsService.inicializar_contabilidad(periodo.provider)
                            cuenta = Cuenta.objects.get(
                                plan_de_cuentas__provider=periodo.provider,
                                code=mov['cuenta_code']
                            )
                        else:
                            raise
                else:
                    raise ValueError("Debe proporcionar cuenta_id o cuenta_code")

                if not cuenta.is_active:
                    raise ValueError(f"La cuenta {cuenta.code} está inactiva.")

                debit = mov.get('debit', 0)
                credit = mov.get('credit', 0)
                total_debit += debit
                total_credit += credit

                Transaccion.objects.create(
                    asiento=asiento,
                    cuenta=cuenta,
                    debit=debit,
                    credit=credit,
                    description=mov.get('description', '')
                )

            if total_debit != total_credit:
                raise ValueError(f"Asiento descuadrado. Debito: {total_debit}, Credito: {total_credit}")

            # Registro en AuditLog
            user = CustomUser.objects.get(id=usuario_id)
            AuditLog.objects.create(
                user=user,
                username=user.username,
                action="ASIENTO_CONTABLE_CREADO",
                details={
                    "asiento_id": str(asiento.id),
                    "monto_total": float(total_debit),
                    "descripcion": description
                }
            )

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
            periodo.is_closed = True
            periodo.save()

            logger.info(f"SARGENTO: Periodo {periodo.name} cerrado exitosamente.")
            return True
        except Exception as e:
            logger.error(f"SARGENTO: Error al cerrar periodo: {e}")
            return False
